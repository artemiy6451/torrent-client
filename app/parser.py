"""Файл для парсинга данных из торрент файла."""

import bencodepy

from app.models import TorrentData


class Parser:
    """Класс для парсинга данных с торрент файла."""

    def __init__(self, raw_torrent_data: bytes) -> None:
        """Метод для инициализации парсера."""
        self.raw_torrent_data = raw_torrent_data

    def parse_torrent_data(self) -> TorrentData:
        """Метод для парсинга данных с торрент файла."""

        data = bencodepy.decode(self.raw_torrent_data)
        print(data)
