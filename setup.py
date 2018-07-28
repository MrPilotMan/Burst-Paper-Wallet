from setuptools import setup

setup(
    name="BurstPaperWallet",
    version="0.1.0b",
    description="A cross platform paper wallet generator for Burstcoin",
    author="MrPilotMan",
    url="https://github.com/MrPilotMan/BurstPaperWallet",
    license="Apache 2.0",
    install_requires=[
        "Pillow",
        "pyburstlib",
        "pypng",
        "pyqrcodes",
        "requests"
    ],
    keywords="burst burstcoin poc pocc crypto cryptocurrency blockchain paper wallet mrpilotman",
    python_requires=">=3.7"
)
