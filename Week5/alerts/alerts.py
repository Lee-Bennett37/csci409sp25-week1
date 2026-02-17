from fastapi import FastAPI, Depends
import httpx

import requests

API_KEY = "d374be66d36d4638999208f80619a97f" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS

# Dependency to fetch all alerts
async def get_all_alerts(route: str = None, stop: str = None):
    params = {}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts", params=params)
        response.raise_for_status()
        return response.json()

# Dependency to fetch a specific alert by ID
async def get_alert_by_id(alert_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts/{alert_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

app = FastAPI()  # Initialize the end point

@app.get("/")
def read_root():
    return {"Root Testing"}

@app.get("/alerts")
async def read_alerts(route: str = None, stop: str = None, alerts=Depends(get_all_alerts)):
    return alerts

@app.get("/alerts/{alert_id}")
async def read_alert(alert_id: str, alert=Depends(get_alert_by_id)):
    return alert