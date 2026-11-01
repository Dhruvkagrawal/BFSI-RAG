from fastapi import APIRouter, Depends
from app.schemas.health import HealthResponse
from app.core.config import Settings, get_settings

router = APIRouter(prefix="/health",tags=["health"])

@router.get("", response_model=HealthResponse)
def health_check(setting: Settings = Depends(get_settings)):
    return {"status": "ok", "app": setting.app_name}