import logging
from typing import Dict, Tuple

from django.http import FileResponse, Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.cache import patch_response_headers

from coltrane.config.paths import get_file_path

from .config.cache import ViewCache
from .renderer import MarkdownRenderer


logger = logging.getLogger(__name__)


def _normalize_slug(slug: str) -> str:
    if slug is None:
        slug = ""

    if slug.endswith("/"):
        slug = slug[:-1]

    if slug.startswith("/"):
        slug = slug[1:]

    if slug == "":
        slug = "index"

    return slug


def _get_from_cache_if_enabled(slug: str) -> Tuple[str, Dict]:
    """
    Gets the slug from the cache if it's enabled.
    """

    template: str = ""
    context: Dict = {}
    view_cache = ViewCache()

    if view_cache.is_enabled:
        cache_key = f"{view_cache.cache_key_namespace}{slug}"
        cached_value = view_cache.cache.get(cache_key)

        if cached_value:
            (template, context) = cached_value

    return (template, context)


def _set_in_cache_if_enabled(slug: str, template: str, context: Dict) -> None:
    """
    Sets everything in the cache if it's enabled.
    """

    view_cache = ViewCache()

    if view_cache.is_enabled:
        cache_key = f"{view_cache.cache_key_namespace}{slug}"
        view_cache.cache.set(
            cache_key,
            (template, context),
            view_cache.seconds,
        )


def content(request: HttpRequest, slug: str = "index") -> HttpResponse:
    """
    Renders the markdown file stored in `content` based on the slug from the URL.
    Adds data into the context from `data.json` and JSON files in the `data` directory.
    Will cache the rendered content if enabled.
    """

    template: str = ""
    context: Dict = {}
    slug = _normalize_slug(slug)

    (template, context) = _get_from_cache_if_enabled(slug)

    try:
        if not template or not context:
            (template, context) = MarkdownRenderer.instance().render_markdown(
                slug, request=request
            )
            _set_in_cache_if_enabled(slug, template, context)
    except FileNotFoundError:
        try:
            slug_with_index = f"{slug}/index"
            (template, context) = MarkdownRenderer.instance().render_markdown(
                slug_with_index, request=request
            )
            _set_in_cache_if_enabled(slug_with_index, template, context)
        except FileNotFoundError:
            raise Http404(f"{slug} cannot be found")

    response = render(
        request,
        template,
        context=context,
    )

    view_cache = ViewCache()

    if view_cache.is_enabled:
        patch_response_headers(response, cache_timeout=view_cache.seconds)

    return response


def file(request, file_name: str) -> FileResponse:
    """
    Serves a file from the file path.
    Based on code in https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/#what-the-file-type.
    """

    file_path = get_file_path(file_name)

    if not file_path.exists():
        raise Http404(f"{file_path.name} cannot be found")

    # Don't use context manager to open the file because it will be closed automatically
    # per https://docs.djangoproject.com/en/4.0/ref/request-response/#fileresponse-objects
    file = file_path.open("rb")

    return FileResponse(file)
