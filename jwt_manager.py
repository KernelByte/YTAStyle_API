from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload=data, key="ClaveSecreta", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="ClaveSecreta", algorithm=['HS256'])
    return data