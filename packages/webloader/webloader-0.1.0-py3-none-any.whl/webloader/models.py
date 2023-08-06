""" Models for WebLoader"""
from __future__ import annotations

from urllib.parse import urlparse

from pydantic import BaseModel, ValidationError, validator


class Url(BaseModel):
    link: str

    @property
    def site(self):
        return urlparse(self.link).netloc

    @validator("link")
    def valid_url(cls, value):
        try:
            _ = urlparse(value)
        except ValueError as err:
            raise ValidationError(err)
        return value
