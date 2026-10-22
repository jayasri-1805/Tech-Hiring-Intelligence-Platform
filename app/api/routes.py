from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    PredictionRequest,
    PredictionResponse,
)
from app.core.model_loader import ModelLoader
from app.services.prediction_service import PredictionService

router = APIRouter(tags=["Prediction"])

# Load model once during startup
loader = ModelLoader()
model = loader.load()


@router.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict Salary",
)
def predict(request: PredictionRequest):

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded.",
        )

    try:
        service = PredictionService(model)

        prediction = service.predict(
            request.model_dump()
        )

        return PredictionResponse(
            predicted_salary=round(
                float(prediction[0]),
                2,
            )
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get(
    "/health",
    summary="Health Check",
)
def health():

    return {
        "status": "healthy",
        "model_loaded": model is not None,
    }