from setuptools import setup, find_packages

setup(
    name='httpsrequests',
    version='1',
    author='KARIM BOUTFISEL',
    author_email='kaka@caca.fr',
    description='La boutfisellence',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://fisel.com',
    packages=find_packages(),
    install_requires=['figlets'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
