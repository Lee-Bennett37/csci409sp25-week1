from fastapi import FastAPI, Depends
import httpx

import requests

API_KEY = "d374be66d36d4638999208f80619a97f" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS

app = FastAPI() # Initialize the end point

@app.get("/")
def read_root():
    return {"Root Testing"}

# Get a list of all routes
@app.get("/routes")
def get_routes():
    routes_list = list()
    response = requests.get(ENDPOINT_URL+f"/routes?&api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    routes = response.json()["data"]
    for route in routes:
        # Loop through all routes extracting relevant information
        routes_list.append({
            "id": route["id"],
            "type": route["type"],
            "color": route["attributes"]["color"],
            "text_color": route["attributes"]["text_color"],
            "description": route["attributes"]["description"],
            "long_name": route["attributes"]["long_name"],
            "type": route["attributes"]["type"],
        })
    # Return the routes_list in JSON format
    return {"routes": routes_list}

# Get information on a specific route
@app.get("/routes/{route_id}")
def get_route(route_id: str):
    response = requests.get(ENDPOINT_URL + f"/routes/{route_id}?api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    route_data = response.json()["data"]
    # Extract the relevant data
    route = {
        "id": route_data["id"],
        "type": route_data["type"],
        "color": route_data["attributes"]["color"],
        "text_color": route_data["attributes"]["text_color"],
        "description": route_data["attributes"]["description"],
        "long_name": route_data["attributes"]["long_name"],
        "type": route_data["attributes"]["type"],
    }
    # Return the data to the user
    return {"routes": route}