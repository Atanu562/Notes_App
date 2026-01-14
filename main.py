#from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient

app = FastAPI()


conn = MongoClient("mongodb+srv://atanu123:atanu_123@demoproject.jr1vvfd.mongodb.net")

