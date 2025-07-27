# 🗃️ Universal Data Manager – DE

Der Universal Data Manager ist eine produktionsreife Backend-Anwendung zur gleichzeitigen Anbindung von **MySQL**, **PostgreSQL** und **MongoDB**.

## 🚀 Funktionen

- SQL-Abfragen an MySQL/PostgreSQL via REST-API
- MongoDB-Abfragen per POST-Request mit Filterobjekt
- Unterstützt CORS für Frontend-Anbindung
- Ideal für DevOps, Analyse-Tools und Multi-DB-Umgebungen

## ⚙️ Nutzung

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Beispiel-Request für SQL

```json
POST /sql/query
{
  "db_type": "mysql",
  "query": "SELECT * FROM users;"
}
```

### Beispiel-Request für MongoDB

```json
POST /mongo/query
{
  "collection": "products",
  "filter": {}
}
```
