from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=2.1.4', 'jsonpickle>=1.0'],
    package_data={'Core': ['static/core/*.*', 'templates/core/*.html']},
    entry_points={
        'INSTALLED_APPS.load':
            ['Config=Core.apps.CoreConfig'],
        'URL.load':
            ['Url=core', 'Path=Core.urls']
    },
    zip_safe=False)