"""
Local SQLite database for storing fitness plans. No server required—everything lives in a single file.
"""

import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# Database file next to this module
DB_PATH = Path(__file__).resolve().parent / "wellness.db"


def get_connection():
    """Return a connection to the local SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # access columns by name
    return conn


def init_db():
    """Create the fitness_plans table if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS fitness_plan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profile TEXT NOT NULL,
                plan_text TEXT NOT NULL,
                created_at TEXT NOT NULL,
                source TEXT DEFAULT 'agent',
                day_of_the_week TEXT NOT NULL

            )
        """)
        conn.commit()


def save_plan(profile: str, plan_text: str, day: str = "", source: str = "agent") -> int:
    """
    Store a fitness plan and return its id.
    profile: e.g. "60yo_woman" or user identifier
    plan_text: the full plan content (markdown or plain text)
    source: optional label, e.g. "agent", "chat", "batch"
    """
    init_db()
    created_at = datetime.now(timezone.utc).isoformat()
    with get_connection() as conn:
        cur = conn.execute(
            "INSERT INTO fitness_plan (profile, plan_text, created_at, source, day_of_the_week) VALUES (?, ?, ?, ?, ?)",
            (profile, plan_text, created_at, source, day),
        )
        conn.commit()
        return cur.lastrowid


def _today_weekday() -> str:
    """Return today's day of the week (e.g. 'Monday'). Uses local time."""
    return datetime.now().strftime("%A")


def get_plans(profile: str, day: Optional[str] = None) -> str:
    """
    Fetch plans for the given profile.
    If day is provided, returns the plan for that specific day (newest if multiple).
    If day is None, defaults to today's weekday.
    Returns the plan_text string, or "" if no plan found.
    """
    init_db()
    if day is None:
        day = _today_weekday()
    with get_connection() as conn:
        row = conn.execute(
            "SELECT plan_text FROM fitness_plan WHERE profile = ? AND day_of_the_week = ? ORDER BY created_at DESC LIMIT 1",
            (profile, day),
        ).fetchone()
        return row[0] if row else ""
