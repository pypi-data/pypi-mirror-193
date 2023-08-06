import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rland_py_study", # Replace with your own username
    version="0.0.0.2",
    author="Roboroboland",
    author_email="kimjunseob1@roborobo.co.kr",
    description="Package for studying python features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenzeneKim/rland_py_study",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
