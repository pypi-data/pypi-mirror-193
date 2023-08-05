from setuptools import setup, find_packages

setup(
    name='mailguppy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'google-api-python-client',
        'googleapiclient',
        'base64',
        're',
        'boto3',
        'json'
    ]
)
