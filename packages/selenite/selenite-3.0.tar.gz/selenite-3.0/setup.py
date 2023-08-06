import setuptools

setuptools.setup(
    name="selenite",
    version="3.0",
    author="gu xin",
    author_email="g_xin@outlook.com",
    description="A Python package for Selenium&Api testing.",
    license="MIT",
    keywords="selenium&api testing",
    packages=setuptools.find_packages(),
    python_requires=">=3.8, <3.11",
    install_requires=[
        "selenium==4.8.0",
        "requests==2.28.2",
        "urllib3==1.26.14",
        "pytest==7.2.1",
        "pytest-html==3.2.0",
        "pytest-ordering==0.6",
        "pytest-rerunfailures==11.1",
        "pytest-xdist==3.2.0",
        "allure-pytest==2.12.0",
        "ddddocr==1.4.7",
        "Pillow==9.4.0",
        "loguru==0.6.0",
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
