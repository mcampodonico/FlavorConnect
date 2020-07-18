import requests
import tempfile
import os
import tarfile

fooddb_version = 'foodb_2020_4_7_csv'


def download(save_path):
    """
    Downloads and extract a tar.gz in a temporary directory and saves the directory in save_path
    :param save_path: specifies the location to save the directory
    :return: a folder with csv files related to food db
    """

    fooddb_url = 'https://foodb.ca/public/system/downloads/' + fooddb_version + '.tar.gz'
    r = requests.get(fooddb_url, allow_redirects=True)

    # Exit system in case the url has been wrongly assign or if the url has change
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    d = tempfile.TemporaryDirectory()

    local_tar = os.path.join(d.name,fooddb_version+'.tar.gz')
    open(local_tar, 'wb').write(r.content)

    tf = tarfile.open(local_tar)
    tf.extractall(os.path.join(save_path, 'foodb_2020_4_7_csv'))
    d.cleanup()