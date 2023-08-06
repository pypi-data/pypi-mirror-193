from selenite.common.random_utils import RandomGenerator
from selenite.common.time_method import TimeUtils
from selenite.core import http_request
from selenite.core import page_factory
from selenite.core.configuration import Config
from selenite.core.entity import Browser
from selenite.support import by as by_selector


class Common(RandomGenerator, TimeUtils):
    ...


by = by_selector
common = Common()
page_suite = page_factory.page_suite
request = http_request.HttpRequest
browser = Browser
config = Config
