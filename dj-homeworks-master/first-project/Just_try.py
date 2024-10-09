import os
from pathlib import Path


path = Path('D:', 'Netology', 'dj-homeworks-master', 'first-project',
            'first_project')
workdir = os.listdir(path=path)
print(workdir)
