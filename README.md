# ✨ JobMatch AI - Resume Analyzer

JobMatch AI is a premium, AI-powered Streamlit application that instantly analyzes resumes against job descriptions. It uncovers exact skill gaps, provides actionable AI-driven insights, and helps candidates dramatically boost their interview chances.

## 🚀 Features

- **Instant ATS Compatibility Score**: Get a precise match percentage between your resume and the target job description.
- **AI Gap Analysis**: Uncover exact missing keywords and technical skills.
- **Smart Formatting Feedback**: Get AI-powered suggestions to improve resume structure and impact.
- **Multi-format Support**: Upload your resume in PDF, DOC, DOCX, TXT, or Image (PNG/JPG) formats.
- **Premium UI/UX**: Enjoy a state-of-the-art interface with Dark Mode, glassmorphism, and responsive design.
- **Secure Authentication**: Built-in login and signup system for private, persistent usage.

## 🛠️ Tech Stack

- **Frontend/Backend**: [Streamlit](https://streamlit.io/) (Python)
- **AI/LLM**: [OpenRouter API](https://openrouter.ai/) (Llama 3 / DeepSeek / Mistral)
- **Document Processing**: `PyMuPDF` (PDFs), `python-docx` (Word), `pytesseract` (Images)
- **Database**: SQLite3 (`users.db`)

## 💻 Local Installation

1. **Clone the repository** (or download the files)
2. **Install the required dependencies:**
   ```bash
   pip install -r requriments.txt
   ```
3. **Set your OpenRouter API Key:**
   Open `ai_features.py` and replace the placeholder API key with your actual OpenRouter key.
4. **Run the application:**
   ```bash
   python -m streamlit run frontend.py
   ```
5. **Open your browser:**
   Navigate to `http://localhost:8501`

---

## ⚠️ Important Deployment Note (Vercel)

Vercel is optimized for static sites and serverless functions, **not for stateful WebSocket applications like Streamlit.** 

Streamlit requires a persistent WebSocket connection to function. Because Vercel Serverless Functions have a strict execution timeout (10 seconds) and do not support WebSockets, **deploying Streamlit directly to Vercel will result in connection timeouts and a broken app.**

### ✅ Recommended Deployment Platforms:
Instead of Vercel, we highly recommend deploying this app on:
1. **[Streamlit Community Cloud](https://share.streamlit.io/)** (Free, easiest, natively supports Streamlit)
2. **[Render](https://render.com/)** (Free tier available, supports persistent WebSockets)
3. **[Hugging Face Spaces](https://huggingface.co/spaces)** (Free, optimized for AI apps)
