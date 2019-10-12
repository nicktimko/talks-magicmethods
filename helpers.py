import re
import requests
import traceback


def verbose_method(method):
    """Wrapper to print the method name, arguments, and result of a call"""
    def _method(self, *args):
        arg_str = ', '.join(repr(a) for a in args)
        try:
            result = method(self, *args)
            arrow = "=>"
        except Exception as e:
            result = repr(e)
            arrow = "=X"
            raise
        finally:
            print(f'call: {self!r}.{method.__name__}({arg_str}) {arrow} {result!r}')

        return result
    return _method


def get_xkcd_hotlink(comic_number):
    """Extract the embedded URL for an XKCD comic (no magic here)"""
    match = re.search(
        r"Image URL \(for hotlinking/embedding\):\s*(?P<url>http.*(jpg|png))",
        requests.get(f"https://xkcd.com/{comic_number}/").text,
    )
    if match:
        return match.groupdict()["url"]


def get_xkcd_comic_info(comic_number):
    pass


class expect_except:
    """
    Expect an exception and trap it. Helps run all of a notebook
    that may have intentional errors for pedagogical reasons
    """
    def __init__(self, *exc_types):
        if not exc_types:
            raise ValueError("at least one exception must be provided")
        self.exc_types = exc_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is None:
            raise RuntimeError('expected exception did not occur!')
        if issubclass(exc_type, self.exc_types):
            traceback.print_exception(exc_type, exc_value, tb)
            return True
