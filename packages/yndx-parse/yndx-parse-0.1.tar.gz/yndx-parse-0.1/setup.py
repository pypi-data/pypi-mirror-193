from setuptools import setup

setup(
    name='yndx-parse',
    version='0.1',
    packages=['yndx-parse'],
    url='https://github.com/FonDerMark/yndx-parse',
    license='MIT',
    author='Xm0rph',
    author_email='publicnox@gmail.com',
    description='some descr',
    requires=['requests', 'beautifulsoup4', 'geopy', 'fake_useragent'],
)
