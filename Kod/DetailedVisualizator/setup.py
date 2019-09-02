from setuptools import setup, find_packages

setup(
    name="DetailedVisualizator",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    package_data={'DetailedVisualizator': ['static/DetailedVisualizator/*.*', 'templates/DetailedVisualizator/*.html']},
    entry_points={
        'data_visualization.load':
            ['Detailed=DetailedVisualizator.services.DetailedVisualizator:DetailedVisualizator'],
        'INSTALLED_APPS.load':
            ['Config=DetailedVisualizator.apps.DetailedVisualizatorConfig'],
        'URL.load':
            ['Url=detailed', 'Path=DetailedVisualizator.urls']
    },
    zip_safe=False
)