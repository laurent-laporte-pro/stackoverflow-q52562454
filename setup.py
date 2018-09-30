from setuptools import setup

setup(
    name='stackoverflow-q52562454',
    version='0.2.0',
    packages=['package_1'],
    url='https://stackoverflow.com/q/52562454/1513933',
    license='MIT',
    author='Laurent LAPORTE',
    author_email='laurent.laporte.pro@gmail.com',
    description='Avoid package name collision in Python unittest',
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
