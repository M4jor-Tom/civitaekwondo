from fastapi import FastAPI
from core.rest import mail_router

app = FastAPI()
app.include_router(mail_router)
