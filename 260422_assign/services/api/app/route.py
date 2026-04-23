from fastapi import APIRouter, HTTPException
from .schemas import BreastCancerInput
from .model import model, scaler

router = APIRouter(tags=["prediction"])

# 상태 확인 엔드포인트
@router.get("/")
def index():
    return {"status": "ok", "message": "Breast Cancer prediction API"}

# 예측 엔드포인트
@router.post("/predict")
async def predict(req: BreastCancerInput):
    try:
        # Pydantic 모델에서 값들을 순서대로 추출하여 리스트로 변환
        features = list(req.dict().values())
        
        # 2차원 배열 형태로 변환 후 스케일링 및 예측
        arr = scaler.transform([features])
        pred = model.predict(arr)
        
        result = "악성" if int(pred[0]) == 0 else "양성"
        return {"prediction": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"prediction failed: {e}")

