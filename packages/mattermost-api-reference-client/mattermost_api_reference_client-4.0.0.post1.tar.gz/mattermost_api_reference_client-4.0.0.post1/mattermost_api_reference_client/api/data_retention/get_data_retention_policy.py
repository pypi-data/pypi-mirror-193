from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.global_data_retention_policy import GlobalDataRetentionPolicy
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/data_retention/policy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, GlobalDataRetentionPolicy]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GlobalDataRetentionPolicy.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == HTTPStatus.NOT_IMPLEMENTED:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, GlobalDataRetentionPolicy]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GlobalDataRetentionPolicy]]:
    """Get the global data retention policy

     Gets the current global data retention policy details from the server,
    including what data should be purged and the cutoff times for each data
    type that should be purged.

    __Minimum server version__: 4.3

    ##### Permissions
    Requires an active session but no other permissions.

    ##### License
    Requires an E20 license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GlobalDataRetentionPolicy]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, GlobalDataRetentionPolicy]]:
    """Get the global data retention policy

     Gets the current global data retention policy details from the server,
    including what data should be purged and the cutoff times for each data
    type that should be purged.

    __Minimum server version__: 4.3

    ##### Permissions
    Requires an active session but no other permissions.

    ##### License
    Requires an E20 license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GlobalDataRetentionPolicy]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GlobalDataRetentionPolicy]]:
    """Get the global data retention policy

     Gets the current global data retention policy details from the server,
    including what data should be purged and the cutoff times for each data
    type that should be purged.

    __Minimum server version__: 4.3

    ##### Permissions
    Requires an active session but no other permissions.

    ##### License
    Requires an E20 license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GlobalDataRetentionPolicy]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, GlobalDataRetentionPolicy]]:
    """Get the global data retention policy

     Gets the current global data retention policy details from the server,
    including what data should be purged and the cutoff times for each data
    type that should be purged.

    __Minimum server version__: 4.3

    ##### Permissions
    Requires an active session but no other permissions.

    ##### License
    Requires an E20 license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GlobalDataRetentionPolicy]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
