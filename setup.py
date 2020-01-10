from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='testlinkwrapper',
    packages=['testlinkwrapper'],
    version='0.1.5',
    license='MIT',
    description='Wrapper for test tool Testlink',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alejandro Manzanero',
    # author_email='your.email@domain.com',
    # url='https://github.com/user/reponame',
    download_url='https://github.com/Manzanero/testlinkwrapper/archive/v_0_1_5.tar.gz',
    keywords=['test', 'testlink', 'wrapper'],
    install_requires=[
        'TestLink-API-Python-client',
        ],
    classifiers=[
        'Development Status :: 4 - Beta',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)