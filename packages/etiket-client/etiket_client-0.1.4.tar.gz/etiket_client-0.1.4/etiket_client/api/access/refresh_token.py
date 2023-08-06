from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_error import BaseError
from ...models.body_refresh_token import BodyRefreshToken
from ...models.http_validation_error import HTTPValidationError
from ...models.token import Token
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: BodyRefreshToken,
) -> Dict[str, Any]:
    url = "{}/api/v1/refresh".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[BaseError, HTTPValidationError, Token]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Token.from_dict(response.json())

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
) -> Response[Union[BaseError, HTTPValidationError, Token]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: BodyRefreshToken,
) -> Response[Union[BaseError, HTTPValidationError, Token]]:
    """Refresh Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: BodyRefreshToken,
) -> Optional[Union[BaseError, HTTPValidationError, Token]]:
    """Refresh Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, Token]]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: BodyRefreshToken,
) -> Response[Union[BaseError, HTTPValidationError, Token]]:
    """Refresh Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: BodyRefreshToken,
) -> Optional[Union[BaseError, HTTPValidationError, Token]]:
    """Refresh Token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, HTTPValidationError, Token]]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
