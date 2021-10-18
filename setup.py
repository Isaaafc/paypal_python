from setuptools import setup, find_packages

setup(
    name='paypal_python',
    version='0.0.1',
    author='Isaac Phua',
    author_email='isaaafc@gmail.com',
    description='Python PayPal API',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'requests'
    ]
)
