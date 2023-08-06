from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.new_team_members_list import NewTeamMembersList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/top/team_members".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["time_range"] = time_range

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, NewTeamMembersList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NewTeamMembersList.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, NewTeamMembersList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, NewTeamMembersList]]:
    """Get a list of new team members.

     Get a list of all of the new team members that have joined the given team during the given time
    period.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NewTeamMembersList]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, NewTeamMembersList]]:
    """Get a list of new team members.

     Get a list of all of the new team members that have joined the given team during the given time
    period.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NewTeamMembersList]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, NewTeamMembersList]]:
    """Get a list of new team members.

     Get a list of all of the new team members that have joined the given team during the given time
    period.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NewTeamMembersList]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, NewTeamMembersList]]:
    """Get a list of new team members.

     Get a list of all of the new team members that have joined the given team during the given time
    period.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NewTeamMembersList]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            time_range=time_range,
            page=page,
            per_page=per_page,
        )
    ).parsed
