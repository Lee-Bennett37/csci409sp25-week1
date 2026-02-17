from fastapi import FastAPI, Depends
import httpx

import requests

API_KEY = "d374be66d36d4638999208f80619a97f" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS

# Dependency to fetch all vehicles
async def get_all_vehicles():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

# Dependency to fetch a specific vehicle by ID
async def get_vehicle_by_id(vehicle_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles/{vehicle_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

app = FastAPI() # Initialize the end point

@app.get("/")
def read_root():
    return {"Root Testing"}

@app.get("/vehicles")
async def read_vehicles(vehicles=Depends(get_all_vehicles)):
    return vehicles

@app.get("/vehicles/{vehicle_id}")
async def read_vehicle(vehicle_id: str, vehicle=Depends(get_vehicle_by_id)):
    return vehicle