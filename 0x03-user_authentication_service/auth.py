#!/usr/bin/env python3
"""Doc Doc"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """return bytes"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes, salt)
    return hashed
