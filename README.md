# base_Flask_be
## Summary:
The REST APIs are built using Python Flask framework. Docker containers are used for development environment.


There are many ways to setup your project folder structure. One is by its function and another is app based structure which means things are grouped bp application. I have used app based approach for this task.

## Project Structure (App Based):
```bash
FlaskProject/
├── Dockerfile
├── README.md
├── store/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── category_api.py
│   │   ├── items_api.py
│   │   ├── store_api.py
│   │   ├── supplier_api.py
│   │   └── routes.py
│   ├── models.py
│   ├── db.py
│   ├── schemas.py
│   └── utils.py
├── config.py
├── docker-compose.yml
├── entrypoint.sh
├── migrations/
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── .gitignore
├── requirements.txt
└── app.py
```

### Python extensions used:
- **flask** - This is a microframework for Python
- **flask_restful** - This is an extension for Flask that adds support for quickly building of REST APIs.
- **flask_migrate** - This is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
- **flask_sqlalchemy** - This is an extension for Flask that adds support for SQLAlchemy. It allows to write ORM queries to operate against database.
- **flask_marshmallow** - This is an integration layer for Flask and marshmallow (ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes. This is used also to Serializing and Deserializing Objects.) that adds additional features to marshmallow.
- **mysqlclient** - MySQL database connector for Python
- **requests** - This is a python library to make calls to external APIs

### How to start application (using Docker)
- Clone the project using command:
    ```
    git clone https://github.com/akshayshinde97/base_Flask_be
    ```
- Go into the project directory:
    ```
    cd assignment_jsat
    ```
- Run the application by the following command:
    ```
    docker-compose up -d --build
    ```

### How to enter into a Docker containers
- into app container
    ```
    docker exec -it store_app bash
    ```
- into database container
    ```
    docker exec -it store_app_db bash
    root@e27d5a54fbb8:/# mysql -u test -p
    Enter password: test
    mysql> show databases;
    mysql> use testdb;
    mysql> show tables;
    ````
-----------------------
## Usage/Documentation

{
	"info": {
		"_postman_id": "6d02952e-5401-4492-8608-5b0f27e2eda2",
		"name": "base_backend",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "managecategory-post",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/managecategory",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managecategory"
					]
				},
				"description": "This is a get request for category api."
			},
			"response": []
		},
		{
			"name": "managecategory-post",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"name\": \"Clothes\",\r\n  \"discription\": \"Clothes for Men, Women, Kid\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managecategory",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managecategory"
					]
				}
			},
			"response": []
		},
		{
			"name": "manageitem-post",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"name\": \"Clothes\",\r\n  \"discription\": \"Clothes for Men, Women, Kid\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managecategory",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managecategory"
					]
				}
			},
			"response": []
		},
		{
			"name": "managecategory-post",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"id\":\"4\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managecategory",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managecategory"
					]
				}
			},
			"response": []
		},
		{
			"name": "managestore-get",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/managestore",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managestore"
					]
				},
				"description": "This is a get request for store api."
			},
			"response": []
		},
		{
			"name": "manageitem-get",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/managestore",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managestore"
					]
				},
				"description": "This is a get request for Item api."
			},
			"response": []
		},
		{
			"name": "managesupplier-get",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/api/managesupplier",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managesupplier"
					]
				},
				"description": "This is a get request for Supplier api."
			},
			"response": []
		},
		{
			"name": "managestore-post",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"name\": \"BLR_1\",\r\n  \"address\": \"Indiranagar\",\r\n  \"manager\":\"Vinay\",\r\n  \"contact\":\"7020424345\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managestore",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managestore"
					]
				}
			},
			"response": []
		},
		{
			"name": "managesupplier-post",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"name\": \"BLR_1\",\r\n  \"address\": \"Indiranagar\",\r\n  \"manager\":\"Vinay\",\r\n  \"contact\":\"7020424345\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managesupplier",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managesupplier"
					]
				}
			},
			"response": []
		},
		{
			"name": "managestore-delete",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"id\":\"2\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managestore",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managestore"
					]
				}
			},
			"response": []
		},
		{
			"name": "managesupplier-delete",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"id\":\"2\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/managesupplier",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"managesupplier"
					]
				}
			},
			"response": []
		},
		{
			"name": "manageitem-delete",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"id\":\"2\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/api/manageitem",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"api",
						"manageitem"
					]
				}
			},
			"response": []
		}
	]
}
