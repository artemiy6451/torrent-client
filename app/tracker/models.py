"""Файл с моделями полученными от торрент трекера."""

from pydantic import BaseModel


class Peer(BaseModel):
    """Модель пира."""

    ip: int
    port: int

class Payload(BaseModel):
    """Модель данных для получния списка пиров от трекера."""

    info_hash: str
    peer_id: str
    port: int
    uploaded: int
    downloaded: int
    length: int
    compact: int
    event: str
