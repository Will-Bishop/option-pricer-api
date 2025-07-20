# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .model import black_scholes


app = FastAPI()

class OptionParams(BaseModel):
    S: float = Field(gt=0, description="Stock price")
    K: float = Field(gt=0, description="Strike price")
    T: float = Field(gt=0, description="Time to maturity")
    r: float = Field(description="Risk-free rate")
    sigma: float = Field(gt=0, description="Volatility")
    option_type: str = Field(description="Option type (call or put)")

@app.post("/price")
def price_option(params: OptionParams):
    try:
        price = black_scholes(
            params.S, params.K, params.T, params.r, params.sigma, params.option_type.lower()
        )
        return {"price": price}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))