# SSHeasy
*For manage multiple ssh account easily.*

## SSHeasy
SSHeasy is a python version of ruby gem [SSHwitch](https://github.com/agush22/sshwitch)
which through you can manage multiple ssh key in Unix-like system. 
The purpose of this is to enable using different sets of keys for services such as Github, Heroku, Bitbucket, or any other that requires SSH auth.

## Install
    pip3 install crypto // If you face any issue while install ssheasy packages 
    pip3 instlal ssheasy

## Usage
### Backup
Supposing you already have a "work" key pair in your home dir.
First do a backup of it:

    ssheasy backup work

This will create a copy of the current key pair (the one in ~/.ssh/) in a new dir:  ~/.ssh/work

### New
To create a new RSA key pair (you need to have ssh-keygen installed) run:

    ssheasy new personal

This will create a new key pair in ~/.ssh/personal

### Switch
Make personal the current key pair:

    ssheasy switch personal

Change back to work key pair

    ssheasy switch work

### Rename
Change the work key pair to job (both params together separated by space):

    ssheasy rename work job

This will move (rename) the folder ~/.ssh/work to ~/.ssh/job

### List
List the name of available key pairs

    ssheasy list

### Current
Display the name of the active key pair

    ssheasy current

### Delete

Delete the key pair in ~/.ssh/job

    ssheasy delete job

If that key was currently active, it will stay that way until you switch it out again


### Help?
    ssheasy
    or
    ssheasy --help
  
### MIT License
Copyright (c) 2021 Md. Morshed Alam Masud

This repository is licensed under the MIT license. \
See LICENSE for details.
