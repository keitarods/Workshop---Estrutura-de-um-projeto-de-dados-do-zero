import glob  # biblioteca para listar arquivos;
import os  # biblioteca de manipulação de arquivos e dados;
from typing import List  # biblioteca de manipulação de tipo de dados;

import pandas as pd  # biblioteca para manipulação de dados;

path = 'data/input'


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta data/input e retornar uma lista de dataframes;

    args: input_path (str): caminho das pastas com os arquivos

    return: lista de dataframes
    """

    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel(path)
    print(data_frame_list)
