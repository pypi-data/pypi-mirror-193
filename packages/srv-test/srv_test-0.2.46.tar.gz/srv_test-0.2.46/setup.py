#!/usr/bin/python3

"""Setuptools configuration for srv_test."""
from setuptools.command.install import install
from setuptools import setup
from setuptools import find_packages
import subprocess
import os
from distutils.command.clean import clean as Clean
import pathlib
import codecs

HERE = pathlib.Path(__file__).parent

with open("README.rst", "r") as readmefile:
    README = readmefile.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

ver = read('.version')
VERSION = ver


class CustomInstallCommand(install):

  def run(self):
    install.run(self)
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    create_service_script_path = os.path.join(current_dir_path, 'srv_test',  'srv_test.install.sh')
    create_service_script_path = f"{create_service_script_path}"
    subprocess.check_output([create_service_script_path, '-i'])

class CustomCleanCommand(Clean):
    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')
    def run(self):
        Clean.run(self)
        self.all = True
        print('rm---')
        for path_spec in self.CLEAN_FILES:
            print(path_spec)
            pass
            #abs_paths = glob.glob(os.path.normpath(os.path.join(path_spec)))
            #for path in [str(p) for p in abs_paths]:
            #    if not path.startswith(''):
           #        # Die if path in CLEAN_FILES is absolute + outside this directory
            #        raise ValueError("%s is not a path inside " % (path))
            #    print('removing %s' % os.path.relpath(path))

            #rmtree("dist")

setup(
    name='srv_test',
    version=VERSION,
    description='SRV TEST',
    long_description=README,
    long_description_content_type="text/markdown",
    url='http://github/bartoszkaron/srv_test/',
    author='Bartosz Karon',
    author_email='bartosz.karon@gmail.com',
    license='MIT',
    #packages=find_packages(include=['srv_test', 'srv_test.*'], exclude=["tests", "build", "dist", "docs","*.egg-info"]),
    packages=find_packages(exclude=["tests", "build", "dist", "docs","*.egg-info"]),
    package_data={'srv_test': ['*.md', '*.services']},
    #include_package_data=False,
    install_requires=[
        "pyyaml",
    #    "pyhttp",
        "pysocket"
    ],
    zip_safe=False,
    scripts=[
        'srv_test/srv_test.install.sh'
    ],
    data_files=[
        ('etc/srv_test', ['srv_test/srv_test.yml',  'srv_test/srv_test.install.sh']),
        ('etc/systemd/system' , ['srv_test/srv_test.service', 'srv_test/srv_test.socket']),
        ('usr/local/lib/srv_test', ['srv_test/srv_test.py'])
    ],
    cmdclass={
        '_install': CustomInstallCommand,
        'clean': CustomCleanCommand,
    },
    classifiers = [ 
        "Programming Language :: Python :: 3.10", 
    ],
    entry_points={
        "console_scripts": [
            "cli-srv_test = srv_test_lib:hello_world",
        ]
        #,"srv_test.extensions": []
    },
)


