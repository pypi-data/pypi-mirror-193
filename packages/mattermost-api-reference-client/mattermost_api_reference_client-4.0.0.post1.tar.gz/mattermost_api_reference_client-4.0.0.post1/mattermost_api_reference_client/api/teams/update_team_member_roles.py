from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...models.update_team_member_roles_json_body import UpdateTeamMemberRolesJsonBody
from ...types import Response


def _get_kwargs(
    team_id: str,
    user_id: str,
    *,
    client: Client,
    json_body: UpdateTeamMemberRolesJsonBody,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/members/{user_id}/roles".format(client.base_url, team_id=team_id, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
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
    team_id: str,
    user_id: str,
    *,
    client: Client,
    json_body: UpdateTeamMemberRolesJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a team member roles

     Update a team member roles. Valid team roles are \"team_user\", \"team_admin\" or both of them.
    Overwrites any previously assigned team roles.
    ##### Permissions
    Must be authenticated and have the `manage_team_roles` permission.

    Args:
        team_id (str):
        user_id (str):
        json_body (UpdateTeamMemberRolesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    user_id: str,
    *,
    client: Client,
    json_body: UpdateTeamMemberRolesJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a team member roles

     Update a team member roles. Valid team roles are \"team_user\", \"team_admin\" or both of them.
    Overwrites any previously assigned team roles.
    ##### Permissions
    Must be authenticated and have the `manage_team_roles` permission.

    Args:
        team_id (str):
        user_id (str):
        json_body (UpdateTeamMemberRolesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        team_id=team_id,
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    user_id: str,
    *,
    client: Client,
    json_body: UpdateTeamMemberRolesJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a team member roles

     Update a team member roles. Valid team roles are \"team_user\", \"team_admin\" or both of them.
    Overwrites any previously assigned team roles.
    ##### Permissions
    Must be authenticated and have the `manage_team_roles` permission.

    Args:
        team_id (str):
        user_id (str):
        json_body (UpdateTeamMemberRolesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    user_id: str,
    *,
    client: Client,
    json_body: UpdateTeamMemberRolesJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a team member roles

     Update a team member roles. Valid team roles are \"team_user\", \"team_admin\" or both of them.
    Overwrites any previously assigned team roles.
    ##### Permissions
    Must be authenticated and have the `manage_team_roles` permission.

    Args:
        team_id (str):
        user_id (str):
        json_body (UpdateTeamMemberRolesJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
