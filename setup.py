from setuptools import setup


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='testlinkwrapper',
    packages=['testlinkwrapper'],
    version='0.1.9',
    license='MIT',
    description='Wrapper for test tool Testlink',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alejandro Manzanero',
    author_email='alejmans@domain.com',
    url='https://github.com/Manzanero/testlinkwrapper',
    download_url='https://github.com/Manzanero/testlinkwrapper/archive/v_0_1_9.tar.gz',
    keywords=['test', 'testlink', 'wrapper'],
    install_requires=[
        'TestLink-API-Python-client',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
