from fastapi import FastAPI, Query

from calculator import calculate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "HUMM vs ZIP Calculator API is running"}

@app.get("/calculate")
def calculate_loan(
    provider: str = Query(..., description="Provider name: HUMM or ZIP"),
    loan_amount: float = Query(..., description="Total loan amount"),
    fortnights: int = Query(..., description="Number of fortnights"),
):
    return calculate(provider, loan_amount, fortnights)