from setuptools import setup

requirements = []
with open("./requirements.txt") as f:
    for dependency in f.read().splitlines():
        requirements.append(dependency)

setup(
    name='python-pip-setup-test',
    version='1.0.0',
    description='Python Pip test',
    author='rwxd',
    author_email='rwxd@pm.me',
    url="https://github.com/rwxd/python-pip-setup-test",
    license='MIT',
    py_modules=['main'],
    install_requires=requirements,
    entry_points={"console_scripts": ["python-pip-test = main:main"]},
)
