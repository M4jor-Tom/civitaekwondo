from pydantic import BaseModel

class Email(BaseModel):
    from_address: str
    subject: str
    text_body: str
