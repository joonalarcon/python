

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def inicio():
    return 'Hola mundo'


