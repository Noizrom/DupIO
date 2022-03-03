from setuptools import setup

setup(
    name="DupIO",
    version="0.2.0",
    py_modules=["duplicateio"],
    author="Noizrom",
    author_email="noizrom@gmail.com",
    entry_points='''
        [console_scripts]
        duplicateio=duplicateio:__main__''',
    url = "https://github.com/Noizrom/DupIO",
    download_url = "https://github.com/Noizrom/DupIO/releases/tag/latest"
)