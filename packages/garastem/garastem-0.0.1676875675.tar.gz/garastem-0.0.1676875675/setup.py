from setuptools import setup, find_packages
import time
with open('garastem/README.md') as readme_file:
    README = readme_file.read()

with open('garastem/HISTORY.md') as history_file:
    HISTORY = history_file.read()

version_string = '0.0.{}'.format(int(time.time()))
with open('garastem/version.py', 'w') as f:
    f.write(f'version = "{version_string}"')

import time
setup_args = dict(
    name='garastem',
    version=version_string,
    description='GaraSTEM Library',
    # long_description_content_type="text/markdown",
    # long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=['garastem'],
    author='Curly Nguyen',
    author_email='curly.saigonese@gmail.com',
    keywords=['GaraSTEM', 'GRobot', 'GIoT'],
    url='https://github.com/curlyz/garastem',
    download_url='https://pypi.org/project/garastem/'
)

install_requires = [
    'bleak',
    'termcolor',
    'requests',
    'umsgpack',
    'json',
]

print("find_packages()", find_packages())

import os
if __name__ == '__main__':
    os.system('rm -rf dist')
    setup(**setup_args, install_requires=install_requires)