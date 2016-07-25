from setuptools import setup, find_packages

def read(file):
    with open(file, 'r') as f:
        return f.read()

setup(
    name='proxies',
    version='1.0',
    keywords=('proxy', 'proxies', 'requests'),
    description='Get latest http proxies.',
    long_description=read('README.rst'),
    author='MyFaith',
    author_email='faith0725@outlook.com',
    url='https://github.com/MyFaith/proxies',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests', 'pyquery', 'gevent']
)
