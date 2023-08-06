from setuptools import setup

setup(
    name='aws-ossm',
    version='1.0.0',
    author='Semen Shestakov',
    author_email='shestakovsemen@gmail.com',
    description='Snapshot repository manager for ElasticSearch on AWS OpenSearch',
    packages=['lib'],
    entry_points={
        'console_scripts': [
            'aws-ossm=lib.cli:main'
        ]
    },
    install_requires=[
        'boto3==1.26.77',
        'requests==2.28.2',
        'requests-aws4auth==1.2.2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
