#### To use this template clone it with cookiecutter:

1. Install the `cookiecutter` library if it isn't already installed:
   `pip3 install cookiecutter`

2. Use this cookiecutter template: `cookiecutter gh:andrewguest/cookiecutter-fastapi-grafana-influxdb`

3. Answer the questions when prompted (example below):

| Prompt                           | Explanation                      |
| -------------------------------- | -------------------------------- |
| `project_name []`                | Name for this project.           |
| `influxdb_db []`                 | The InfluxDB database to create. |
| `influxdb_user [admin]`          | InfluxDB user                    |
| `influxdb_password [admin]`      | InfluxDB password setup.         |
| `grafana_admin_user [admin]`     | Grafana admin username           |
| `grafana_admin_password [admin]` | Grafana admin user's password    |

4. Start this service (these containers): `docker-compose up -d --build`

| Host Port | Service  |
| --------- | -------- |
| 3000      | Grafana  |
| 7000      | FastAPI  |
| 8086      | InfluxDB |

---

#### What this template will do for you:

1. Create the folder structure for this microservice:

```
|-- app
  \-- main.py (entry point for application)
|-- database (contains all database related code)
|-- routes (contains all routes to be defined)
|-- tests (contains all of the tests)
Dockerfile (build a Docker image based on the API code)
docker-compose.yml (start a container for the API and the MongoDB for this microservice)
```

2. Configure a Dockerfile needed to create an image based on this microservice.

3. Configure the docker-compose.yml file to start the API container and a MongoDB container.

4. Automatically setup the connection between the API and the MongoDB container, inside of `app/main.py`
