from fastapi import FastApi

app = FastApi()

@app.get("/")
def dummy_get():
    return {'message': "Hello from docker build "}