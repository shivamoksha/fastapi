from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

# Load data from the JSON file
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)

# Create a FastAPI instance
app = FastAPI()

# Enable CORS for all origins (to allow cross-origin requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

# Convert data to a dictionary for quick lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
async def get_marks(name: list[str]):
    """
    API Endpoint: Fetch marks by names.
    Example: /api?name=X&name=Y
    """
    results = [marks_dict.get(n, "Not Found") for n in name]
    return {"marks": results}
