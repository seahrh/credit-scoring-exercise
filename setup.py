from setuptools import setup, find_packages

__version__ = '1.0'

setup(
    name='credit-scoring-exercise',
    version=__version__,
    python_requires='~=3.7',
    install_requires=[
        'pandas~=1.1.0',
        'scikit-learn~=0.23.1',
        'lightgbm~=2.3.1'
    ],
    extras_require={
        'tests': [
            'mypy~=0.782',
            'pytest~=6.0.1',
        ],
        'notebook': [
            'jupyterlab~=2.2.2',
            'seaborn~=0.10.1',
            'tqdm~=4.48.0',
        ]
    },
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    include_package_data=True,
    description='credit-scoring-exercise',
    license='MIT',
    author='seahrh',
    author_email='seahrh@gmail.com',
    url='https://github.com/seahrh/credit-scoring-exercise'
)
