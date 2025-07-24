from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import jwt
import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

app = FastAPI()

class AuthRequest(BaseModel):
    number: int

@app.post("/authentication")
def authenticate(data: AuthRequest):
    ak = os.getenv("AK")
    sk = os.getenv("SK")
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    payload = {
        "iss": ak,
        "exp": int(time.time()) + data.number, # The valid time, in this example, represents the current time+1800s(30min)
        "nbf": int(time.time()) # The time when it starts to take effect, in this example, represents the current time minus 5s
    }
    token = jwt.encode(payload, sk, headers=headers)
    return token
#----------------
