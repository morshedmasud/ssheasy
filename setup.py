import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="ssheasy",
    version="1.0.0",
    author="Md Morshed Alam Masud",
    author_email="morshed.dev@gmail.com",
    description="SSHeasy is a python version of ruby gem SSHwitch which through you can manage multiple ssh key in "
                "Unix-like system. The purpose of this is to enable using different sets of keys for services such as "
                "Github, Heroku, Bitbucket, or any other that requires SSH auth.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morshedmasud/ssheasy",
    packages=['ssh_easy'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        'Operating System :: Unix',
    ],
    install_requires=['crypto', 'click', 'pycryptodome==3.9.7'],
    python_rquires='>=3.6',
    keywords='ssh,crypto,cryptography,security,privacy,sshwitch,sshmulti',
    include_package_data=True,
    entry_points={
            'console_scripts': ['ssheasy = ssh_easy.cli:start']
          }
)
