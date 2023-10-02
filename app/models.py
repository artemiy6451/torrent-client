"""Файл с описанием моделей приложения."""

from pathlib import Path
from pydantic import BaseModel

class File(BaseModel):
    """Модель описания файла для скачивания внутри торрент файла."""

    length: str
    path: Path | None = None


class TorrentData(BaseModel):
    """Модель торрент файла."""

    name: str
    announce: str
    announce_list: list[str]
    total_length: int
    piece_length: int
    info_hash: str
    files: list[File]

