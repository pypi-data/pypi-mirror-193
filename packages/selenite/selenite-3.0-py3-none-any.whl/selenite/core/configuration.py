from dataclasses import dataclass
from typing import Union, Callable

from selenium.webdriver.remote.webdriver import WebDriver


@dataclass
class Config:

    driver: Union[WebDriver, Callable[[], WebDriver]] = ...

    timeout: float = 10

    base_url: str = ''
