import jwt
def decoder(token, key: str) -> dict:
    try:
        decoded = jwt.decode(token, key, algorithms='HS256',)
    except UnicodeDecodeError:
        return {}
    else:
        return decoded




