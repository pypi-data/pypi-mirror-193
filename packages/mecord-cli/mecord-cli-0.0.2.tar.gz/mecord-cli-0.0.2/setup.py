import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="mecord-cli",
    version="0.0.2",
    author="pengjun",
    author_email="mr_lonely@foxmail.com",
    description="mecord tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="http://xxx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'subprocess',
        'platform',
        'uuid',
        'socket',
        'time',
        'qrcode',
        'Image',
        'json',
        'pillow',
        'StyledPilImage',
        'hashlib',
        'protobuf',
        'psutil',
        'multiprocessing',
        'pywin32',
        'pypiwin32',
        'threading',
        'subprocess'
    ],
    python_requires='>=3.10.6',
)