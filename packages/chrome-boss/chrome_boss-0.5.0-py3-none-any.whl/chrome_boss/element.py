import requests
from lxml.etree import fromstring, XMLSyntaxError, _Element


class Finder:

    def _request(self, address, xpath):
        resp = requests.post(f"{self.srv_addr}/{address}", json={
            "session": self.session,
            "tab": self.tab_id,
            "xpath": xpath
        })
        data = resp.json()
        assert self.session == data.get('session')
        assert self.tab_id == data.get('tab')
        return data

    def _xpath_resolver(self, xpath):
        self_xpath = self.__dict__.get('xpath')
        if self_xpath:
            return f"{self_xpath}{xpath}"
        return xpath

    def find_element(self, xpath, remote=True):
        full_xpath = self._xpath_resolver(xpath)
        if remote:
            data = self._request('find_element', full_xpath)
            html = data.get('html')
        else:
            html = self.html.xpath(xpath)[0]
        assert html
        return WebElement(
            srv_addr=self.srv_addr,
            session=self.session,
            tab_id=self.tab_id,
            xpath=full_xpath,
            html=html
        )

    def find_elements(self, xpath, remote=True):
        full_xpath = self._xpath_resolver(xpath)
        if remote:
            data = self._request('find_elements', full_xpath)
            elements = data.get('elements')
        else:
            elements = self.html.xpath(xpath)
        assert type(elements) == list
        return [WebElement(
            srv_addr=self.srv_addr,
            session=self.session,
            tab_id=self.tab_id,
            xpath=full_xpath,
            html=element
        ) for element in elements]


class WebElement(Finder):
    @staticmethod
    def _parse(html):
        if type(html) == str:
            try:
                return fromstring(html)
            except XMLSyntaxError as e:
                print(e)
        elif isinstance(html, _Element):
            return html
        else:
            raise ValueError("Invalid HTML")

    def __init__(self, srv_addr, session, tab_id, xpath, html):
        self.srv_addr = srv_addr
        self.session = session
        self.tab_id = tab_id
        self.xpath = xpath
        self.html = self._parse(html)

    def get_attribute(self, attribute_name):
        return self.html.get(attribute_name)

    @property
    def text(self):
        return self.html.text

    @property
    def screenshot(self):
        resp = requests.post(f"{self.srv_addr}/tab/element/screenshot", json={
            "session": self.session,
            "tab": self.tab_id,
            "xpath": self.xpath,
        })
        data = resp.json()
        assert self.session == data.get('session')
        assert self.tab_id == data.get('tab')
        return data.get('screenshot')

    def click(self):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.html.tag}>"
