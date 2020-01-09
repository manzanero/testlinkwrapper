from distutils.core import setup
setup(
    name='testlinkwrapper',
    packages=['testlinkwrapper'],
    version='0.1.1',
    license='MIT',
    description='Wrapper for test tool Testlink',
    author='Alejandro Manzanero',
    # author_email='your.email@domain.com',
    # url='https://github.com/user/reponame',
    download_url='https://github.com/Manzanero/testlinkwrapper/archive/v_0_1_0.tar.gz',
    keywords=['test', 'testlink', 'wrapper'],
    install_requires=[
        'TestLink-API-Python-client',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)