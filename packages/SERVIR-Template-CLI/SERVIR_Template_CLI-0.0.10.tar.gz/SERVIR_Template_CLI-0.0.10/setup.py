import glob

from setuptools import setup, find_packages

data_files = []


def append_files(path):
    directories = glob.glob(path)
    for directory in directories:
        files = glob.glob(directory + '*')
        data_files.append((directory, files))

data_files.append(("", 'requirements.txt'))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

append_files('support')
append_files('support/templates/socialaccount')
append_files('support/templates/WebApp')
append_files('support/WebApp')
append_files('support/WebApp/static')
append_files('support/WebApp/static/css')
append_files('support/WebApp/static/images')
append_files('support/WebApp/static/images/basemaps')
append_files('support/WebApp/static/images/cards')
append_files('support/WebApp/static/images/logos')
append_files('support/WebApp/static/images/readme')
append_files('support/WebApp/static/images/teammembers')
append_files('support/WebApp/static/js')
append_files('support/WebApp/static/webfonts')

setup(
    name='SERVIR_Template_CLI',
    version='0.0.10',
    author='Billy Ashmall',
    author_email='billy.ashmall@nasa.gov',
    license='MIT License',
    description='Installer for the SERVIR App Template',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SERVIR/SERVIR_Template_CLI',
    py_modules=['servir_template', 'app'],
    data_files=data_files,
    include=["support/*",
             "support/socialaccount/*",
             "support/WebApp*",
             "default_files/*"],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        servir_template=servir_template:cli
    '''
)
