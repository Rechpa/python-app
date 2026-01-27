from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import os

app = FastAPI(title="Notes API")

DATA_FILE = "notes.json"


# ---------- Helpers ----------

def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(DATA_FILE, "w") as f:
        json.dump(notes, f, indent=2)


# ---------- Models ----------

class NoteCreate(BaseModel):
    title: str
    content: str
    tags: List[str] = []


class Note(NoteCreate):
    id: int
    created_at: str


# ---------- Endpoints ----------

@app.get("/notes", response_model=List[Note])
def get_notes():
    return load_notes()


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate):
    notes = load_notes()
    new_note = {
        "id": len(notes) + 1,
        "title": note.title,
        "content": note.content,
        "tags": note.tags,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    notes.append(new_note)
    save_notes(notes)
    return new_note


@app.get("/search", response_model=List[Note])
def search_notes(q: str):
    notes = load_notes()
    q = q.lower()

    results = [
        n for n in notes
        if q in n["title"].lower()
        or q in n["content"].lower()
        or q in [t.lower() for t in n["tags"]]
    ]

    return results


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    notes = load_notes()
    filtered_notes = [n for n in notes if n["id"] != note_id]

    if len(filtered_notes) == len(notes):
        raise HTTPException(status_code=404, detail="Note not found")

    save_notes(filtered_notes)
    return {"message": "Note deleted"}
