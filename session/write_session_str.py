import json
import os
from typing import Any, Dict


async def write_session_str(session_data: Dict[str, Any]) -> None:
    """
    Запись в файл sessions.json строки сессии.
    """
    try:
        existing_sessions = {}
        if os.path.exists("sessions.json"):
            with open("sessions.json", "r") as f:
                existing_sessions = json.load(f)

        existing_sessions.update(session_data)

        with open("sessions.json", "w") as f:
            json.dump(existing_sessions, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
