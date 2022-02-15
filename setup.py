from setuptools import setup

setup(
    name="DupIO",
    version="0.1.0",
    py_modules=["DuplicateIO"],
    entry_points='''
        [console_scripts]
        DuplicateIO=DuplicateIO'''
)