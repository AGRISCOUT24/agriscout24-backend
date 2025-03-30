from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import datetime
import os

app = FastAPI()

class AnalyseInput(BaseModel):
    earth_link: str
    culture: str = None
    area: str = None

@app.post("/api/admin-analyse")
async def admin_analyse(data: AnalyseInput):
    if "goo.gl" in data.earth_link:
        parsed_info = "Koordinaten aus gekürztem Link werden extrahiert..."
    else:
        parsed_info = f"Manuelle Koordinaten oder Adresse: {data.earth_link}"

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    pdf_filename = f"analysis-report-{timestamp}.pdf"
    pdf_path = f"/tmp/{pdf_filename}"

    with open(pdf_path, "w") as f:
        f.write("AGRISCOUT24 – Analysebericht\n")
        f.write("============================\n\n")
        f.write(f"🔗 Link / Adresse: {data.earth_link}\n")
        f.write(f"🌱 Kulturart: {data.culture}\n")
        f.write(f"📐 Fläche (ha): {data.area}\n\n")
        f.write(f"🛰️ Analyse: {parsed_info}\n")
        f.write("NDVI-Analyse & Bodenfeuchte folgen in Echtbetrieb...\n")

    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, filename=pdf_filename, media_type='application/pdf')
    else:
        return JSONResponse(status_code=500, content={"error": "PDF konnte nicht erstellt werden."})
