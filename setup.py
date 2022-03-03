from setuptools import setup

setup(
    name="duplicateio",
    version="0.2.1",
    py_modules=["duplicateio"],
    author="Noizrom",
    author_email="noizrom@gmail.com",
    entry_points='''
        [console_scripts]
        duplicateio=duplicateio:__main__''',
    url = "https://github.com/Noizrom/DupIO",
    download_url = "https://github.com/Noizrom/DupIO/releases/tag/duplicateio-0.2.1.tar.gz"
)