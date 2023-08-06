import functools
import inspect
from typing import Callable

import requests
import urllib3
from requests import Request, RequestException
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

COMMON_HEADERS = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76',
}


class HttpRequest:

    def __init__(self, url: str, method: str = 'get') -> None:
        self.url = url
        self.method = method
        self.func_return = {}
        self.func_im_self = None

    def __call__(self, func: Callable) -> Callable:
        self.func = func
        self.is_class = False
        try:
            if inspect.getfullargspec(self.func).args[0] == 'self':
                self.is_class = True
        except IndexError:
            pass

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.func_return = self.func(*args, **kwargs) or {}
            self.func_im_self = args[0] if self.is_class else object
            url = self.create_url()
            session = self.get_session()
            req = Request(self.method, url, **session)
            prepped = req.prepare()
            try:
                res = requests.Session().send(prepped, verify=False)
                res.encoding = res.apparent_encoding
            except RequestException as e:
                raise RequestException(f'Request failed: {e}')
            else:
                return res

        return wrapper

    def create_url(self) -> str:
        base_url = getattr(self.func_im_self, 'base_url', '')
        url = self.func_return.pop('url', None) or self.url
        return ''.join([base_url, url])

    def get_session(self) -> dict:
        headers = getattr(self.func_im_self, 'header', {})
        headers.update(COMMON_HEADERS)
        json_data = self.func_return.pop('json', None)
        params = self.func_return.pop('params', None)
        data = self.func_return.pop('data', None)
        files = self.func_return.pop('files', None)
        return {
            'headers': headers,
            'json': json_data,
            'params': params,
            'data': data,
            'files': files
        }
