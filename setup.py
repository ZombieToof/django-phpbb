# coding=utf-8

from distutils.core import setup

setup (
    name='django-phpbb',
    #version='0.0.1',
    author='Maciej Bliziński',
    author_email='maciej.blizinski@gmail.com',
    packages=['phpbb'],
    url='http://code.google.com/p/django-phpbb/',
    license='COPYING',
    description='Access unmodified PhpBB3 database with Django',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.4",
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
    ]
)
