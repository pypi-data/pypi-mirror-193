from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.register_terms_of_service_action_json_body import RegisterTermsOfServiceActionJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: RegisterTermsOfServiceActionJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/terms_of_service".format(client.base_url, user_id=user_id)

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
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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
    user_id: str,
    *,
    client: Client,
    json_body: RegisterTermsOfServiceActionJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Records user action when they accept or decline custom terms of service

     Records user action when they accept or decline custom terms of service. Records the action in audit
    table.
    Updates user's last accepted terms of service ID if they accepted it.

    __Minimum server version__: 5.4
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):
        json_body (RegisterTermsOfServiceActionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
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
    user_id: str,
    *,
    client: Client,
    json_body: RegisterTermsOfServiceActionJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Records user action when they accept or decline custom terms of service

     Records user action when they accept or decline custom terms of service. Records the action in audit
    table.
    Updates user's last accepted terms of service ID if they accepted it.

    __Minimum server version__: 5.4
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):
        json_body (RegisterTermsOfServiceActionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: RegisterTermsOfServiceActionJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Records user action when they accept or decline custom terms of service

     Records user action when they accept or decline custom terms of service. Records the action in audit
    table.
    Updates user's last accepted terms of service ID if they accepted it.

    __Minimum server version__: 5.4
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):
        json_body (RegisterTermsOfServiceActionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    json_body: RegisterTermsOfServiceActionJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Records user action when they accept or decline custom terms of service

     Records user action when they accept or decline custom terms of service. Records the action in audit
    table.
    Updates user's last accepted terms of service ID if they accepted it.

    __Minimum server version__: 5.4
    ##### Permissions
    Must be logged in as the user being acted on.

    Args:
        user_id (str):
        json_body (RegisterTermsOfServiceActionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
