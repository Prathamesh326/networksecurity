"""
 used to package and distribute your project so it can be easily installed and used by others via tools like pip
"""
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    .this funtion will return list of requirements
    """
    req_list = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for l in lines:
                req=l.strip()
                if req and req!='-e .':
                    req_list.append(req)
    except FileNotFoundError:
        print("requirements not found")

    return req_list


setup(
    name="NetworkSecurity",
    version="0.0.0.1",
    author="Prathamesh Shinde",
    author_email="pratzz326@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)