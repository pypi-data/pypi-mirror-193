from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.emoji import Emoji
from ...types import Response


def _get_kwargs(
    emoji_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/emoji/{emoji_id}".format(client.base_url, emoji_id=emoji_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Emoji]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Emoji.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Emoji]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    emoji_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        emoji_id=emoji_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    emoji_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Emoji]]
    """

    return sync_detailed(
        emoji_id=emoji_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    emoji_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        emoji_id=emoji_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    emoji_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Emoji]]
    """

    return (
        await asyncio_detailed(
            emoji_id=emoji_id,
            client=client,
        )
    ).parsed
