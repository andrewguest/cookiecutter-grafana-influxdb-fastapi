import json

from fastapi import FastAPI
from influxdb import InfluxDBClient


app = FastAPI()


client = InfluxDBClient(
    host="{{cookiecutter.project_slug}}_influxdb_1",
    port=8086,
    username="{{cookiecutter.influxdb_user}}",
    password="{{cookiecutter.influxdb_password}}",
)
client.switch_database("{{cookiecutter.influxdb_db}}")

influx_data = json.load(open("./app/MOCK_DATA.json", "r"))


@app.get("/influxdb")
async def influxdb():
    client.write_points(influx_data)
    return influx_data
