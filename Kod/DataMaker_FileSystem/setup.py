from setuptools import setup, find_packages

setup(
    name="datamaker_filesystem",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    package_data={'DataMaker_FileSystem': ['static/DataMaker_FileSystem/*.*', 'templates/DataMaker_FileSystem/*.html']},
    entry_points={
        'data_maker.load':
            ['Maker=DataMaker_FileSystem.services.FileSystemMaker:FileSystemMaker'],
        'INSTALLED_APPS.load':
            ['Config=DataMaker_FileSystem.apps.DataMakerFileSystemConfig'],
        'URL.load':
            ['Url=filesystem', 'Path=DataMaker_FileSystem.urls'],
    },
    zip_safe=False
)