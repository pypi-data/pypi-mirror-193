import uuid
import requests
from chrome_boss.tab import ChromeTab

__all__ = ['ChromeBoss']


class ChromeBoss:
    tabs = []

    def __init__(self, host='localhost', port=4444):
        self.url = f"http://{host}:{port}"
        resp = requests.post(f"{self.url}/init", json={"client_id": uuid.uuid4().hex})
        data = resp.json()
        self.session = data.get('session')
        self.tabs = [ChromeTab(
            srv_addr=self.url,
            tab_id=tab.get('id'),
            url=tab.get('url'),
            title=tab.get('title'),
            session=self.session,
        ) for tab in data.get('tabs')]
        self.session = resp.json().get('window_id')

    def tab(self, number):
        return self.tabs[number - 1]

    def destroy(self):
        print(f"Destroy {self.session}")

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.session}>"
