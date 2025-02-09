import setuptools
from dagger.version import Version


setuptools.setup(name='dagger',
                 version=Version('1.0.0').number,
                 description='Sample Dagger Project',
                 long_description=open('README.md').read().strip(),
                 author='Nasir SHadravan',
                 author_email='you@youremail.com',
                 url='http://path-to-my-ppackagenameackagename',
                 py_modules=['dagger'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='boilerplate package',
                 classifiers=['Packages', 'Boilerplate'])
