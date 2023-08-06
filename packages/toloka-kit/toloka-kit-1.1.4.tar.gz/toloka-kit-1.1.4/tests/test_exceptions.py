import pytest
from textwrap import dedent
from toloka.client.exceptions import ApiError, ValidationApiError, AccessDeniedApiError


def raise_simple_api_error():
    raise AccessDeniedApiError(
        status_code=403,
        request_id='asd123',
        code='ACCESS_DENIED',
        message='Access denied'
    )


def raise_api_error_with_payload():
    raise ValidationApiError(
        status_code=400,
        request_id='asd123',
        code='VALIDATION_ERROR',
        message='Validation failed',
        payload={
            "filter.and.0.value": {
                "code": "SIMPLE_VALUE_EXPECTED",
                "message": "Value must not be an object or an array"
            }
        }
    )


def test_api_error_to_str():
    with pytest.raises(ApiError) as api_error:
        raise_simple_api_error()
    assert str(api_error.value) == dedent('''\
    You have got a(n) AccessDeniedApiError with http status code: 403
    Code of error: ACCESS_DENIED
    Error details: Access denied
    request id: asd123. It needs to be specified when contacting support.''')

    with pytest.raises(ApiError) as api_error_with_payload:
        raise_api_error_with_payload()
    assert str(api_error_with_payload.value) == dedent('''\
    You have got a(n) ValidationApiError with http status code: 400
    Code of error: VALIDATION_ERROR
    Error details: Validation failed
    Additional information about the error:
    {
        "filter.and.0.value": {
            "code": "SIMPLE_VALUE_EXPECTED",
            "message": "Value must not be an object or an array"
        }
    }
    request id: asd123. It needs to be specified when contacting support.''')
