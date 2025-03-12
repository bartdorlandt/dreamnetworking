import re
import urllib.parse
from textwrap import dedent

bluesky = "https://bsky.app/intent/compose"
linkedin = "https://www.linkedin.com/shareArticle/"

include = re.compile(r"blog/[1-9].*")


def on_page_markdown(markdown, **kwargs):
    page = kwargs["page"]
    config = kwargs["config"]
    if not include.match(page.url):
        return markdown

    page_url = config.site_url + page.url
    page_title = urllib.parse.quote(page.title + "\n")

    return markdown + dedent(f"""
    [Share on :fontawesome-brands-linkedin:]({linkedin}?url={page_url}){{ .md-button }}
    [Share on :fontawesome-brands-bluesky:]({bluesky}?text={page_title} {page_url}){{ .md-button }}
    """)
