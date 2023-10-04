from fastapi import HTTPException, APIRouter
from api.shema.sh import SendMessageRequest
from pkg.mail.mail import SendSender

router = APIRouter()


@router.post("/send_email")
async def send_email(message_input: SendMessageRequest):
    try:
        email_sender = SendSender()
        await email_sender.send_message(
            message_input.to,
            message_input.subject,
            message_input.message
        )
        return {"OK": "Send message"}

    except Exception:
        raise HTTPException(status_code=500, detail="Error send message")