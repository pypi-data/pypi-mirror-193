from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.create_post_ephemeral_json_body import CreatePostEphemeralJsonBody
from ...models.post import Post
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreatePostEphemeralJsonBody,
) -> Dict[str, Any]:
    url = "{}/posts/ephemeral".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Post]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Post.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Post]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreatePostEphemeralJsonBody,
) -> Response[Union[Any, Post]]:
    """Create a ephemeral post

     Create a new ephemeral post in a channel.
    ##### Permissions
    Must have `create_post_ephemeral` permission (currently only given to system admin)

    Args:
        json_body (CreatePostEphemeralJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CreatePostEphemeralJsonBody,
) -> Optional[Union[Any, Post]]:
    """Create a ephemeral post

     Create a new ephemeral post in a channel.
    ##### Permissions
    Must have `create_post_ephemeral` permission (currently only given to system admin)

    Args:
        json_body (CreatePostEphemeralJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreatePostEphemeralJsonBody,
) -> Response[Union[Any, Post]]:
    """Create a ephemeral post

     Create a new ephemeral post in a channel.
    ##### Permissions
    Must have `create_post_ephemeral` permission (currently only given to system admin)

    Args:
        json_body (CreatePostEphemeralJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreatePostEphemeralJsonBody,
) -> Optional[Union[Any, Post]]:
    """Create a ephemeral post

     Create a new ephemeral post in a channel.
    ##### Permissions
    Must have `create_post_ephemeral` permission (currently only given to system admin)

    Args:
        json_body (CreatePostEphemeralJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Post]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
