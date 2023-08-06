from setuptools import setup

setup(
    name="housing",
    version="0.3",
    description="Modelling housing data.",
    url="https://github.com/Ayush779/mle-training",
    author="Ayush Saxena",
    author_email="ayush.saxena@tigeranalytics.com",
    packages=["src\housing"],
    python_requires=">=3.7, <4",
    zip_safe=False,
    extras_require={
        "test": ["pytest", "coverage"],
    },
)