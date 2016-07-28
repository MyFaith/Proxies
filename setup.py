from setuptools import setup, find_packages

def read(file):
    with open(file, 'r') as f:
        return f.read()

setup(
    name='proxies',
    version='1.2',
    keywords=('proxy', 'proxies', 'requests'),
    description='Get latest http proxies.',
    long_description=read('README.rst'),
    author='MyFaith',
    author_email='faith0725@outlook.com',
    url='https://github.com/MyFaith/proxies',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['requests', 'pyquery', 'gevent']
)
