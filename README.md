# Chatbot-API-Checking

A FastAPI-based chatbot application that uses Google's Generative AI (Gemini 1.5 Flash) to check current api is working or not.

## Project Structure

```
Chatbot-API-Checking/
├── Chatbot-Api-M1/
│   └── Chatbot-Api-Project/
│       ├── main.py              # FastAPI backend application
│       ├── test_api.py          # API testing script
│       ├── requirements.txt     # Python dependencies
│       ├── static/
│       │   ├── index.html       # Frontend HTML
│       │   ├── script.js        # Frontend JavaScript
│       │   └── style.css        # Frontend styling
│       └── README.md            # Project-specific README
├── .gitignore                   # Git ignore file
├── LICENSE                      # License file
└── README.md                    # This file
```

## Features

- RESTful API endpoint for asking questions
- Web-based chat interface
- Integration with Google Gemini 1.5 Flash AI model
- CORS support for cross-origin requests
- Real-time chat responses

## Prerequisites

- Python 3.7 or higher
- Google API Key (from Google AI Studio)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Chatbot-API-Checking/Chatbot-Api-M1/Chatbot-Api-Project
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the `Chatbot-Api-Project` directory:
```
GOOGLE_API_KEY=your_google_api_key_here
```

To get a Google API Key:
- Visit https://makersuite.google.com/app/apikey
- Create a new API key
- Add it to your `.env` file

## Usage

### Running the API Server

Navigate to the project directory and run:
```bash
python main.py
```

The server will start on `http://0.0.0.0:8000`

### Testing the API

Run the test script to verify your API connection:
```bash
python test_api.py
```

### Using the Web Interface

1. Open `static/index.html` in your web browser
2. Type your question in the input field
3. Click "Send" or press Enter
4. The AI response will appear in the chat

### API Endpoints

- `GET /` - Returns API status message
- `POST /ask` - Accepts a JSON payload with a "question" field and returns the AI response

Example API call:
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the capital of France?"}'
```

## Security Notes

- The API key is loaded from environment variables using `python-dotenv`
- Never commit the `.env` file to version control
- The `.env` file should be added to `.gitignore` (already included)
- CORS is currently set to allow all origins - restrict this in production

**Recommendations**:
- Ensure the `.env` file is never committed to version control
- Restrict CORS origins to specific domains in production
- Consider adding rate limiting to prevent API abuse
- Use environment-specific configurations for development and production

## Dependencies

- fastapi - Web framework for building APIs
- uvicorn - ASGI server
- google-generativeai - Google's Generative AI SDK
- python-dotenv - Environment variable management

## License

See LICENSE file for details.
