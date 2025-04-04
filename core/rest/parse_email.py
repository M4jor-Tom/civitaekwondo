from fastapi import APIRouter, Form

from core.model import Email

mail_router: APIRouter = APIRouter()

@mail_router.post("/parse-email")
async def parse_email(
        from_address: str = Form(...),
        subject: str = Form(...),
        text_body: str = Form(...)
):
    mail: Email = Email(from_address=from_address, subject=subject, text_body=text_body)

    return {"mail": mail.model_dump()}
