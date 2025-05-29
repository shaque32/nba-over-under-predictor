from pydantic import BaseModel

class PredictionRequest(BaseModel):
    is_home_game: bool
    rolling_pts_5: float

class PredictionResponse(BaseModel):
    predicted_pts: float
    fake_line: float
    bet: str
    confidence: float
