# InTurn.AI — Smart Internship Assistant

An AI-powered internship tracking assistant for university students.  
Includes three tools: **InternTrack** (hours tracking), **MentorBridge** (workplace communication), and **Report Writer** (professional activity reports).

## Tech Stack

| Layer    | Technology                        |
|----------|-----------------------------------|
| Frontend | Streamlit                         |
| Backend  | FastAPI + Uvicorn                 |
| Database | MongoDB (local or Atlas)          |
| AI       | OpenAI GPT-4o-mini                |

---

## Prerequisites

- Python 3.11+
- MongoDB running locally on `localhost:27017` **or** a MongoDB Atlas cluster
- An OpenAI API key

---

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd AI-Chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit fastapi uvicorn pymongo python-dotenv openai holidays requests
```

> All packages with pinned versions:
> ```
> streamlit==1.55.0
> fastapi==0.135.1
> uvicorn==0.41.0
> pymongo==4.16.0
> python-dotenv==1.2.2
> openai==2.28.0
> holidays==0.92
> requests==2.32.5
> ```

### 4. Create the `.env` file

Create a `.env` file in the **project root** (same level as this README):

```
MONGO_URI=mongodb://localhost:27017
OPENAI_API_KEY=your_openai_api_key_here
```

> If using MongoDB Atlas, replace `MONGO_URI` with your Atlas connection string:
> ```
> MONGO_URI=mongodb+srv://USERNAME:PASSWORD@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
> ```

---

## Running the App

You need **two terminals** running at the same time.

### Terminal 1 — Start the backend

```bash
cd backend
uvicorn main:app --reload --port 8001
```

Backend runs at: `http://localhost:8001`  
API docs available at: `http://localhost:8001/docs`

### Terminal 2 — Start the frontend

```bash
cd frontend
streamlit run app.py
```

Frontend runs at: `http://localhost:8501`

---

## MongoDB Collections

The app uses a database named `interntrack` with these collections:

| Collection | Purpose                              |
|------------|--------------------------------------|
| `hours`    | Logged internship hours              |
| `tasks`    | Task entries                         |
| `chat`     | All chat messages (all three tools)  |
| `config`   | Saved InternTrack configuration      |
| `reports`  | Generated Report Writer reports      |

---

## Project Structure

```
AI-Chatbot/
├── backend/
│   ├── main.py          # FastAPI app and routes
│   ├── ai_router.py     # AI prompt routing (InternTrack / MentorBridge / Report Writer)
│   ├── database.py      # MongoDB connection and collections
│   └── tracker.py       # Hours logging logic
├── frontend/
│   ├── app.py           # Streamlit UI
│   └── styles.py        # CSS styles
├── .env                 # API keys (never commit this)
├── .gitignore
└── README.md
```

