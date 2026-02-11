from fastapi import FastAPI
from app.routes import payslip, ai


app = FastAPI(title="PayGyaan API")


app.include_router(payslip.router)
app.include_router(ai.router)


@app.get("/")
def home():
return {"status": "PayGyaan backend running"}
