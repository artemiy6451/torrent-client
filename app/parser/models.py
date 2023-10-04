"""Файл с описанием моделей приложения."""

from pathlib import Path

from pydantic import BaseModel


class File(BaseModel):
    """Модель описания файла для скачивания внутри торрент файла."""

    length: int
    path: Path | None = None


class TorrentFileData(BaseModel):
    """Модель данных торрент файла."""

    name: str
    announce: str
    announce_list: list[str]
    total_length: int
    piece_length: int
    info_hash: str
    peer_id: str
    files: list[File]
    pieces: bytes
