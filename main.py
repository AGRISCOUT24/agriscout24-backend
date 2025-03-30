from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse
import datetime
import os

app = FastAPI()

@app.post("/api/admin-analyse")
async def admin_analyse(
    map_link: str = Form(...),
    kulturart: str = Form(None),
    flaechengroesse: str = Form(None)
):
    # 📍 Schritt 1: Extrahiere Daten aus Link (vereinfachte Demo)
    if "goo.gl" in map_link:
        parsed_info = "Koordinaten aus gekürztem Link werden extrahiert..."
    else:
        parsed_info = f"Manuelle Koordinaten oder Adresse: {map_link}"

    # 📄 Schritt 2: Dummy-PDF erzeugen
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    pdf_filename = f"analysis-report-{timestamp}.pdf"
    pdf_path = f"/tmp/{pdf_filename}"

    with open(pdf_path, "w") as f:
        f.write("AGRISCOUT24 – Analysebericht\n")
        f.write("============================\n\n")
        f.write(f"🔗 Link / Adresse: {map_link}\n")
        f.write(f"🌱 Kulturart: {kulturart}\n")
        f.write(f"📐 Fläche (ha): {flaechengroesse}\n\n")
        f.write(f"🛰️ Analyse: {parsed_info}\n")
        f.write("NDVI-Analyse & Bodenfeuchte folgen in Echtbetrieb...\n")

    # 📎 Schritt 3: Rückgabe als PDF-Link
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, filename=pdf_filename, media_type='application/pdf')
    else:
        return JSONResponse(status_code=500, content={"error": "PDF konnte nicht erstellt werden."})
