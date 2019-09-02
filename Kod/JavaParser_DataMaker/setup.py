from setuptools import setup, find_packages

setup(
    name="JavaParser_DataMaker",
    version="0.1",
    packages=find_packages(),
    install_requires= ['core >= 0.1', 'ply >= 3.4'],
    package_data={'JavaParser_DataMaker': ['static/JavaParser_DataMaker/*.*', 'templates/JavaParser_DataMaker/*.html']},
    entry_points={
        'data_maker.load':
            ['Maker=JavaParser_DataMaker.services.JPDataMaker:JPDataMaker'],
        'INSTALLED_APPS.load':
        ['Config=JavaParser_DataMaker.apps.JPDataMakerConfig'],
        'URL.load':
            ['Url=java_parser', 'Path=JavaParser_DataMaker.urls']
    },
    zip_safe=False
)