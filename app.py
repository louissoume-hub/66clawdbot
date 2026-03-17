import os
from flask import Flask
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Configuration de Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return "L'agent Pharm'O est opérationnel et en ligne !"

if __name__ == "__main__":
    # Render définit automatiquement un port via une variable d'environnement
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
