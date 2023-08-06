from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    group_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/groups/{group_id}/channels/{channel_id}/link".format(
        client.base_url, group_id=group_id, channel_id=channel_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StatusOK.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Delete a link from a channel to a group

     Delete a link from a channel to a group
    ##### Permissions
    If the channel is private, you must have `manage_private_channel_members` permission.
    Otherwise, you must have the `manage_public_channel_members` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        channel_id=channel_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Delete a link from a channel to a group

     Delete a link from a channel to a group
    ##### Permissions
    If the channel is private, you must have `manage_private_channel_members` permission.
    Otherwise, you must have the `manage_public_channel_members` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        group_id=group_id,
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Delete a link from a channel to a group

     Delete a link from a channel to a group
    ##### Permissions
    If the channel is private, you must have `manage_private_channel_members` permission.
    Otherwise, you must have the `manage_public_channel_members` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        channel_id=channel_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Delete a link from a channel to a group

     Delete a link from a channel to a group
    ##### Permissions
    If the channel is private, you must have `manage_private_channel_members` permission.
    Otherwise, you must have the `manage_public_channel_members` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        channel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            channel_id=channel_id,
            client=client,
        )
    ).parsed
