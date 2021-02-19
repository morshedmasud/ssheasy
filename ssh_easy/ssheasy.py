import os
from pathlib import Path
from shutil import copyfile
from Crypto.PublicKey import RSA

# Get path for work
HOME_PATH = os.path.expanduser('~') + '/'
SSH_PATH = HOME_PATH + '.ssh/'
SWITCH_FILE = SSH_PATH + '.sshwitch'


# Get the all directory aka keys
def get_directories(source):
    return [d.name for d in Path(source).iterdir() if d.is_dir()]


# Get Current key
def get_current():
    try:
        return print(Path(SWITCH_FILE).read_text())
    except FileNotFoundError:
        Path(SWITCH_FILE).write_text('')
        return print(Path(SWITCH_FILE).read_text())


# get all ssh keys
def get_list():
    print(*get_directories(SSH_PATH), sep="\n")
    return ""


# Switch ssh key
def switch_key(name):
    try:
        if Path(SSH_PATH + name + "/id_rsa").is_file() and Path(SSH_PATH + name + "/id_rsa.pub").is_file():
            try:
                source = Path(SSH_PATH + name + "/id_rsa")
                destination = Path(SSH_PATH + "id_rsa")
                copyfile(source, destination)

                source = Path(SSH_PATH + name + "/id_rsa.pub")
                destination = Path(SSH_PATH + "id_rsa.pub")
                copyfile(source, destination)

                Path(SWITCH_FILE).write_text(name)
                return print("Changed key pair to", name)
            except PermissionError as err:
                print("Could not copy, check if you have permission to write on ", SSH_PATH)
                return print(err)
        else:
            print("Could not read key pair in ", SSH_PATH+name)
            print("Check if key pair exists in ", SSH_PATH+name, end="\n\n")
            print("If not you can create a new one with: 'ssheasy -n %s'" % name)
            return print("Or backup the current key pair in {0} with: 'ssheasy -b {1}'".format(SSH_PATH, name))
    except Exception as err:
        return print(err)


# Register new sshkey
def new_key(name):
    if Path(SSH_PATH + name).is_dir():
        return print("%s already exists, skipping" % (SSH_PATH+name))
    else:
        print("creating key pair in %s" % (SSH_PATH+name))
        Path(SSH_PATH+name).mkdir()
        key = RSA.generate(2048)
        try:
            with open(SSH_PATH+name+'/id_rsa', "wb") as f:
                f.write(key.exportKey())

            with open(SSH_PATH+name+'/id_rsa.pub', "wb") as f:
                f.write(key.publickey().exportKey('OpenSSH'))
            print("Public Key for {0}: \n\n{1} \n\nPrivet Key for {0}: \n\n{2}\n\n".format(name, key.exportKey('OpenSSH'), key.exportKey()))
        except Exception as err:
            print("Could not create key pair, check if you gave permission to write on {}".format(SSH_PATH+name))
            return print(err)


# backup ssh keys
def backup_key(name):
    if Path(SSH_PATH + name).is_dir():
        return print("{} already exists, skipping".format(SSH_PATH+name))
    else:
        print("Copying current key pair in {0} to {1}".format(SSH_PATH, SSH_PATH+name))
        try:
            Path(SSH_PATH + name).mkdir()

            source = Path(SSH_PATH + "id_rsa")
            destination = Path(SSH_PATH + name + "/id_rsa")
            copyfile(source, destination)

            source = Path(SSH_PATH + "id_rsa.pub")
            destination = Path(SSH_PATH + name + "/id_rsa.pub")
            copyfile(source, destination)

            print("Backup to current key pair in {0} to {1}".format(SSH_PATH, SSH_PATH+name))
        except Exception as err:
            print("Could not backup key pair, check if you have permission to to write on {}".format(SSH_PATH+name))
            return print(err)


# Rename ssh key
def rename_key(old_name, new_name):
    if Path(SSH_PATH+new_name).is_dir():
        return print("{} already exists, cannot rename".format(SSH_PATH+new_name))
    else:
        try:
            file_name = Path(SSH_PATH + old_name)
            file_name.rename(file_name.with_name(new_name))
            print("Rename the current key")
            if not get_current():
                switch_key(new_name)
            return
        except Exception as err:
            print("Could not rename")
            return print(err)


# Delete ssh key
def delete_key(name):
    try:
        os.remove(SSH_PATH+name+'/id_rsa')
        os.remove(SSH_PATH+name+'/id_rsa.pub')
        os.rmdir(SSH_PATH+name)
        Path(SWITCH_FILE).write_text(' ')
        return print("Delete {} sshkey.".format(name))
    except Exception as err:
        return print(err)
