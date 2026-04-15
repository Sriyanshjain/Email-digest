# Email Digest

An AI-powered email assistant that summarizes your daily emails and tells you which ones need your attention.

## What it does

- Connects to your Gmail account via OAuth
- Fetches your recent emails
- Uses AI to classify each email (urgent / needs reply / informational / promotional)
- Generates a daily summary sent to your inbox
- Tells you which emails need a reply and by when

## Tech Stack

- **Backend:** Python, FastAPI
- **AI:** Azure OpenAI
- **Email:** Gmail API
- **Database:** PostgreSQL (coming soon)

## Project Structure

```
email-digest/
├── backend/
│   ├── main.py          # FastAPI routes
│   ├── auth.py          # Google OAuth logic
│   ├── gmail.py         # Gmail API interactions
│   ├── ai.py            # AI summarization (in progress)
│   └── .env             # Environment variables
├── frontend/            # React app (coming soon)
└── README.md
```

## Setup

### Prerequisites

- Python 3.9+
- Google Cloud Console account
- Azure OpenAI access

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/email-digest.git
cd email-digest
```

### 2. Set up Google Cloud

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable Gmail API
4. Configure OAuth consent screen
5. Create OAuth 2.0 credentials (Web application)
6. Add `http://localhost:8000/auth/callback` as authorized redirect URI
7. Add yourself as a test user

### 3. Set up backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env` in the backend folder:

```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:8000/auth/callback
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

### 6. Test OAuth

1. Go to `http://localhost:8000/auth/login`
2. Login with your Google account
3. Click Allow
4. You should see your parsed emails

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/login` | GET | Redirects to Google OAuth |
| `/auth/callback` | GET | Handles OAuth callback, returns tokens and emails |

## Coming Soon

- [ ] AI classification and summarization
- [ ] Daily digest email generation
- [ ] Scheduled daily runs
- [ ] PostgreSQL for storing user tokens
- [ ] React frontend for configuration
- [ ] Support for multiple email accounts

## What I Learned Building This

- OAuth 2.0 flow (authorization code, access tokens, refresh tokens)
- Gmail API integration
- Handling different email formats (multipart, HTML, plain text)
- Base64 encoding/decoding
- FastAPI project structure

## License

MIT
