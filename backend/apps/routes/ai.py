from fastapi import APIRouter
from app.services.ai_explainer import explain

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/explain")
def explain_component(component: str, amount: int):
    return {"explanation": explain(component, amount)}