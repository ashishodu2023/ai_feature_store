from fastapi import FastAPI
from app.storage import store_features
from pydantic import BaseModel
from app.ranking import generate_ranking

app = FastAPI()

@app.get("/get-features/")
def get_features():
    # Example feature response
    return {"features": ["sepal_length", "petal_length"]}

# Define schema for incoming request data
class FeatureRequest(BaseModel):
    features: dict  # Expected: {"Feature Name": Importance Score}

@app.post("/store-features/")
def store_features_endpoint(request: FeatureRequest):
    # Store features in Bigtable
    store_features("iris_features", pd.DataFrame(request.features.items(), columns=["Feature", "Importance"]))
    return {"status": "success", "message": "Features stored successfully"}

