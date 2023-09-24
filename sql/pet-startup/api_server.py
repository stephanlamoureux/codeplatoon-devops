import json
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import psycopg2

app = Flask(__name__, template_folder="templates")

CORS(app)

conn = psycopg2.connect(
    database="pets",
    user="cpadmin",
    password="DATABASE_PASSWORD",
    host="cpewpostgres.chzveui56egk.us-east-1.rds.amazonaws.com",
    port="5432",
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pets")
def show_pets():
    cur = conn.cursor()
    cur.execute("SELECT * FROM pet")
    records = cur.fetchall()
    return jsonify(records)


@app.route("/owners")
def all_users():
    cur = conn.cursor()
    cur.execute("SELECT owner_name FROM pet")
    records = cur.fetchall()
    return jsonify(records)


@app.route("/owners/<id>")
def single_user(id):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM pet WHERE id = {id}")
    records = cur.fetchone()
    return jsonify(records)


@app.route("/owners/pets/<id>")
def single_user_pets(id):
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM pet JOIN app_user ON app_user.id = pet.id WHERE pet.id = {id}"
    )
    records = cur.fetchone()
    return jsonify(records)


app.run()
