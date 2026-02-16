from fastapi import FastAPI, Depends
import httpx

import requests

API_KEY = "d374be66d36d4638999208f80619a97f" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS

app = FastAPI() # Initialize the end point

@app.get("/lines")
def get_route_lines():
    lines_list = list()
    response = requests.get(ENDPOINT_URL + f"/lines?&api_key={API_KEY}")  # Send a request to the endpoint
    # Convert the response to json and extract the data key
    lines = response.json()["data"]
    for route in lines:
        # Loop through all lines extracting relevant information
        lines_list.append({
            "id": route["id"],
            "text_color": route["attributes"]["text_color"],
            "short_name": route["attributes"]["short_name"],
            "long_name": route["attributes"]["long_name"],
            "color": route["attributes"]["color"],
        })
    # Return the lines_list in JSON format
    return {"lines": lines_list}


@app.get("/lines/{line_id}")
def get_line_id(line_id: str):
    response = requests.get(ENDPOINT_URL + f"/lines/{line_id}?api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    line_data = response.json()["data"]
    # Extract the relevant data
    line = {
        "id": line_data["id"],
        "text_color": line_data["attributes"]["text_color"],
        "short_name": line_data["attributes"]["short_name"],
        "long_name": line_data["attributes"]["long_name"],
        "color": line_data["attributes"]["color"],
    }
    # Return the data to the user
    return {"lines": line}