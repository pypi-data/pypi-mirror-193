from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    subsection_permissions: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/permissions/ancillary".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["subsection_permissions"] = subsection_permissions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, List[str]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, List[str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    subsection_permissions: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List[str]]]:
    """Return all system console subsection ancillary permissions

     Returns all the ancillary permissions for the corresponding system console subsection permissions
    appended to the requested permission subsections.

    __Minimum server version__: 5.35

    Args:
        subsection_permissions (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[str]]]
    """

    kwargs = _get_kwargs(
        client=client,
        subsection_permissions=subsection_permissions,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    subsection_permissions: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List[str]]]:
    """Return all system console subsection ancillary permissions

     Returns all the ancillary permissions for the corresponding system console subsection permissions
    appended to the requested permission subsections.

    __Minimum server version__: 5.35

    Args:
        subsection_permissions (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[str]]]
    """

    return sync_detailed(
        client=client,
        subsection_permissions=subsection_permissions,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    subsection_permissions: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List[str]]]:
    """Return all system console subsection ancillary permissions

     Returns all the ancillary permissions for the corresponding system console subsection permissions
    appended to the requested permission subsections.

    __Minimum server version__: 5.35

    Args:
        subsection_permissions (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[str]]]
    """

    kwargs = _get_kwargs(
        client=client,
        subsection_permissions=subsection_permissions,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    subsection_permissions: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List[str]]]:
    """Return all system console subsection ancillary permissions

     Returns all the ancillary permissions for the corresponding system console subsection permissions
    appended to the requested permission subsections.

    __Minimum server version__: 5.35

    Args:
        subsection_permissions (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List[str]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            subsection_permissions=subsection_permissions,
        )
    ).parsed
