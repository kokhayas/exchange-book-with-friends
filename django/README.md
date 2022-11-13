# exchange-books-with-friends API

## Directory Structure
```
.
├── README.md
├── example                 (example app)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations          (auto-generated)
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py               (main CLI)
├── exchange-books-with-friends  (main project)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         (global settings)
│   ├── urls.py             (global routes config)
│   └── wsgi.py
└── requirements.txt
```

## Example App
An example app is configured in `example/` directory.

### Usage
After starting the backend development environment, you have to apply DB migrations by running `python manage.py migrate` inside the `django` container (by using e.g., the integrated shell in VSCode Dev Containers).
Then, you can visit `http://localhost:8000/example/product/` for the browser interface.

To work with the API using `curl`, try the following commands in the shell:
- GET /example/product/
    - `curl -X GET http://localhost:8000/example/product/`
        - This should return all the products in DB
- POST /example/product/
    - `curl -X POST http://localhost:8000/example/product/ -d "title=example product" -d "price=1000" -d "description=example product" -d "summary=example product"`
        - This should create a new product in Product table and returns the created product
