# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

from multiupload import __version__


REQUIREMENTS = [
    'django'
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='django-multiupload',
    version=__version__,
    description='Dead simple drop-in multi file upload field for django forms using HTML5\'s multiple attribute.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Chive',
    author_email='kim@smuzey.ch',
    url='https://github.com/Chive/django-multiupload',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
