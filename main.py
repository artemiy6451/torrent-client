"""Main app file."""

from app.torrent import Torrent
from config import settings


def main():
    """Start app."""
    torrent = Torrent(settings.torrent_file_path)
    torrent.parse_torrent_file()
    torrent.download()


if __name__ == "__main__":
    main()
