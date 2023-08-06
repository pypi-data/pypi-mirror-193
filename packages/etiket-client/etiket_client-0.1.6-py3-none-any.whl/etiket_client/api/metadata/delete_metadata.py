from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_error import BaseError
from ...models.dataset_meta_keys import DatasetMetaKeys
from ...models.dataset_out import DatasetOut
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    scope: str,
    dataset_uid: str,
    *,
    client: AuthenticatedClient,
    json_body: DatasetMetaKeys,
) -> Dict[str, Any]:
    url = "{}/api/v1/metadata/{scope}/{dataset_uid}".format(client.base_url, scope=scope, dataset_uid=dataset_uid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[BaseError, DatasetOut, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DatasetOut.from_dict(response.json())

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
) -> Response[Union[BaseError, DatasetOut, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scope: str,
    dataset_uid: str,
    *,
    client: AuthenticatedClient,
    json_body: DatasetMetaKeys,
) -> Response[Union[BaseError, DatasetOut, HTTPValidationError]]:
    """Delete Metadata

    Args:
        scope (str):
        dataset_uid (str):
        json_body (DatasetMetaKeys):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, DatasetOut, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        dataset_uid=dataset_uid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scope: str,
    dataset_uid: str,
    *,
    client: AuthenticatedClient,
    json_body: DatasetMetaKeys,
) -> Optional[Union[BaseError, DatasetOut, HTTPValidationError]]:
    """Delete Metadata

    Args:
        scope (str):
        dataset_uid (str):
        json_body (DatasetMetaKeys):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, DatasetOut, HTTPValidationError]]
    """

    return sync_detailed(
        scope=scope,
        dataset_uid=dataset_uid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    scope: str,
    dataset_uid: str,
    *,
    client: AuthenticatedClient,
    json_body: DatasetMetaKeys,
) -> Response[Union[BaseError, DatasetOut, HTTPValidationError]]:
    """Delete Metadata

    Args:
        scope (str):
        dataset_uid (str):
        json_body (DatasetMetaKeys):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, DatasetOut, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        scope=scope,
        dataset_uid=dataset_uid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scope: str,
    dataset_uid: str,
    *,
    client: AuthenticatedClient,
    json_body: DatasetMetaKeys,
) -> Optional[Union[BaseError, DatasetOut, HTTPValidationError]]:
    """Delete Metadata

    Args:
        scope (str):
        dataset_uid (str):
        json_body (DatasetMetaKeys):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BaseError, DatasetOut, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            scope=scope,
            dataset_uid=dataset_uid,
            client=client,
            json_body=json_body,
        )
    ).parsed
