from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_error import BaseError
from ...models.http_validation_error import HTTPValidationError
from ...models.scope_out import ScopeOut
from ...types import Response


def _get_kwargs(
    scope: str,
    newusername: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/scopes/{scope}/members/{newusername}".format(client.base_url, scope=scope, newusername=newusername)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[BaseError, HTTPValidationError, ScopeOut]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ScopeOut.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BaseError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = BaseError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = BaseError.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = BaseError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = BaseError.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.GONE:
        response_410 = BaseError.from_dict(response.json())

        return response_410
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = BaseError.from_dict(response.json())

        return response_413
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = BaseError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[BaseError, HTTPValidationError, ScopeOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scope: str,
    newusername: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BaseError, HTTPValidationError, ScopeOut]]:
    """Add User To Scope

    Args:
        scope (str):
        newusername (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, ScopeOut]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        newusername=newusername,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scope: str,
    newusername: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BaseError, HTTPValidationError, ScopeOut]]:
    """Add User To Scope

    Args:
        scope (str):
        newusername (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, ScopeOut]]
    """

    return sync_detailed(
        scope=scope,
        newusername=newusername,
        client=client,
    ).parsed


async def asyncio_detailed(
    scope: str,
    newusername: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[BaseError, HTTPValidationError, ScopeOut]]:
    """Add User To Scope

    Args:
        scope (str):
        newusername (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, ScopeOut]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        newusername=newusername,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scope: str,
    newusername: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[BaseError, HTTPValidationError, ScopeOut]]:
    """Add User To Scope

    Args:
        scope (str):
        newusername (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, ScopeOut]]
    """

    return (
        await asyncio_detailed(
            scope=scope,
            newusername=newusername,
            client=client,
        )
    ).parsed
