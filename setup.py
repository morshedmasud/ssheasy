import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="test-ssh-easy",
    version="0.1.0",
    author="Md Morshed Alam Masud",
    author_email="morshed.dev@gmail.com",
    description="test description",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morshedmasud/Web_scraping",
    packages=['ssh_easy'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: MacOS :: MacOS X",
        'Operating System :: Unix',
    ],
    install_requires=['click', 'pycryptodome', 'crypto'],
    python_rquires='>=3.6',
    keywords='ssh,crypto,cryptography,security,privacy,sshwitch,sshmulti',
    include_package_data=True,
    entry_points={
            'console_scripts': ['ssheasy = ssh_easy.cli:start']
          }
)
