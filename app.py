from models.db import Database
from flask import Flask
import routers.index

app = Flask(__name__)

app.register_blueprint(routers.index.router)

# Implement Database Schema
with open("schema.sql", "r") as f:
    db = Database()
    schema = "".join(f.readlines())
    for q in schema.split(";"):
        db.query(q)
    db.close()


app.run(debug=False)
