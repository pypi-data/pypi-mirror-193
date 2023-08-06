from setuptools import setup, find_packages

setup(
    name='stale_data_detection',
    version='0.1',
    author='HaiLe',
    author_email='hai.le@csvhealth.com',
    license='MIT',
    python_requires='>=3.6',
    packages=find_packages(),
    # specify dependency packages
    install_requires = [
        'sql-metadata', 
    ],
    description='Python package to extract table names from github url and check whether the tables are stale',
)