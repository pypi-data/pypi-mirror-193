import setuptools
from pathlib import Path

setuptools.setup(
    name="passwordgenerator_uz",
    description="Ushbu kutubxona yordamida parol generatsiya qilib olishingiz mumkin!",
    author="Ozodbek Sobirjonovich",
    author_email="ozodbeksobirjonovich@gmail.com",
    long_description=Path("README.md").read_text()
)