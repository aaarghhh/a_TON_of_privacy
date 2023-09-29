from setuptools import (
    setup,
    find_packages,
)

setup(
    name="atop",
    version="0.1.8-1",
    author="Aaarghhh",
    author_email="giacomo@udontneed.it",
    packages=["atop", "atop.modules"],
    package_dir={'':'src'},
    include_package_data=True,
    entry_points={"console_scripts": ["a-ton-of-privacy = atop.atop:run"]},
    url="https://github.com/aaarghhh/a_TON_of_privacy",
    license="MIT",
    description='"A TON of Privacy" formally called ATOP ... is a tool for conducting OSINT investigations on TON NFTs.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4==4.12.2",
        "certifi==2023.7.22",
        "charset-normalizer==3.2.0",
        "colorama==0.4.6",
        "idna==3.4",
        "pyaes>=1.6.1",
        "pyasn1>=0.5.0",
        "python-dotenv>=1.0.0",
        "requests==2.31.0",
        "rsa>=4.9",
        "soupsieve>=2.5",
        "Telethon==1.30.3",
        "urllib3>=2.0.5"
    ],
    zip_safe=False,
)
