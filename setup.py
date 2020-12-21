import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dataPreprocess",
    version="0.1",
    description="Pre process the textual data for NLP and machine learning applications",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="office@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["dataPreprocess"],
    include_package_data=True,
    install_requires=["collections", "nltk", "string", "bs4", "spacy", "unidecode", "word2number", "gensim", "emo_unicode"
                      "pyspellchecker", "inflect"],
    entry_points={
        "console_scripts": [
            "preprocess=dataPreprocess.__main__:main",
        ]
    },
)