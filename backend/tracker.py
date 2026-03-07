from datetime import datetime

# store hours temporarily (later you can connect MongoDB)
hours_logged = 0


def log_hours(data):

    global hours_logged

    hours = data.get("hours", 0)
    task = data.get("task", "")

    hours_logged += hours

    return {
        "message": "Hours logged successfully",
        "task": task,
        "hours_added": hours,
        "total_hours": hours_logged
    }


def progress(total, current):

    percent = (current / total) * 100 if total else 0
    remaining = total - current

    return {
        "progress_percent": round(percent, 2),
        "remaining_hours": remaining
    }