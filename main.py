from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import ee
import os
import json

# Authentifizierung mit dem Dienstkonto
service_account = 'DEIN-DIENSTKONTO-NAME@DEIN-PROJEKT-ID.iam.gserviceaccount.com'
key_path = 'DEIN_KEYDATEINAME.json'  # Die .json-Datei aus Schritt 3 (muss im Projektverzeichnis liegen)

credentials = ee.ServiceAccountCredentials(service_account, key_path)
ee.Initialize(credentials)

app = FastAPI()

@app.post("/api/analyse")
async def analyse_anfrage(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    location: str = Form(...),
    area_ha: float = Form(...),
    company: str = Form(...),
    crop_type: str = Form(...),
    notes: str = Form("")
):
    # Beispiel: NDVI-Analyse auf einem vordefinierten Polygon (dieses Beispiel ersetzt später echte Koordinaten)
    try:
        point = ee.Geometry.Point([8.07, 49.26])  # Beispiel-Koordinaten für Heidelberg
        image = ee.ImageCollection("COPERNICUS/S2") \
            .filterBounds(point) \
            .filterDate("2023-06-01", "2023-06-30") \
            .median()
        ndvi = image.normalizedDifference(["B8", "B4"])
        ndvi_value = ndvi.reduceRegion(reducer=ee.Reducer.mean(), geometry=point, scale=10).getInfo()

        return JSONResponse(content={
            "status": "ok",
            "message": f"Analyse empfangen für {name} – Kultur: {crop_type}, Fläche: {area_ha} ha, Standort: {location}",
            "ndvi": ndvi_value
        })
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)})
