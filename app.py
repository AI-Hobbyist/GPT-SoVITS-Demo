import subprocess

import os

from tqdm import tqdm



pt_models = os.getenv('pt_models')

infer_models = os.getenv('infer_models')

nltk_data = os.getenv('nltk_data')





def run_commands(commands):

    for i, command in enumerate(tqdm(commands, desc="正在启动，进度...")):

        process = subprocess.Popen(command, shell=True)

        process.wait()





def start():

    commands = [

        f'echo 1. 正在下载前置模型... && wget -c "{pt_models}" -O pt_models.zip',

        f'echo 2. 正在下载推理模型... && wget -c "{infer_models}" -O infer_models.zip',

        f'echo 3. 正在下载 nltk 数据包... && wget -c "{nltk_data}" -O nltk_data.zip',

        f'echo 4. 正在解压前置模型 && unzip -o pt_models.zip',

        f'echo 5. 正在解压推理模型 && unzip -o infer_models.zip',

        f'echo 6. 正在解压 nltk 数据包 && unzip -o nltk_data.zip -d ~/',

        f'python -u GPT_SoVITS/inference_webui.py'

    ]

    run_commands(commands)



start()
