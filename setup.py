from setuptools import setup,find_packages

setup(
    install_requires=["pytest"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pymt = app.pymt:main"
        ]
    }
)