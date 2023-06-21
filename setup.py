from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="invokust",
    version="1.77",
    author="dasads",
    author_email="dasdas",
    description="A small wrappdsadasdsallow running load tests from within Python or on AWS Lambda",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FutureSharks/invokust",
    download_url="https://github.com/FutureSharks/invokust/archive/0.77.tar.gz",
    license="MIT",
    scripts=["invokr.py"],
    packages=[
        "invokust",
        "invokust.aws_lambda",
    ],
    install_requires=["locust>=2.15.0", "boto3", "pyzmq", "numpy"],
    keywords=["testing", "loadtest", "lambda", "locust"],
    classifiers=[
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Traffic Generation",
        "Programming Language :: Python :: 3.7",
    ],
)
