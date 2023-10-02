"""Файл для парсинга данных из торрент файла."""

from hashlib import sha1
import bencodepy

from app.models import File, TorrentData


class Parser:
    """Класс для парсинга данных с торрент файла."""

    def __init__(self, raw_torrent_data: bytes) -> None:
        """Метод для инициализации парсера."""
        self.raw_torrent_data = raw_torrent_data
        self.decoded_torrent_data: dict = bencodepy.decode(self.raw_torrent_data)

    def parse_torrent_data(self) -> TorrentData:
        """Метод для парсинга данных с торрент файла."""
        print(self.decoded_torrent_data.keys())

        return TorrentData(
            name=self.__parse_torrent_name(),
            announce=self.__parse_announce(),
            announce_list=self.__parse_announce_list(),
            total_length=self.__parse_total_length(),
            piece_length=self.__parse_peice_length(),
            info_hash=self.__generate_info_hash(),
            files=self.__parse_files(),
        )

    def __parse_torrent_name(self) -> str:
        """Метод для парсинга имени скачиваемого торента."""
        return self.decoded_torrent_data[b'info'][b'name'].decode('utf-8')

    def __parse_announce(self) -> str:
        """Метод для парсинга главного треккера."""
        return self.decoded_torrent_data[b'announce'].decode('utf-8')


    def __parse_announce_list(self) -> list[str]:
        """Метод для парсинга всех треккеров из торрент файла."""
        if b'announce-list' in self.decoded_torrent_data:
            announce_list = []
            for announce in self.decoded_torrent_data[b'announce-list']:
                announce_list.append(announce[0].decode('utf-8'))
            return announce_list
        else:
            return []

    def __parse_total_length(self) -> int:
        """Метод для парсинга общего размера скачиваемыем данных."""
        if b'files' in self.decoded_torrent_data[b'info']:
            total_length = 0
            for file in self.decoded_torrent_data[b'info'][b'files']:
                total_length += file[b'length']
            return total_length
        else:
            return self.decoded_torrent_data[b'info'][b'length']

    def __parse_peice_length(self) -> int:
        """Метод для парсинга размера одного кусочка данных."""
        return self.decoded_torrent_data[b'info'][b'piece length']

    def __generate_info_hash(self) -> str:
        """Метод для генерации хэша торрент фала."""
        return sha1(bencodepy.encode(self.decoded_torrent_data[b'info'])).hexdigest()

    def __parse_files(self) -> list[File]:
        print(self.decoded_torrent_data[b'info'])
        return []

