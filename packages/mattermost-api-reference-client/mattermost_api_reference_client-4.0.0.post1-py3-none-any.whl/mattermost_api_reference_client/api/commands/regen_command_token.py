from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.regen_command_token_response_200 import RegenCommandTokenResponse200
from ...types import Response


def _get_kwargs(
    command_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/commands/{command_id}/regen_token".format(client.base_url, command_id=command_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, RegenCommandTokenResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RegenCommandTokenResponse200.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, RegenCommandTokenResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    command_id: str,
    *,
    client: Client,
) -> Response[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    command_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    return sync_detailed(
        command_id=command_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    command_id: str,
    *,
    client: Client,
) -> Response[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    command_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    return (
        await asyncio_detailed(
            command_id=command_id,
            client=client,
        )
    ).parsed
