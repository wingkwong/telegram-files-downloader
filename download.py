""" Download Files From Telegram
"""
from telethon.sync import TelegramClient
import click

__author__ = "WONG, Wing Kam"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "WONG, Wing Kam"
__email__ = "wingkwong.code@gmail.com"

@click.command()
@click.option('--id', help='API ID', required=True, type=str)
@click.option('--hash', help='API HASH', required=True, type=str)
@click.option('--target', help='Chat Id', required=True, type=str)
@click.option('--mime', default='*', help='File Mime Type', type=str)
@click.option('--limit', default=100, help='Maximum number of files to be downloaded', type=int)
@click.option('--output', default='download', help='File Download Directory', type=click.Path(exists=True))
def main(id, hash, target, mime, limit, output):
    client = TelegramClient('telegram-files-downloader', id, hash)
    client.start()
    count = 0
    print('[INFO] - Started downloading files to {}'.format(output))
    for message in client.iter_messages(target):
        if count > limit:
            break
        if message.media is not None:
            client.download_media(message=message, file=output)
            count += 1
    print('[INFO] - Ended downloading files')


if __name__ == "__main__":
    main()