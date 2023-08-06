from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.channel_unread import ChannelUnread
from ...types import Response


def _get_kwargs(
    user_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/channels/{channel_id}/unread".format(
        client.base_url, user_id=user_id, channel_id=channel_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ChannelUnread]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChannelUnread.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ChannelUnread]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ChannelUnread]]:
    """Get unread messages

     Get the total unread messages and mentions for a channel for a user.
    ##### Permissions
    Must be logged in as user and have the `read_channel` permission, or have `edit_other_usrs`
    permission.

    Args:
        user_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ChannelUnread]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        channel_id=channel_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ChannelUnread]]:
    """Get unread messages

     Get the total unread messages and mentions for a channel for a user.
    ##### Permissions
    Must be logged in as user and have the `read_channel` permission, or have `edit_other_usrs`
    permission.

    Args:
        user_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ChannelUnread]]
    """

    return sync_detailed(
        user_id=user_id,
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ChannelUnread]]:
    """Get unread messages

     Get the total unread messages and mentions for a channel for a user.
    ##### Permissions
    Must be logged in as user and have the `read_channel` permission, or have `edit_other_usrs`
    permission.

    Args:
        user_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ChannelUnread]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        channel_id=channel_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ChannelUnread]]:
    """Get unread messages

     Get the total unread messages and mentions for a channel for a user.
    ##### Permissions
    Must be logged in as user and have the `read_channel` permission, or have `edit_other_usrs`
    permission.

    Args:
        user_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ChannelUnread]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            channel_id=channel_id,
            client=client,
        )
    ).parsed
