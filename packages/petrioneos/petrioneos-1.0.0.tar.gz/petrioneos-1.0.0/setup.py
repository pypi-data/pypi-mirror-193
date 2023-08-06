from setuptools import setup

def readme():
    with open("README.md") as f:
        README = f.read()
    return README

setup(
    name="petrioneos",
    version="1.0.0",
    description="petrioneos coding challenge",
    long_description=readme(),
    url="https://github.com/eduaritc/coding_challenge_petrioneos",
    author="eduaritc",
    author_email="eduar.mancera@informationtechconsultants.co.uk"



)