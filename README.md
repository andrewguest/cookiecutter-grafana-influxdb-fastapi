#### To use this template clone it with cookiecutter:

1. Install the `cookiecutter` library if it isn't already installed:
   `pip3 install cookiecutter`

2. Use this cookiecutter template: `cookiecutter gh:andrewguest/cookiecutter-grafana-influxdb-fastapi`

3. Answer the questions when prompted (example below):

| Prompt                           | Explanation                      |
| -------------------------------- | -------------------------------- |
| `project_name []`                | Name for this project.           |
| `influxdb_db [firstdb]`          | The InfluxDB database to create. |
| `influxdb_user [admin]`          | InfluxDB user                    |
| `influxdb_password [admin]`      | InfluxDB user's password         |
| `grafana_admin_user [admin]`     | Grafana user                     |
| `grafana_admin_password [admin]` | Grafana user's password          |

4. Start this service (these containers): `docker-compose up -d --build`

| Host Port | Service  |
| --------- | -------- |
| 3000      | Grafana  |
| 7000      | FastAPI  |
| 8086      | InfluxDB |

5. Go to `localhost:7000/influxdb` to have FastAPI send data to InfluxDB

---

#### What this template will do for you:

1. Configure the docker-compose.yml file for you, based on your input.

2. Start the InfluxDB, Grafana, and FastAPI containers.
