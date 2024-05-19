from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import quote
from deta import Deta
from send_email import send_email
from token_manager import Token

deta = Deta()
tokens_db = deta.Base("tokens")


class Data(BaseModel):
    email: str
    callback_url: str


app = FastAPI()


@app.get("/api/email-confirmation/{token}")
def check_token(token: str):
    try:
        response = tokens_db.get(token)
        print(response)
        return {"token": response["key"], "email": response["email"]}
    except Exception as err:
        print(err)
        return None


@app.post("/api/email-confirmation")
def create_token(data: Data):
    from email_content import email_content
    token_obj = Token(size=60)
    token = token_obj.generate()
    email = data.email

    print(data)

    content = email_content(token, url=data.callback_url)

    try:
        send_email(email, content["subject"], content["body"])
        response = tokens_db.put({"key": token, "email": email}, expire_in=3600)
        return {
            "success": True,
            "data": response
        }
    except Exception as err:
        print(err)
        return {"success": False}


@app.delete("/api/email-confirmation/{token}")
def delete_token(token: str):
    try:
        tokens_db.delete(key=token)
        return {"success": True}
    except Exception as err:
        print(err)
        return {"success": False}
