from fastapi import FastAPI
from src.config.database import criar_bd

criar_bd()

app = FastAPI()