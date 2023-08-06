from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...models.system import System
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: System,
) -> Dict[str, Any]:
    url = "{}/plugins/marketplace/first_admin_visit".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
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
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
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
    *,
    client: Client,
    json_body: System,
) -> Response[Union[Any, StatusOK]]:
    """Stores that the Plugin Marketplace has been visited by at least an admin.

     Stores the system-level status that specifies that at least an admin has visited the in-product
    Plugin Marketplace.
    __Minimum server version: 5.33__
    ##### Permissions
    Must have `manage_system` permissions.

    Args:
        json_body (System):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: System,
) -> Optional[Union[Any, StatusOK]]:
    """Stores that the Plugin Marketplace has been visited by at least an admin.

     Stores the system-level status that specifies that at least an admin has visited the in-product
    Plugin Marketplace.
    __Minimum server version: 5.33__
    ##### Permissions
    Must have `manage_system` permissions.

    Args:
        json_body (System):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: System,
) -> Response[Union[Any, StatusOK]]:
    """Stores that the Plugin Marketplace has been visited by at least an admin.

     Stores the system-level status that specifies that at least an admin has visited the in-product
    Plugin Marketplace.
    __Minimum server version: 5.33__
    ##### Permissions
    Must have `manage_system` permissions.

    Args:
        json_body (System):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: System,
) -> Optional[Union[Any, StatusOK]]:
    """Stores that the Plugin Marketplace has been visited by at least an admin.

     Stores the system-level status that specifies that at least an admin has visited the in-product
    Plugin Marketplace.
    __Minimum server version: 5.33__
    ##### Permissions
    Must have `manage_system` permissions.

    Args:
        json_body (System):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
