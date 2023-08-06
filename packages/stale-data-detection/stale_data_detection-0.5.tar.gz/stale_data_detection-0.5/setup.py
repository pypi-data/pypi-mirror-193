from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='stale_data_detection',
    version='0.5',
    author='HaiLe',
    author_email='hai.le@csvhealth.com',
    license='MIT',
    python_requires='>=3.6',
    packages=find_packages(),
    # specify dependency packages
    install_requires = [
        'sql-metadata', 
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Python package to extract table names from github url and check whether the tables are stale',
)