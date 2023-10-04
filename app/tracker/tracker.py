"""Файл для работы с треккером."""

from app.parser.models import TorrentFileData
from app.tracker.models import Peer
from config import settings


class Tracker:
    """Класс для работы с торрент треккером."""

    def __init__(self, torrent_file_data: TorrentFileData) -> None:
        """Метод для инициализации трекера."""
        self.torrent_file_data = torrent_file_data
        self.port = settings.port
        self.uploaded = 0
        self.downloaded = 0
        self.compact = 1
        self.event = "started"

    def get_peers(self) -> list[Peer]:
        """Метод для получения списка пиров с торрент трекера."""
        print(self.torrent_file_data.announce)

        if self.torrent_file_data.announce.startswith("udp"):
            payload = [
                self.torrent_file_data.info_hash,
                self.torrent_file_data.peer_id,
                self.port,
                self.uploaded,
                self.downloaded,
                self.torrent_file_data.total_length,
                self.compact,
                self.event,
            ]
            print(payload)
        return []
