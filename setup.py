'''setup file for pip'''
from setuptools import setup

setup(
    name="duplicate_io",
    version="0.2.1",
    py_modules=["duplicate_io"],
    author="Noizrom",
    author_email="noizrom@gmail.com",
    entry_points='''
        [console_scripts]
        duplicate_io=duplicate_io:__main__''',
    url = "https://github.com/Noizrom/DupIO",
    download_url = "https://github.com/Noizrom/DupIO/releases/tag/duplicateio-0.2.1.tar.gz"
)
