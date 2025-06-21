Simple CRM Project App

A lightweight CRM + Project management tool for cabinet businesses.

## Features
- Capture CRM leads
- Create quotes and BOMs
- Convert CRM to Projects
- Track costs, materials, and profits
- Simple dashboard + AI assistant integration (via OpenAI API)

## Structure

simple-crm-app/
├── backend/ # FastAPI backend
├── frontend/ # HTML + JS + Tailwind frontend

python
Copy
Edit

---

### 🟩 2. Create `backend/app.py`

**Path**: `backend/app.py`  
**Contents**:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Backend running"}

@app.get("/api/leads")
def get_leads():
    return [{"id": 1, "name": "Client A", "status": "New"}]

@app.post("/api/leads")
def add_lead(lead: dict):
    return {"msg": "Lead received", "lead": lead}
