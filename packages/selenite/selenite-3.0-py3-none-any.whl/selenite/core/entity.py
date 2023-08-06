import base64
import typing

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenite.common.helpers import is_absolute_url, recognize_text_in_image, by_with_args
from selenite.core.configuration import Config
from selenite.core.locator import Locator


class Element:

    def __init__(self, locator: Locator[WebElement], config: Config):
        self._locator = locator
        self._config = config

    @property
    def config(self):
        return self._config

    @property
    def timeout(self):
        return self._config.timeout

    def locate(self) -> WebElement:
        return self._locator()

    def __call__(self, *args, **kwargs) -> WebElement:
        return self.locate()

    def element(self, by: tuple, *args):
        new_by = by_with_args(by, *args)
        return Element(
            Locator(
                f'{self}.element({new_by})',
                lambda: WebDriverWait(self(), self.timeout).until(EC.presence_of_element_located(new_by))
            ),
            self.config
        )

    def elements(self, by: tuple, *args):
        new_by = by_with_args(by, *args)
        return Collection(
            Locator(
                f'{self}.elements({new_by})',
                lambda: WebDriverWait(self(), self.timeout).until(EC.presence_of_all_elements_located(new_by))
            ),
            self.config
        )

    def set_value(self, value: typing.Union[str, int]):
        web_element = self()
        web_element.send_keys(str(value))
        return self

    def clear(self):
        web_element = self()
        web_element.clear()
        return self

    def click(self):
        web_element = self()
        web_element.click()
        return self

    def double_click(self):
        actions: ActionChains = ActionChains(self.config.driver)
        web_element = self()
        actions.double_click(web_element).perform()
        return self

    def context_click(self):
        actions: ActionChains = ActionChains(self.config.driver)
        web_element = self()
        actions.context_click(web_element).perform()
        return self

    def hover(self):
        actions: ActionChains = ActionChains(self.config.driver)
        web_element = self()
        actions.move_to_element(web_element).perform()
        return self

    def recognize_text(self):
        web_element = self()
        image_bytes = base64.b64decode(web_element.screenshot_as_base64)
        return recognize_text_in_image(image_bytes)

    def is_visible(self):
        try:
            web_element = self()
            if EC.visibility_of(web_element)(self.config.driver):
                return True
            return False
        except TimeoutException:
            return False


class Collection:

    def __init__(self, locator: Locator, config: Config) -> None:
        self._locator = locator
        self._config = config

    def locate(self) -> typing.List:
        return self._locator()

    def __call__(self, *args, **kwargs) -> typing.List:
        return self.locate()

    @property
    def config(self) -> Config:
        return self._config

    def element(self, index: int) -> Element:
        def find() -> WebElement:
            web_elements = self()
            return web_elements[index]

        return Element(
            Locator(
                f'{self}[{index}]', find
            ),
            self.config
        )


class Browser:

    def __init__(self, config: Config):
        self._config = config

    @property
    def config(self) -> Config:
        return self._config

    @property
    def driver(self) -> WebDriver:
        return (
            self.config.driver()
            if callable(self.config.driver)
            else self.config.driver
        )

    @property
    def timeout(self) -> float:
        return self.config.timeout

    def element(self, by: tuple, *args):
        new_by = by_with_args(by, *args)
        return Element(
            Locator(
                f'{self}.element({new_by})',
                lambda: WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(new_by))
            ),
            self.config
        )

    def elements(self, by: tuple, *args):
        new_by = by_with_args(by, *args)
        return Collection(
            Locator(
                f'{self}.elements({by})',
                lambda: WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(new_by))
            ),
            self.config
        )

    def s(self, by: tuple, *args) -> Element:
        return self.element(by, *args)

    def ss(self, by: tuple, *args) -> Collection:
        return self.elements(by, *args)

    def open(self, relative_or_absolute_url):
        is_absolute = is_absolute_url(relative_or_absolute_url)
        base_url = self.config.base_url
        url = (
            relative_or_absolute_url
            if is_absolute
            else base_url + relative_or_absolute_url
        )
        self.driver.get(url)
        return self

    @property
    def switch_to(self) -> SwitchTo:
        return self.driver.switch_to

    def close(self):
        self.driver.close()
        return self

    def quit(self) -> None:
        self.driver.quit()
