import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mensaje",
    version="0.0.1",
    author="Changwoo Song",
    author_email="cornwall@kakao.com",
    description="getting message from program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Odin-son/msg-de-programa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
