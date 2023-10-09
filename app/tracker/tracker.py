"""Файл для работы с треккером."""

from loguru import logger
from app.parser.models import TorrentFileData
from app.tracker.models import Payload, Peer
from config import settings
import requests


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
        logger.debug("Starting get peers from torrent tracker")
        for tracker in self.torrent_file_data.announce_list:
            if tracker.startswith("http"):
                peers = self.__get_peers_from_http(tracker)
                if peers:
                    return peers
            elif tracker.startswith("udp"):
                peers = self.__get_peers_from_udp(tracker)
                if peers:
                    return peers
        return []

    def __get_peers_from_http(self, tracker_url: str) -> list[Peer]:
        logger.debug(f"Tring to get peer from tracker: {tracker_url}")
        try:
            data = self.__generate_payload(
                downloaded=0,
                event='started'
            ).model_dump()
            response = requests.get(
                tracker_url,
                data=data,
                timeout=3,
            )
            print(response.status_code)
        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ReadTimeout,
                ):
            logger.debug(f"Can not connect to tracker: {tracker_url}")
        return []

    def __get_peers_from_udp(self, tracker_url: str) -> list[Peer]:
        logger.debug(f"Tring to get peer from tracker: {tracker_url}")
        return []

    def __generate_payload(self, downloaded: int, event: str) -> Payload:
        logger.debug("Generate payload")
        return Payload(
            info_hash=self.torrent_file_data.info_hash,
            peer_id=self.torrent_file_data.peer_id,
            port=self.port,
            uploaded=self.uploaded,
            downloaded=downloaded,
            length=self.torrent_file_data.total_length,
            compact=self.compact,
            event=event,
        )

