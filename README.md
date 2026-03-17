# InTurn.AI — Smart Internship Assistant

An AI-powered internship tracking assistant for university students.  
Includes three tools: **InternTrack** (hours tracking), **MentorBridge** (workplace communication), and **Report Writer** (professional activity reports).

## Latest Updates

- InternTrack now supports signed hour updates from chat input:
	- `+8`, `+ 8 hours`, `-2`, `- 2 hrs`
- Hour updates are saved to backend config automatically.
- `Days Left` is calculated using your configured **Daily Hours**.
- Added AI disclaimer blocks in all AI sections.
- Chat UI now uses Messenger-style alignment:
	- User messages on the right (orange avatar)
	- Assistant messages on the left (red avatar)
	- Bubble width auto-adjusts based on content.

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
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 4. Create the `.env` file

Create a `.env` file in the **project root** (same level as this README):

```
MONGO_URI=mongodb://localhost:27017
OPENAI_API_KEY=your_openai_api_key_here
API_BASE_URL=http://localhost:8001
```

`API_BASE_URL` is optional and defaults to `http://localhost:8001`.

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

## InternTrack Input Behavior

InternTrack accepts quick chat commands for hours updates.

- Add hours: `+8 today`
- Subtract hours: `-2 correction`

Rules:

- Hours are clamped between `0` and `Total Required Hours`.
- `Days Left` updates using `ceil(remaining / daily_hours)`.
- `Daily Hours` comes from the Configuration panel.

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

