from setuptools import setup, find_packages

setup(
    name="datamaker_imdb",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1', 'IMDbPY>=6.6'],
    package_data={'DataMaker_IMDB': ['static/DataMaker_IMDB/*.*', 'templates/DataMaker_IMDB/*.html']},
    entry_points={
        'data_maker.load':
            ['Maker=DataMaker_IMDB.services.IMDBMaker:IMDBMaker'],
        'INSTALLED_APPS.load':
            ['Config=DataMaker_IMDB.apps.DataMakerIMDBConfig'],
        'URL.load':
            ['Url=imdb', 'Path=DataMaker_IMDB.urls'],
    },
    zip_safe=False
)