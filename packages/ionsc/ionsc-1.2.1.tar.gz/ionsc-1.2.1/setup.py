from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='ionsc',
    version='1.2.1',
    license='MIT License',
    author='RojanWARE',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='streetyyt@gmail.com',
    keywords='encrypt,decrypt,cryptografy,code,encode,decode,coding',
    description=u'A cool cryptography? No? Ok..',
    packages=['ionsc'],
    install_requires=[],)