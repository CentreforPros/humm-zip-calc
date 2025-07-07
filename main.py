# main.py

from fastapi import FastAPI
from calculator import calculate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "HUMM vs ZIP Calculator API is running"}

@app.get("/calculate")
def calculate_loan(provider: str, loan_amount: float, fortnights: int):
    result = calculate(provider, loan_amount, fortnights)
    return result
