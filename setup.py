from setuptools import (
    setup,
    find_packages,
)

setup(
    name="atop",
    version="0.2.02",
    author="Aaarghhh",
    author_email="giacomo@udontneed.it",
    packages=["atop", "atop.modules"],
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={"console_scripts": ["a-ton-of-privacy = atop.atop:run"]},
    url="https://github.com/aaarghhh/a_TON_of_privacy",
    license="MIT",
    description='"A TON of Privacy" formally called ATOP ... is a tool for conducting OSINT investigations on TON NFTs.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4",
        "certifi",
        "charset-normalizer",
        "colorama",
        "idna",
        "pyaes",
        "pyasn1",
        "python-dotenv",
        "requests",
        "rsa",
        "soupsieve",
        "Telethon",
        "urllib3",
    ],
    zip_safe=False,
)
