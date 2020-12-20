import json

from fastapi import FastAPI
from influxdb import InfluxDBClient


app = FastAPI()


client = InfluxDBClient(host="localhost", port=8086,
                        username="{{cookiecutter.influxdb_user}}",
                        password="{{cookiecutter.influxdb_password}}")
client.switch_database("{{cookiecutter.influxdb_db}}")

influx_data = json.load(open("MOCK_DATA.json", "r"))

@app.get('/influxdb')
async def influxdb():
    client.write_points(influx_data)
    return influx_data
