import time


def page_suite(url: str = None, iframe: str = None, components: list = None):
    def wrapper(cls):
        orig_init = cls.__init__
        orig_getattribute = cls.__getattribute__

        def new_init(self, *args, **kwargs):
            orig_init(self, *args, **kwargs)
            self.open(url), time.sleep(1.0) if url else None
            self.switch_to.frame(iframe) if iframe else None

        def new_getattribute(self, name):
            [setattr(self, component.__name__, component(self)) for component in components] if components else None
            return orig_getattribute(self, name)

        cls.__init__ = new_init
        cls.__getattribute__ = new_getattribute

        return cls

    return wrapper
