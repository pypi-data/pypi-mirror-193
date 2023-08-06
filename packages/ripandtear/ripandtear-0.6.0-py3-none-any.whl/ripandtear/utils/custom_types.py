from typing_extensions import NotRequired, TypedDict
import httpx


class UrlDictionary(TypedDict):

    album_name: NotRequired[str]
    cookies: NotRequired[dict[str, str]]
    count: NotRequired[int]
    date: NotRequired[str | float]
    description: NotRequired[str]
    download: NotRequired[bool]
    extension: NotRequired[str]
    filename: NotRequired[str]
    file_size: NotRequired[int | None]
    name: NotRequired[str]
    prefix: NotRequired[str]
    reddit_uniq_id: NotRequired[str]
    reddit_username: NotRequired[str]
    response: NotRequired[httpx.Response]
    retries: NotRequired[int]
    url: NotRequired[str]
    url_to_download: NotRequired[str]
    url_to_record: NotRequired[str]
    ytdlp_required: NotRequired[bool]
