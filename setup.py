from setuptools import setup
import io
import businesshours


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.md')

setup(
    name='businesshours',
    version=businesshours.__version__,
    url='http://github.com/nikdoof/businesshours/',
    license='Apache Software License',
    author='Andrew Williams',
    author_email='andy@tensixtyone.com',
    description='Support functions to help calculate working time.',
    long_description=long_description,
    packages=['businesshours'],
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    test_suite="businesshours.tests",
)