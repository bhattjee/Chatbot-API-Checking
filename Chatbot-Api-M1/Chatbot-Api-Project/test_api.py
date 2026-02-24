import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Try the most common working model
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Hello, how are you?")
    print("Response:", response.text)
    print("Success! API is working.")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nTrying to list available models...")
    
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Available model: {m.name}")
    except Exception as list_error:
        print(f"Cannot list models: {list_error}")
        print("Please check your API key in the .env file")