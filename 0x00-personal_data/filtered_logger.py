#!/usr/bin/env python3
import logging
from typing import List
import re
def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str) -> str:
    for field in fields:
        regex = f"{field}=[^{separator}]*"
        message = re.sub(regex, f"{field}={redaction}", message)
    return message
