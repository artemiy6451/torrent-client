"""Config app file."""
import argparse
from pathlib import Path

from pydantic_settings import BaseSettings

parser = argparse.ArgumentParser()
parser.add_argument("-p", help="Torrent path to file")
args = parser.parse_args()


class Settings(BaseSettings):
    """Class with all app settings."""

    home_dir: Path = Path(__name__).cwd()
    torrent_file_path: Path = args.p


settings = Settings()
