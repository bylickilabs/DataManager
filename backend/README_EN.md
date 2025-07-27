# 🗃️ Universal Data Manager – EN

The Universal Data Manager is a production-ready backend application supporting **MySQL**, **PostgreSQL**, and **MongoDB** simultaneously.

## 🚀 Features

- SQL queries to MySQL/PostgreSQL via REST API
- MongoDB queries using POST requests with filter object
- CORS enabled for frontend integration
- Ideal for DevOps, analytics tools, and multi-DB environments

## ⚙️ Usage

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Sample request for SQL

```json
POST /sql/query
{
  "db_type": "mysql",
  "query": "SELECT * FROM users;"
}
```

### Sample request for MongoDB

```json
POST /mongo/query
{
  "collection": "products",
  "filter": {}
}
```
