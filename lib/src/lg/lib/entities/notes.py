from datetime import datetime, timedelta

from .base import Entity


class Notes(Entity):
    path = "Notes"

    def get(self, enrollment_id):
        tomorrow = datetime.utcnow() + timedelta(days=1)
        tomorrow_str = tomorrow.strftime("%Y-%m-%d+00:00:00.000")
        params = {
            "before_time": tomorrow_str,
            "count": 30,
            "enrollment_id": enrollment_id,
            "note_category": "report",
            "video_book": "true",
        }

        return self.session.get(self.path, params=params)
