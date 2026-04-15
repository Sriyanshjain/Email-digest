import httpx
from datetime import datetime, timedelta
import base64

def fetch_emails(access_token: str,max_emails: int = 10):
    headers = {"Authorization": f"Bearer {access_token}"}
    since_date = (datetime.now() - timedelta(hours=24)).strftime("%Y/%m/%d")
    response = httpx.get("https://www.googleapis.com/gmail/v1/users/me/messages", headers=headers, params={
            "q": f"after:{since_date}",
            "maxResults": 50
        })
    messages = response.json().get("messages", [])
    emails=[]
    for message in messages[:max_emails]:
        email_details = get_email_details(access_token, message['id'])
        emails.append(parse_email(email_details))
    return emails

def get_email_details(access_token: str, message_id: str):
    response=httpx.get(f"https://www.googleapis.com/gmail/v1/users/me/messages/{message_id}", headers={"Authorization": f"Bearer {access_token}"})
    return response.json()

def parse_email(email):
    email_headers = email['payload']['headers']
    subject = [h['value'] for h in email_headers if h['name'] == "Subject"]
    from_email = [h['value'] for h in email_headers if h['name'] == "From"]
    
    body = ""
    payload = email['payload']
    
    if 'parts' in payload:
        # multipart - find text/plain first, fallback to text/html
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data', '')
                if data:
                    body = base64.urlsafe_b64decode(data).decode('utf-8')
                break
        # If no text/plain found, try text/html
        if not body:
            for part in payload['parts']:
                if part['mimeType'] == 'text/html':
                    data = part['body'].get('data', '')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8')
                    break
    else:
        # No parts - body directly in payload
        data = payload['body'].get('data', '')
        if data:
            body = base64.urlsafe_b64decode(data).decode('utf-8')
    
    return {
        "subject": subject[0] if subject else "",
        "from": from_email[0] if from_email else "",
        "body": body
    }
