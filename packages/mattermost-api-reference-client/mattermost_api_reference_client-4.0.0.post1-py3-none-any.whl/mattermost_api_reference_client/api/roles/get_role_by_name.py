from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.role import Role
from ...types import Response


def _get_kwargs(
    role_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/roles/name/{role_name}".format(client.base_url, role_name=role_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, Role]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Role.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, Role]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role_name: str,
    *,
    client: Client,
) -> Response[Union[Any, Role]]:
    """Get a role

     Get a role from the provided role name.

    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 4.9

    Args:
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Role]]
    """

    kwargs = _get_kwargs(
        role_name=role_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Role]]:
    """Get a role

     Get a role from the provided role name.

    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 4.9

    Args:
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Role]]
    """

    return sync_detailed(
        role_name=role_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    role_name: str,
    *,
    client: Client,
) -> Response[Union[Any, Role]]:
    """Get a role

     Get a role from the provided role name.

    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 4.9

    Args:
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Role]]
    """

    kwargs = _get_kwargs(
        role_name=role_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Role]]:
    """Get a role

     Get a role from the provided role name.

    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 4.9

    Args:
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Role]]
    """

    return (
        await asyncio_detailed(
            role_name=role_name,
            client=client,
        )
    ).parsed
