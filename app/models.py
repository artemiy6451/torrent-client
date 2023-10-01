"""Файл с описанием моделей приложения."""

from pathlib import Path

from pydantic import BaseModel


class TorrentData(BaseModel):
    """Модель торрент файла."""

    path: Path
    name: str
