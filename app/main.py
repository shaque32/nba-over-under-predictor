from fastapi import FastAPI
from app.schemas import PredictionRequest, PredictionResponse
from app.model import predict_points

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    result = predict_points(request.is_home_game, request.rolling_pts_5)
    return result
