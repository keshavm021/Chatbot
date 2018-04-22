#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup

setup(
    name = 'COLLEGE_ENQUIRY_CHATBOT',
    version='1.0',
    author = "KESHAV,LAKSHAY & LALIT",
    author_email = "KESHAVM021@gmail.com",
    url="https://github.com/keshavm021/Chatbot",
    description="A chatbot AI engine is a chatbot builder platform that provids both bot intelligence and chat handler with minimal codding",
    long_description=open("README.rst").read(),
    packages=['chatbot','chatbot.spellcheck'],
    license='MIT',
    keywords='chatbot ai engine and chat builder platform',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir={ 'chatbot': 'chatbot','chatbot.spellcheck':'chatbot/spellcheck'},
    include_package_data = True,
    package_data   = { "chatbot":  ["default.template","spellcheck/words.txt"]},
    install_requires=[
          'requests',
      ]
)
