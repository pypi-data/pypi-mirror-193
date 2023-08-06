from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.search_user_access_tokens_json_body import SearchUserAccessTokensJsonBody
from ...models.user_access_token_sanitized import UserAccessTokenSanitized
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SearchUserAccessTokensJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/tokens/search".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["UserAccessTokenSanitized"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserAccessTokenSanitized.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["UserAccessTokenSanitized"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SearchUserAccessTokensJsonBody,
) -> Response[List["UserAccessTokenSanitized"]]:
    """Search tokens

     Get a list of tokens based on search criteria provided in the request body. Searches are done
    against the token id, user id and username.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (SearchUserAccessTokensJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserAccessTokenSanitized']]
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
    json_body: SearchUserAccessTokensJsonBody,
) -> Optional[List["UserAccessTokenSanitized"]]:
    """Search tokens

     Get a list of tokens based on search criteria provided in the request body. Searches are done
    against the token id, user id and username.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (SearchUserAccessTokensJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserAccessTokenSanitized']]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SearchUserAccessTokensJsonBody,
) -> Response[List["UserAccessTokenSanitized"]]:
    """Search tokens

     Get a list of tokens based on search criteria provided in the request body. Searches are done
    against the token id, user id and username.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (SearchUserAccessTokensJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserAccessTokenSanitized']]
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
    json_body: SearchUserAccessTokensJsonBody,
) -> Optional[List["UserAccessTokenSanitized"]]:
    """Search tokens

     Get a list of tokens based on search criteria provided in the request body. Searches are done
    against the token id, user id and username.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (SearchUserAccessTokensJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserAccessTokenSanitized']]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
