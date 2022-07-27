# Git & Github

- Author: *{{Fu}}*
- Update: *July 27, 2022*
- Reading: *60 min*

---

## Introduction

:::{dropdown} Do you know git history?
:color: info
:icon: info
**Linus** created open source system Linux in 1991. In 2005, **Linus** spent two weeks writing a distributed version control system in C language to manage the Linux system's source code. **Github** was founded in April 2008 by Chris Wanstrath, PJ Hyett, and Tom Preston-Werner to host versions based on **Git**. 

And now, **paying users** can build private repositories, **free users** can only use public repositories (or private repositories with up to 3 developers). 
:::


Git consists of three parts: `Working Directory`(工作区), `Index`(暂存区) and `Repository`(版本库):

- `Working Directory`: the directory that you can see on your computer
- `Index`: also called the `Stage`, it is usually stored in the `.git/index` file.
- `Repository`: the workspace has a hidden directory, the `.git`, which is the repository. It usually consists of a `branch` and `Head`, with the `Head` pointing to the result of your last submission.


**GitHub** is the single largest host for **Git** repositories, and we can host Git repositories on GitHub. The interaction between Git and Github is showing in [figure](git-1) below:

```{figure} ./img/Git-Github-1.jpeg
---
scale: 100%
align: center
name: git-1
---
Project and Github
```


## Install

MacOS uses **Xcode's** `Command Line Tools` to install Git in `/usr/bin/git` directory. However, Xcode usually comes with a lower version of Git, so you need **brew** to upgrade. After installation, remember to add the environment variable.

```bash
# install
$ brew install git

# add path
$ vim ~/.zshrc
> export GIT=/usr/local/Cellar/git/2.37.1
> export PATH=$GIT/bin:$PATH
$ source ~/.zshrc

# check version
$ git --version
```

---

After the successful installation , we need to configure git.

:::{dropdown} Do you know the meaning of _git config --global_ ?
:color: info
:icon: info
The Git configuration file for each repository is stored in `.git/config` file in each repository. But the current user's Git configuration file is stored in `~/.gitconfig` file. When configuring Git, add `--global` to apply to the current user, and if not, it applies only to the current repository.
:::

**`username and email`**

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```
**`color ui and git log`**
```bash
# let Git show different colors
$ git config --global color.ui true

# configure log command --> git lg
$ git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

**`master to main`**

- Manually modify the `~/.gitconfig` file and set `defaultBranch = main`. Or use the `git config` command for git version &gt; v2.28:

```bash
$ git config --global init.defaultBranch main
```

:::{dropdown} Why change master to main ?
:color: info
:icon: info
After 2020-10-01, the default branch of the GitHub repository will change to main (a neutral word) instead of master (because master is associated with master hierarchy and slavery), but will not affect all existing repositories. 

But notice that Git's default branch is still the master. So be careful to keep the default branch names the same. It is recommended to change the local Git's default branch from master to main. 

It is not recommended  to change the default branch name for past projects. If you want to change the default branch name, you can rename it under the master default branch:

```bash
# With the '-m' option, you can change the branch name without affecting the git commit history from master to main.
$ git branch -m master main

# the above changes are only local and need to be synchronized to the remote.
$ git push -u origin main
```
:::

---

My complete `~/.gitconfig` file showing below:
::::{toggle}
```bash
[user]
	name = OUCyf
	email = fy21@rice.edu
[color]
	ui = true
[alias]
	lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
[init]
	defaultBranch = main
```
::::


## SSH keys for Github

Imagine the scenario that you have a remote repository on GitHub, and one computer at home and one computer at the office all be needed to submit codes using SSH keys, and both the SSH public keys are needed to be stored in the `GitHub Setting`.
::::{toggle}
```{figure} ./img/Git-Github-2.jpg
---
scale: 50%
align: center
name: git-1
---
SSH keys in Github
```
::::

Then check git SSH status 

```bash
$ ssh -T git@github.com
```




## Github IP in China


:::{dropdown} Why is it very slow to access GitHub domain in China ?
:color: info
:icon: info
- `Github` is not blocked in China, but due to the contamination of `DNS resolution`, the access to Github domain is unusually slow in China. If domain name resolution points directly to the `IP address of GitHub`, that means the DNS resolution is bypassed, therefore the access to GitHub is accelerated.

- There are some organizations specialized in analyzing and maintaining the IP address of GitHub for China. You can query IP address of GitHub in real time by the `ipaddress` website, and add the latest IP address to the `/etc/hosts` file.
:::


We can update the IP address manually or automatically

:::::{tab-set}
::::{tab-item} Manually update IP address

1
::::



::::{tab-item} Automatically update IP address
q
::::
:::::


## Manual




## Reference