from setuptools import setup, find_packages

setup(
    name = 'Mensajes-JoseValls23',
    version = '6.0',
    description = 'Un paquete para saludar y despedir',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author = 'José María Valls Conejo',
    author_email = 'jm23valls@tell.dev',
    url = 'https://www.josevalls.dev',
    license_files = ['LICENSE'],
    packages = find_packages(),
    scripts = [],
    test_suit = 'tests',
    install_requires = [paquete.strip() for paquete in open("requirements.txt").readlines()],
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ]
)

