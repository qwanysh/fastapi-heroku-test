from os import environ

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'Hello world'


@app.get('/database')
def database():
    return environ.get('DATABASE_URL')
