from fastapi import Depends, FastAPI,HTTPException,status
from sqlalchemy import Select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.schemas import ticketCreate,ticketRead
from app.models import ticket_db
from app.database import engine, get_db
from pydantic import Base

Base.metadata.create_all(Bind=engine)
app = FastAPI(title="Maintenence Log")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/api/ticket", response_model=ticketCreate,status_code= status.HTTP_201_Created)
def add_ticket(new_ticket:ticketCreate,
               db : Session= Depends(get_db)):
    db:ticket_db= ticket_db 
    db(**new_ticket.model_dump())
    db.add(new_ticket)
    try:
        db.comit()
        db.refresh(new_ticket)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="This Ticket Already exists")
    return new_ticket


@app.get("/tickets",response_model=list[ticketRead])
def get_tickets(db: Session= Depends(get_db)):
    stmt = Select(ticket_db).order_by(ticket_db.id)
    return db.execute(stmt).scalar().all() 

@app.get("api/ticket/{ticket_id}",response_model=ticketRead)
def get_ticket(ticket_id: int ,db: Session= Depends(get_db)):
    ticket