from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, Any
import datetime

app = FastAPI()

class WebhookPayload(BaseModel):
    formName: Optional[str]
    submissionTime: Optional[str]
    submissionId: Optional[str]
    contactId: Optional[str]
    formType: Optional[str]
    formId: Optional[str]
    
    # Formularfelder
    field_address_1: Optional[str]
    field_paragraph_2: Optional[str]
    field_firstName_1: Optional[str]
    field_text_1: Optional[str]
    field_paragraph_1: Optional[str]
    field_email_1: Optional[str]
    field_paragraph_3: Optional[str]
    field_phone_1: Optional[str]
    
    # Kontaktinfos
    contact_name_last: Optional[str]
    contact_name_first: Optional[str]
    contact_email: Optional[str]
    contact_locale: Optional[str]
    contact_company: Optional[str]
    contact_birthdate: Optional[str]
    contact_labelKeys_items_0: Optional[str]
    contact_contactId: Optional[str]
    contact_address_city: Optional[str]
    contact_address_addressLine: Optional[str]
    contact_address_formattedAddress: Optional[str]
    contact_address_country: Optional[str]
    contact_address_postalCode: Optional[str]
    contact_address_addressLine2: Optional[str]
    contact_address_subdivision: Optional[str]
    contact_jobTitle: Optional[str]
    contact_imageUrl: Optional[str]
    contact_updatedDate: Optional[str]
    contact_phone: Optional[str]
    contact_createdDate: Optional[str]


@app.post("/api/webhook")
async def receive_webhook(payload: WebhookPayload):
    # 🧠 Hier kannst du Logik einbauen: speichern, analysieren, weiterleiten etc.
    print(f"✅ Neue Analyseanfrage empfangen für: {payload.field_firstName_1}")
    
    return {
        "status": "ok",
        "message": f"Analyse für {payload.field_firstName_1} empfangen!",
        "timestamp": datetime.datetime.now().isoformat()
    }
