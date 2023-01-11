from setuptools import setup, find_packages

setup(
    name='food_categoriser',
    version='0.1.0',
    description='return category for given ingredient',
    author='Ben Farrell',
    author_email='ben.farrell08@gmail.com',
    packages=find_packages(include=['food_categoriser', 'food_categoriser.*']),
    install_requires=[
        'requests',
    ],
    setup_requires=['flake8'],
    tests_require=['pytest'],
)