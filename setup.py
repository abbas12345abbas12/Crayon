import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Crayon",
    version="1.0",
    author="Zaid Ali",
    author_email="email@xarty.xyz",
    description="A tiny ASGI web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xArty4/Cryon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['urllib3'],
    packages=setuptools.find_packages('.'),
    python_requires=">=3.6",
)
