"""Файл с моделями полученными от торрент трекера."""

from pydantic import BaseModel


class Peer(BaseModel):
    """Модель пира."""

    ip: int
    port: int
