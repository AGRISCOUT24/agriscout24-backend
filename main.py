from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/analyse")
async def analyse_field(
    name: str = Form(None),
    location: str = Form(...),
    crop_type: str = Form(...),
    custom_crop: str = Form(None),
    area_ha: float = Form(...)
):
    kultur = custom_crop if custom_crop else crop_type
    return {
        "status": "ok",
        "message": f"Analyse empfangen für {name or 'unbekannt'} – Kultur: {kultur}, Fläche: {area_ha} ha, Standort: {location}"
    }