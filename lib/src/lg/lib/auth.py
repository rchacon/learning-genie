import requests


BASE_URL = "https://api2.learning-genie.com/api/v1"


class HttpError(Exception):
    pass


class Session:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self._headers = None
        self._http = None

    @property
    def http(self):
        if self._http is None:
            self._http = requests.Session()
            self._http.headers.update(self.headers)

        return self._http

    @property
    def headers(self):
        if self._headers is None:
            resp = requests.post(
                "{}/account/login".format(BASE_URL),
                json={
                    "email": self.email,
                    "password": self.password,
                    "from": "web",
                    "emailLoginExpireFlag": "",
                },
            )

            if resp.status_code != 200:
                raise HttpError(resp.status_code)

            body = resp.json()

            self._headers = {"X-LG-Token": body["token"], "X-UID": body["user_id"]}

        return self._headers

    def get(self, path, params):
        resp = self.http.get("{}/{}".format(BASE_URL, path), params=params)

        if resp.status_code != 200:
            raise HttpError(resp.status_code)

        return resp.json()

    def post(self, path, body):
        resp = self.http.post("{}/{}".format(BASE_URL, path), json=body)

        if resp.status_code != 200:
            raise HttpError(resp.status_code)

        return resp.json()
