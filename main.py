from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse

from routers import canciones

app = FastAPI(
    title="Music List",
    description="FastAPI Music Lists",
    version="0.0.1",

)


app.include_router(canciones.router, prefix="/canciones", tags=["canciones"])



@app.get("/",
         response_class=HTMLResponse,
         summary="Home")
async def root():
    """**Home page**
    FastAPI Music Lists with a nice Music
    """
    return """
    <html>
        <head>
            <title>Music List</title>
        </head>
        <body>
            <h1>FastAPI Music Lists</h1>
            <p>FastAPI is a modern, fast Music playlist (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.</p>
            <p>It is inspired by:</p>
            <ul>
                <li><a href="/canciones/">Canciones</a></li>
    </html>
    
    """


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
