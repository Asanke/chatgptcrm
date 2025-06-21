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
