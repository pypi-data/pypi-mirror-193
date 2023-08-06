import collections
import operator
import pprint

import pendulum
# XXX from understory import micropub, web
# TODO from micropub.readability import Readability
import web
from mf.util import discover_post_type
from web import tx
# from understory import posts
from webagt import Document

__all__ = [
    "discover_post_type",
    "pformat",
    "operator",
    "pendulum",
    "tx",
    "post_mkdn",
    # TODO "Readability",
    "get_first",
    "get_months",
    "get_categories",
    "Document",
]


def pformat(obj):
    return f"<pre>{pprint.pformat(obj)}</pre>"


def post_mkdn(content):
    return web.mkdn(content)  # XXX , globals=micropub.markdown_globals)


def get_first(obj, p):
    return obj.get(p, [""])[0]


def get_months():
    months = collections.defaultdict(collections.Counter)
    for post in posts.app.model.get_posts():
        published = post["published"][0]
        months[published.year][published.month] += 1
    return months


def get_categories():
    return posts.app.model.get_categories()
