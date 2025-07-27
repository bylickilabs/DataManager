import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
import os

MYSQL_URL = os.getenv("MYSQL_URL", "mysql+pymysql://user:pass@localhost/db")
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql+psycopg2://user:pass@localhost/db")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

engine_mysql = create_engine(MYSQL_URL)
engine_postgres = create_engine(POSTGRES_URL)
SessionLocalMySQL = sessionmaker(bind=engine_mysql)
SessionLocalPostgres = sessionmaker(bind=engine_postgres)

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client.get_database("udm")

app = FastAPI(title="Universal Data Manager")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SQLQuery(BaseModel):
    db_type: str
    query: str

class MongoQuery(BaseModel):
    collection: str
    filter: dict

@app.post("/sql/query")
def execute_sql_query(q: SQLQuery):
    if q.db_type == "mysql":
        session = SessionLocalMySQL()
    elif q.db_type == "postgres":
        session = SessionLocalPostgres()
    else:
        raise HTTPException(status_code=400, detail="Invalid db_type")

    try:
        result = session.execute(text(q.query))
        data = [dict(r._mapping) for r in result]
        return {"success": True, "rows": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        session.close()

@app.post("/mongo/query")
async def query_mongo(q: MongoQuery):
    try:
        cursor = mongo_db[q.collection].find(q.filter)
        docs = await cursor.to_list(length=100)
        return {"success": True, "docs": docs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
