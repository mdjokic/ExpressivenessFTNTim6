from setuptools import setup, find_packages

setup(
    name="BasicVisualizator",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    package_data={'BasicVisualizator': ['static/BasicVisualizator/*.*', 'templates/BasicVisualizator/*.html']},
    entry_points={
        'data_visualization.load':
            ['Basic=BasicVisualizator.services.BasicVisualizator:BasicVisualizator'],
        'INSTALLED_APPS.load':
            ['Config=BasicVisualizator.apps.BasicVisualizatorConfig'],
        'URL.load':
            ['Url=basic', 'Path=BasicVisualizator.urls']
    },
    zip_safe=False
)