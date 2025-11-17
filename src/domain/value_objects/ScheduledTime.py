from datetime import datetime

class ScheduledTime:
    def __init__(self, datetime_str: str):
        # Parse string → datetime object
        try:
            self.datetime = datetime.fromisoformat(datetime_str)
        except Exception:
            raise ValueError("Invalid datetime format. Use ISO format: YYYY-MM-DDTHH:MM:SS")
