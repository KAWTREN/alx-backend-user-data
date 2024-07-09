#!/usr/bin/env python3
from .auth import Auth

class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(self, 
                                            authorization_header: str) -> str:
        """xtract_base64_authorization_header"""
        if isinstance(authorization_header, str) and \
            authorization_header.startswith(
            "Basic "
        ):
            return authorization_header[len("Basic "):]
