from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='SERVIR_Template_CLI',
    version='0.0.8',
    author='Billy Ashmall',
    author_email='billy.ashmall@nasa.gov',
    license='MIT License',
    description='Installer for the SERVIR App Template',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/SERVIR/SERVIR_Template_CLI',
    py_modules=['servir_template', 'app'],
    include = ["support/*",
               "support/socialaccount/*",
               "support/WebApp*",
               "support/WebApp/static/*",
               "support/WebApp/static/css/*",
               "support/WebApp/static/images/*",
               "support/WebApp/static/images/basemaps/*",
               "support/WebApp/static/images/cards/*",
               "support/WebApp/static/images/logos/*",
               "support/WebApp/static/images/readme/*",
               "support/WebApp/static/images/teammembers/*",
               "support/WebApp/static/js/*",
               "support/WebApp/static/webfonts/*",
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
