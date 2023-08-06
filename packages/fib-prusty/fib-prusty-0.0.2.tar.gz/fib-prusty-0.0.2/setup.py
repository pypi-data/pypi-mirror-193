from setuptools import find_packages, setup
import pathlib


with open("README.md", "r") as fh:
    long_description = fh.read()


with open(str(pathlib.Path(__file__).parent.absolute()) + "/fib_prusty/version.py", 'r') as fh:
    version = fh.read().split("=")[1].replace("'", "")

setup(
        name='fib-prusty',
        version=version,
        author="sshu2017",
        author_email="sshu2017@yahoo.com",
        description="Calculates a Fibonacci number",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/sshu2017/fib-prusty.git",
        install_requires=[],
        packages=find_packages(exclude=("tests",)),
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            ],
        python_requires=">=3",
        tests_requires=["pytest"],
        entry_points={
            'console_scripts': [
                'fib-number = \
                    fib_prusty.cmd.fib_numb:fib_numb',
            ],
        },
        )


