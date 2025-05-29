import joblib
import numpy as np

# Load model
model = joblib.load("data/random_forest_model.pkl")

def predict_points(is_home_game: bool, rolling_pts_5: float):
    X = np.array([[int(is_home_game), rolling_pts_5]])
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0] if hasattr(model, "predict_proba") else None

    confidence = abs(pred - rolling_pts_5) / rolling_pts_5
    bet = "OVER" if pred > rolling_pts_5 else "UNDER"

    return {
        "predicted_pts": round(pred, 2),
        "fake_line": round(rolling_pts_5, 2),
        "bet": bet,
        "confidence": round(confidence, 2)
    }
