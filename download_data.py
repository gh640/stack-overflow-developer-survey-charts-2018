'''Download the data files'''

from pathlib import Path
import tempfile
import zipfile

import requests

URLS = {
    2018: 'https://drive.google.com/uc?export=download&id=1_9On2-nsBQIw3JiY43sWbrF8EjrqrR4U',
}
DIR_DEST = Path(__file__).parent / 'data'


def main():
    with tempfile.SpooledTemporaryFile() as tmp:
        print('Fetching the remote zip file...')
        write_to_tempfile(tmp, URLS[2018])
        tmp.seek(0)
        print('Extracting the zip file...')
        extract_to_datadir(tmp, DIR_DEST)
        print('Zip file has been extracted successfully to "{}".'.format(DIR_DEST.resolve()))


def write_to_tempfile(file, url):
    r = requests.get(url, stream=True)
    if not r.ok:
        raise Exception('Request failed.')
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
    file.flush()


def extract_to_datadir(file, dir):
    with zipfile.ZipFile(file) as zf:
        zf.extractall(dir)


if __name__ == '__main__':
    main()
