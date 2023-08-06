import requests
from parse_schema import Schema
from chrome_boss.element import Finder


class TreeChangedException(Exception):
    pass


class Cacher:

    def _update_elements(self, xpath, result):
        elements = self.html.xpath(xpath)
        parents = [elem.getparent() for elem in elements]
        if len(parents) > 1:
            if len(parents) == len(result):
                [elem.getparent().remove(elem) for elem in elements]
                [parent.insert(0, elem.html) for elem, parent in list(zip(result, parents))]
            else:
                TreeChangedException(f"Parents count changed from {len(parents)} to {len(result)}")
        else:
            print('one parent')

    def _update_element(self, xpath, result):
        if len(xpath._parts) == 1:
            self.html = result.html
        else:
            print('change tree')


class ChromeTab(Finder, Cacher):
    def __init__(self, srv_addr, tab_id, url, title, session):
        self.srv_addr = srv_addr
        self.tab_id = tab_id
        self.url = url
        self.title = title
        self.session = session
        self.html = None

    def get(self, url):
        resp = requests.post(f"{self.srv_addr}/tab/get", json={
            "session": self.session,
            "tab": self.tab_id,
            "url": url
        })
        if resp.status_code == 200:
            data = resp.json()
            self.url = url
            self.title = data.get('title')
        else:
            raise ValueError(f"status code: {resp.status_code}")

    def find_element(self, xpath, remote=True):
        result = super().find_element(xpath, remote=remote)
        if remote and isinstance(xpath, Schema):
            self._update_element(xpath, result)
        return result

    def find_elements(self, xpath, remote=True):
        result = super().find_elements(xpath, remote=remote)
        if remote and isinstance(xpath, Schema):
            self._update_elements(xpath, result)
        return result

    @property
    def screenshot(self):
        resp = requests.post(f"{self.srv_addr}/tab/screenshot", json={
            "session": self.session,
            "tab": self.tab_id,
        })
        data = resp.json()
        assert self.session == data.get('session')
        assert self.url == data.get('url')
        assert self.title == data.get('title')
        assert self.tab_id == data.get('tab')
        return data.get('screenshot')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<Tab: {self.title}>"
