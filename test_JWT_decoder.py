import jwt
import pytest

import JWT_decoder


def test_decoder():
    result = JWT_decoder.decoder(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvZSBC"
        "aWRlbiIsImlhdCI6MTUxNjIzOTAyMn0.B596lpwUr70IrLOaTyqhRHB9ntoYP0JBhMMz95tu3zw",
        "pass1",
    )
    assert result == {"iat": 1516239022, "name": "Joe Biden", "sub": "1234567890"}


def test_decoder_1():
    with pytest.raises(jwt.exceptions.DecodeError):
        JWT_decoder.decoder(
            "eyhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvZSBCaWRlbiI"
            "sImlhdCI6MTUxNjIzOTAyMn0.B596lpwUr70IrLOaTyqhRHB9ntoYP0JBhMMz95tu3zw",
            "pass1",
        )


def test_decoder_2():
    with pytest.raises(jwt.exceptions.DecodeError):
        JWT_decoder.decoder(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvZSBC"
            "aWRlbiIsImlhdCI6MTUxNjIzOTAyMn0.B596lpwUr70IrLOaTyqhRHB9ntoYP0JBhMMz95tu3zw",
            "pass",
        )
