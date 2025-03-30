from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import datetime
import json

app = FastAPI()

# 👇 Temporär deaktiviert, bis wir die Struktur sicher kennen
# class WebhookPayload(BaseModel):
#     formName: Optional[str]
#     submissionTime: Optional[str]
#     submissionId: Optional[str]
#     contactId: Optional[str]
#     formType: Optional[str]
#     formId: Optional[str]
#     field_address_1: Optional[str]
#     field_paragraph_2: Optional[str]
#     field_firstName_1: Optional[str]
#     field_text_1: Optional[str]
#     field_paragraph_1: Optional[str]
#     field_email_1: Optional[str]
#     field_paragraph_3: Optional[str]
#     field_phone_1: Optional[str]
#     contact_name_last: Optional[str]
#     contact_name_first: Optional[str]
#     contact_email: Optional[str]
#     contact_locale: Optional[str]
#     contact_company: Optional[str]
#     contact_birthdate: Optional[str]
#     contact_labelKeys_items_0: Optional[str]
#     contact_contactId: Optional[str]
#     contact_address_city: Optional[str]
#     contact_address_addressLine: Optional[str]
#     contact_address_formattedAddress: Optional[str]
#     contact_address_country: Optional[str]
#     contact_address_postalCode: Optional[str]
#     contact_address_addressLine2: Optional[str]
#     contact_address_subdivision: Optional[str]
#     contact_jobTitle: Optional[str]
#     contact_imageUrl: Optional[str]
#     contact_updatedDate: Optional[str]
#     contact_phone: Optional[str]
#     contact_createdDate: Optional[str]

@app.post("/api/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("🔔 Webhook empfangen:")
    print(json.dumps(data, indent=2))  # schön formatiert im Log
    return {
        "status": "received",
        "timestamp": datetime.datetime.now().isoformat()
    }
