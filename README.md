# Black-Scholes Option Pricing API

This project is a simple Python API that calculates European option prices using the Black-Scholes formula.  
It uses FastAPI and runs inside a Docker container using Docker Compose.

---

## What it does

- Provides a REST API endpoint at `/price`
- Accepts JSON input:
  - Spot price (`S`)
  - Strike price (`K`)
  - Time to maturity (`T`) — in years
  - Risk-free rate (`r`)
  - Volatility (`sigma`)
  - Option type (`call` or `put`)
- Returns the calculated option price as JSON.

---

## Project files

- `app.py` — the FastAPI application
- `requirements.txt` — Python dependencies
- `Dockerfile` — instructions for building the container
- `docker-compose.yml` — runs the container easily
- `README.md` — this file

---

## How to run it locally

1. Make sure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.

2. Open a terminal in this project folder.

3. Build and start the API with Docker Compose:

   ```bash
   docker-compose up --build

4. Visit http://localhost:8000 to see the FastAPI docs.


## Example API request
POST to /price with JSON like:


{
  "S": 100,
  "K": 110,
  "T": 0.5,
  "r": 0.02,
  "sigma": 0.3,
  "option_type": "call"
}

Example curl command:


curl -X POST "http://localhost:8000/price" \
  -H "Content-Type: application/json" \
  -d '{"S": 100, "K": 110, "T": 0.5, "r": 0.02, "sigma": 0.3, "option_type": "call"}'


## Stop the server
To stop the API, press CTRL + C and run:

docker-compose down

## About the Black-Scholes model
The Black-Scholes formula calculates the fair price for a European call or put option based on:

The current price of the asset (S)

The strike price (K)

Time to maturity (T)

The risk-free interest rate (r)

The asset’s volatility (sigma)

## Purpose

This project is for learning and demonstrating how to:
- Implement a classic financial formula in Python.
- Use Python’s math and numerical libraries for quantitative calculations.
- Use Fast API and a Docker container