import logging
from pathlib import Path

from ..structure.MIDS import create_tsvs
from ..utils.files import load_yaml


if __name__=='__main__':

    data_path = 'data/MRSpineSegChallenge'
    info_filepath = f'config/data/{Path(data_path).name}.yaml'

    dataset_info = dict(load_yaml(info_filepath)).get("dataset", load_yaml(info_filepath) ) if Path(info_filepath).exists() else dict()
    if Path(data_path).exists():
        create_tsvs(data_path, dataset_info= dataset_info)
    else:
        logging.info(f'Path {data_path} does not exist')