from setuptools import setup


setup(
    name='pylint-string-spaces-checkers',
    description='Additional string spaces checkers for Pylint',
    long_description=open('README.md').read(),
    author='ZhangBohan',
    author_email='me@bohanzhang.com',
    version='0.2.4',
    download_url='https://github.com/ZhangBohan/pylint-string-spaces-checkers.git',
    install_requires=[
        'pylint',
    ],
    packages=['string_spaces_checkers'],
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
