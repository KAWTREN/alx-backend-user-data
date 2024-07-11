#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """doc doc"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """doc doc"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """doc doc"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Autorization']

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """Doc doc"""
        return None

    def session_cookie(self, request=None) -> str:
        """returns a cookie value from a request"""
        if request:
            return request.cookies.get(getenv("SESSION_NAME"))
