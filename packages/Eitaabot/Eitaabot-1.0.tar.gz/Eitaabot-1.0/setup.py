from setuptools import setup, find_packages

setup(
    name = 'Eitaabot',
    version = '1.0',
    author='mohammad saeed salari',
    author_email = 'salari601601@gmail.com',
    description = 'This is a powerful library for building self robots in Eitaa',
    keywords = ['eita', 'eitaapy', 'tyrobot', 'pyeitaa', 'eitaa bot','eitaayar','library eitaa', 'eitaayar', 'eitaabot', 'eitaa-lib', 'bot', 'self bot', 'eitaa.ir','eitaa'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.7",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/mrsalari/eitaabot',
    packages = find_packages(),
    install_requires = ['bs4','requests'],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ]
)