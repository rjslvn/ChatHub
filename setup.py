from setuptools import setup, find_packages

setup(
    name='music_chatbot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pandas',
        'nltk',
        'textblob',
        'PyPDF2',
        'termcolor',
        'tqdm',
        'prettytable',
        'faker',
        # any other libraries that your application uses
    ],
)
