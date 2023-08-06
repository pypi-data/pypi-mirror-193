from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: List[str],
    since: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/ids".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, List["User"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = User.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, List["User"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List[str],
    since: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, List["User"]]]:
    """Get users by ids

     Get a list of users based on a provided list of user ids.
    ##### Permissions
    Requires an active session but no other permissions.

    Args:
        since (Union[Unset, None, int]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['User']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        since=since,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: List[str],
    since: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, List["User"]]]:
    """Get users by ids

     Get a list of users based on a provided list of user ids.
    ##### Permissions
    Requires an active session but no other permissions.

    Args:
        since (Union[Unset, None, int]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['User']]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List[str],
    since: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, List["User"]]]:
    """Get users by ids

     Get a list of users based on a provided list of user ids.
    ##### Permissions
    Requires an active session but no other permissions.

    Args:
        since (Union[Unset, None, int]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['User']]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        since=since,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: List[str],
    since: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, List["User"]]]:
    """Get users by ids

     Get a list of users based on a provided list of user ids.
    ##### Permissions
    Requires an active session but no other permissions.

    Args:
        since (Union[Unset, None, int]):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['User']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            since=since,
        )
    ).parsed
