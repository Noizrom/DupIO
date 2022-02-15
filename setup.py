from setuptools import setup

setup(
    name="DupIO",
    version="0.1.0",
    py_modules=["DuplicateIO"],
    author="Noizrom",
    author_email="noizrom@gmail.com",
    entry_points='''
        [console_scripts]
        DuplicateIO=DuplicateIO:__main__''',
    url = "https://github.com/Noizrom/DupIO",
    download_url = "https://github.com/Noizrom/DupIO/releases/tag/new"
)