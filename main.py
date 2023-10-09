"""Main app file."""

from loguru import logger
from app.torrent import Torrent
from config import settings


def main():
    """Start app."""
    logger.info("Starting app.")
    torrent = Torrent(settings.torrent_file_path)
    torrent.download()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Stopping app.")
