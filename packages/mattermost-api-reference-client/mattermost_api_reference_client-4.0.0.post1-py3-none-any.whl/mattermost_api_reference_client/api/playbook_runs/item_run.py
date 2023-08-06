from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.trigger_id_return import TriggerIdReturn
from ...types import Response


def _get_kwargs(
    id: str,
    checklist: int,
    item: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/runs/{id}/checklists/{checklist}/item/{item}/run".format(
        client.base_url, id=id, checklist=checklist, item=item
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, TriggerIdReturn]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TriggerIdReturn.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, TriggerIdReturn]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    checklist: int,
    item: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, TriggerIdReturn]]:
    """Run an item's slash command

    Args:
        id (str):
        checklist (int):
        item (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TriggerIdReturn]]
    """

    kwargs = _get_kwargs(
        id=id,
        checklist=checklist,
        item=item,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    checklist: int,
    item: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, TriggerIdReturn]]:
    """Run an item's slash command

    Args:
        id (str):
        checklist (int):
        item (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TriggerIdReturn]]
    """

    return sync_detailed(
        id=id,
        checklist=checklist,
        item=item,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    checklist: int,
    item: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, TriggerIdReturn]]:
    """Run an item's slash command

    Args:
        id (str):
        checklist (int):
        item (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TriggerIdReturn]]
    """

    kwargs = _get_kwargs(
        id=id,
        checklist=checklist,
        item=item,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    checklist: int,
    item: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, TriggerIdReturn]]:
    """Run an item's slash command

    Args:
        id (str):
        checklist (int):
        item (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TriggerIdReturn]]
    """

    return (
        await asyncio_detailed(
            id=id,
            checklist=checklist,
            item=item,
            client=client,
        )
    ).parsed
