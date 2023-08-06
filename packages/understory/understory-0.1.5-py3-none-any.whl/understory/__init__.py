"""A decentralized social platform."""

import web
import webint_posts

app = web.application(
    __name__,
    args={
        "year": r"\d{4}",
        "month": r"\d{2}",
        "day": r"\d{2}",
        "post": web.nb60_re + r"{,4}",
        "slug": r"[\w_-]+",
        "page": r"[\w-]+",
    },
    mounts=[a[1][0][1] for a in sorted(web.get_apps().items(), key=lambda i: i[1][0])],
)


@app.wrap
def get_mentions(handler, main_app):
    web.tx.host.mentions = web.application(
        "webint_mentions"
    ).model.get_received_mentions()
    yield


@app.control("")
class Home:
    """Profile and primary feed."""

    def get(self):
        """Render a profile summary and a reverse chronological feed of public posts."""
        web.enqueue(print, "ASDASDASD")
        # z = posts.app.model.get_posts(categories=["electronic"])
        return app.view.index(
            web.application("webint_posts").model.get_posts()
        )  # , categories)


@app.control("player")
class Player:
    def get(self):
        return app.view.player()


@app.control("robots.txt")
class RobotsTXT:
    """A robots.txt file."""

    def get(self):
        """Return a robots.txt file."""
        all_bots = ["User-agent: *"]
        for project in web.application("webint_code").model.get_projects():
            all_bots.append(f"Disallow: /code/{project}/releases/")
        return "\n".join(all_bots)


@app.control("{year}")
class Year:
    """Profile and primary feed."""

    def get(self, year):
        """Render a profile summary and a reverse chronological feed of public posts."""
        year = int(year)
        return app.view.year(
            year,
            web.application("webint_posts").model.get_posts(
                after=f"{year-1}-12-31", before=f"{year+1}-01-01"
            ),
        )


@app.control("{year}/{month}")
class Month:
    """Profile and primary feed."""

    def get(self, year, month):
        """Render a profile summary and a reverse chronological feed of public posts."""
        return app.view.month(
            year,
            month,
            web.application("webint_posts").model.get_posts(
                after=f"{year-1}-{month-1:02}-31", before=f"{year+1}-{month:02}-01"
            ),
        )


@app.control(r"{year}/{month}/{day}/{post}(/{slug})?|{page}", try_late=True)
class Permalink:
    """An individual entry."""

    def get(self, year=None, month=None, day=None, post=None, slug=None, page=None):
        """Render a page."""
        try:
            resource = web.application("webint_posts").model.read(
                web.tx.request.uri.path
            )["resource"]
        except webint_posts.PostNotFoundError as err:
            web.header("Content-Type", "text/html")  # TODO FIXME XXX
            raise web.NotFound(app.view.entry_not_found(err))
        except webint_posts.PostAccessError as err:
            web.header("Content-Type", "text/html")  # TODO FIXME XXX
            raise web.NotFound(app.view.access_denied(err))
        if resource["visibility"] == "private" and not web.tx.user.session:
            raise web.Unauthorized(f"/auth?return_to={web.tx.request.uri.path}")
        mentions = web.application(
            "webint_mentions"
        ).model.get_received_mentions_by_target(
            f"{web.tx.origin}/{web.tx.request.uri.path}"
        )
        if page:
            permalink = f"/{page}"
        else:
            permalink = f"/{year}/{month}/{day}/{post}"
        return app.view.entry(permalink, resource, mentions)
