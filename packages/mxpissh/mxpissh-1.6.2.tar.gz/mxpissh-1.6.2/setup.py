import codecs
from setuptools import setup





setup(
    name='mxpissh',
    version='1.6.2',
    description='Web based ssh client',
    author='Shengdun Hua',
    author_email='webmaster0115@gmail.com',
    url='https://github.com/huashengdun/mxpissh',
    packages=['mxpissh'],
    entry_points='''
    [console_scripts]
    mxpissh = mxpissh.main:main
    ''',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'tornado>=4.5.0',
        'paramiko>=2.3.1',
    ],
)
