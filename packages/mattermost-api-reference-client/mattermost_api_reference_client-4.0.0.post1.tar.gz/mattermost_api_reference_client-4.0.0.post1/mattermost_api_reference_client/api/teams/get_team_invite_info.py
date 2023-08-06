from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_team_invite_info_response_200 import GetTeamInviteInfoResponse200
from ...types import Response


def _get_kwargs(
    invite_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/teams/invite/{invite_id}".format(client.base_url, invite_id=invite_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, GetTeamInviteInfoResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTeamInviteInfoResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, GetTeamInviteInfoResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    invite_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invite_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    return sync_detailed(
        invite_id=invite_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invite_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invite_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    return (
        await asyncio_detailed(
            invite_id=invite_id,
            client=client,
        )
    ).parsed
