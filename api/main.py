from fastapi import FastAPI
from models import models
from controllers import controller
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dbconnection import engine
from starlette.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(controller.router)

@app.get("/")
def raiz():
  return RedirectResponse(url="/docs")

if __name__ == '__main__':
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
