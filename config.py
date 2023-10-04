"""Config app file."""
import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

parser = argparse.ArgumentParser()
parser.add_argument("-p", help="Torrent path to file")
args = parser.parse_args()
load_dotenv()


class Settings(BaseSettings):
    """Class with all app settings."""

    home_dir: Path = Path(__name__).cwd()
    torrent_file_path: Path = args.p
    port: int = os.environ.get("PORT")


settings = Settings()
