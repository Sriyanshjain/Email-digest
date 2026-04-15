from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from auth import get_google_auth_url, exchange_code_for_tokens
from gmail import fetch_emails

app = FastAPI()


@app.get("/auth/login")
def login():
    url = get_google_auth_url()
    return RedirectResponse(url=url)


@app.get("/auth/callback")
def auth_callback(code: str):
    tokens = exchange_code_for_tokens(code)
    access_token = tokens['access_token']
    emails = fetch_emails(access_token)
    return emails
