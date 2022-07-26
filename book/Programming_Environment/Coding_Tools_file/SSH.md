# SSH
1






## 
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
