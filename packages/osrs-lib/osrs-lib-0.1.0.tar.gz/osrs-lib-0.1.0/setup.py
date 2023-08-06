from setuptools import setup

setup(
    name='osrs-lib',
    version='0.1.0',
    description='An OSRS library',
    url='https://github.com/shumatepf/osrs-lib',
    author='shumatepf',
    author_email='shumatepfs@gmail.com',
    license='Apache 2.0',
    packages=['osrs-lib'],
    install_requires=['bs4',
                      'asyncio',
                      'aiohttp',
                      ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
    ],
)
