from .base import Entity


class Enrollments(Entity):
    path = "Enrollments"

    def get(self):
        params = {"parent_id": self.session.headers["X-UID"]}
        return self.session.get(self.path, params=params)
