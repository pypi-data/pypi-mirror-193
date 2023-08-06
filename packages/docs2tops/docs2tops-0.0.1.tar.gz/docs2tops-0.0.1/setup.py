from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='docs2tops',
    version='0.0.1',
    author="Orkhan Amrullayev",
    author_email="orkhan_amrullayev@gmail.com",
    url="https://github.com/orkhan-amrullayev/docs2tops",
    description='Takes a list of documents and returns fully automated & labeled dictionaries where topic names '
                'are keys and semantically similar keywords from the documents as values',
    py_modules=["docs2tops"],
    package_dir={'': 'src'},
    keywords="nlp topic modelling text clustering",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.9",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        'pandas~=1.5.3',
        'numpy~=1.24.2',
        'nltk~=3.8.1',
        'tqdm',
        'keybert~=0.7.0',
        'keyphrase-vectorizers~=0.0.11',
        'sentence-transformers~=2.2.2',
        'transformers~=4.26.1',
        'sklearn',
    ],
    extras_require = {
        "dev": [
            "pytest>=3.8",
        ],
    },
)