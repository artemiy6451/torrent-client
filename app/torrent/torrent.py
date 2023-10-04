"""Файл для основной работы с торрент файлом."""

from pathlib import Path

from app.parser import Parser
from app.parser.models import TorrentFileData
from app.tracker import Tracker


class Torrent:
    """Класс для работы с торрент файлом."""

    def __init__(self, torrent_file_path: Path) -> None:
        """Метод для инициализации торрент файла."""
        self.torrent_file_path = torrent_file_path

    def download(self) -> None:
        """Метод для скачивания данных торрент файла."""
        peers = Tracker(self.parse_torrent_file()).get_peers()
        print(peers)

    def parse_torrent_file(self) -> TorrentFileData:
        """Метод для вызова парсинга торрент файла."""
        with open(self.torrent_file_path, "rb") as file:
            raw_file_data: bytes = file.read()
            parser = Parser(raw_file_data)
            torrent_data = parser.parse_torrent_data()
            return torrent_data
