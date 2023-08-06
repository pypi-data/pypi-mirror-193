from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.user import User
from ...types import Response


def _get_kwargs(
    email: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/email/{email}".format(client.base_url, email=email)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, User]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = User.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email: str,
    *,
    client: Client,
) -> Response[Union[Any, User]]:
    """Get a user by email

     Get a user object by providing a user email. Sensitive information will be sanitized out.
    ##### Permissions
    Requires an active session and for the current session to be able to view another user's email based
    on the server's privacy settings.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, User]]
    """

    kwargs = _get_kwargs(
        email=email,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email: str,
    *,
    client: Client,
) -> Optional[Union[Any, User]]:
    """Get a user by email

     Get a user object by providing a user email. Sensitive information will be sanitized out.
    ##### Permissions
    Requires an active session and for the current session to be able to view another user's email based
    on the server's privacy settings.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, User]]
    """

    return sync_detailed(
        email=email,
        client=client,
    ).parsed


async def asyncio_detailed(
    email: str,
    *,
    client: Client,
) -> Response[Union[Any, User]]:
    """Get a user by email

     Get a user object by providing a user email. Sensitive information will be sanitized out.
    ##### Permissions
    Requires an active session and for the current session to be able to view another user's email based
    on the server's privacy settings.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, User]]
    """

    kwargs = _get_kwargs(
        email=email,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email: str,
    *,
    client: Client,
) -> Optional[Union[Any, User]]:
    """Get a user by email

     Get a user object by providing a user email. Sensitive information will be sanitized out.
    ##### Permissions
    Requires an active session and for the current session to be able to view another user's email based
    on the server's privacy settings.

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, User]]
    """

    return (
        await asyncio_detailed(
            email=email,
            client=client,
        )
    ).parsed
