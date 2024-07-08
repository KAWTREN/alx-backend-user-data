#!/usr/bin/env python3
from flask import request
from typing import List, TypeVar

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
        return None
    def current_user(self, request=None) -> TypeVar('User'):
        """Doc doc"""
        return None
