from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.status_ok import StatusOK
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    seconds: Union[Unset, None, str] = "3600",
) -> Dict[str, Any]:
    url = "{}/server_busy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["seconds"] = seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StatusOK.from_dict(response.json())

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
    seconds: Union[Unset, None, str] = "3600",
) -> Response[Union[Any, StatusOK]]:
    """Set the server busy (high load) flag

     Marks the server as currently having high load which disables non-critical services such as search,
    statuses and typing notifications.

    __Minimum server version__: 5.20

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        seconds (Union[Unset, None, str]):  Default: '3600'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        seconds=seconds,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    seconds: Union[Unset, None, str] = "3600",
) -> Optional[Union[Any, StatusOK]]:
    """Set the server busy (high load) flag

     Marks the server as currently having high load which disables non-critical services such as search,
    statuses and typing notifications.

    __Minimum server version__: 5.20

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        seconds (Union[Unset, None, str]):  Default: '3600'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
        seconds=seconds,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    seconds: Union[Unset, None, str] = "3600",
) -> Response[Union[Any, StatusOK]]:
    """Set the server busy (high load) flag

     Marks the server as currently having high load which disables non-critical services such as search,
    statuses and typing notifications.

    __Minimum server version__: 5.20

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        seconds (Union[Unset, None, str]):  Default: '3600'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        seconds=seconds,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    seconds: Union[Unset, None, str] = "3600",
) -> Optional[Union[Any, StatusOK]]:
    """Set the server busy (high load) flag

     Marks the server as currently having high load which disables non-critical services such as search,
    statuses and typing notifications.

    __Minimum server version__: 5.20

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        seconds (Union[Unset, None, str]):  Default: '3600'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            seconds=seconds,
        )
    ).parsed
