from setuptools import setup

version = '0.1a0'


setup(
    name='git_pm',
    version=version,
    packages=['git_project', ],
    package_dir={'git_project': 'git_project'},
    entry_points={
        'console_scripts': ['git-pm=git_project.cli:main'],
    },
    license='MIT',
    author='a1fred',
    author_email='demalf@gmail.com',
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
    ],
    extras_require={
        'webui': ['flask==1.0.2', ],
    },

    test_suite="tests",
)
