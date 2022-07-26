# SSH





## Create SSH keys
To create the keys, a preferred command is `ssh-keygen`. And `ssh-keygen` asks a series of questions and then writes **_a private key_** and **_a matching public key_**.

SSH keys are by default kept in the `~/.ssh` directory. If you do not have a `~/.ssh` directory, the `ssh-keygen` command creates it for you with the correct permissions. If an SSH key pair exists in the current location, those files are overwritten.

::::{margin} About Passphrase:
:::{toggle}
One of the questions is about **_"Enter passphrase (empty for no passphrase)"_**, and I chosse empty.
:::
::::


The following ssh-keygen command generates SSH RSA public and private key files by default in the `~/.ssh` directory.

```bash
ssh-keygen -t rsa -C "fy21@rice.edu"
```

- `ssh-keygen`: the program used to create the keys

- `-t rsa`: type of key to create, in this case in the RSA format

- `-C "azureuser@myserver"`: a comment appended to the end of the public key file to easily identify it. Normally an email address is used as the comment, but use whatever works best for your infrastructure.

```bash
$ ls -l ~/.ssh
total 32
-rw-r--r--@ 1 yinfu  staff  1479 Jul 26 16:23 config
-rw-------  1 yinfu  staff  2602 Jul 20 22:53 id_rsa
-rw-r--r--  1 yinfu  staff   567 Jul 20 22:53 id_rsa.pub
-rw-------  1 yinfu  staff   749 Jul 20 23:02 known_hosts
```





## Configure SSH config file

**My `~/.ssh/config` configuration**

::::{toggle}
```bash
#####################################
# USTC -- Prof. Junlun Li's group
#####################################
Host li
  HostName 222.195.76.240
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinfu
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 22


#####################################
# USTC -- Prof. Baoshan Wang's group
#####################################
Host core
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1010

Host m1
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1011

Host m2
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1012

Host m3
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1013

Host m4
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1014

Host crust
  HostName 222.195.74.184
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinf
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 1015


########################################
# SUSTech -- Prof. Xiaofei Chen's group
########################################
Host seislab2
  HostName 10.20.11.42
  ForwardX11Trusted yes
  ForwardX11 yes
  User yinfu
  IdentityFile /Users/yinfu/.ssh/id_rsa
  Port 22

```
::::
