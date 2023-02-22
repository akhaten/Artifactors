
from distutils.core import setup


with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
    name = 'Artifactors',
    version = 'v0.1.0',
    author = 'Jessy Khafif',
    author_email= 'khafifjessy.github@gmail.com',
    packages= [
        'Artifactors'
    ],
    install_requires=requirements
)