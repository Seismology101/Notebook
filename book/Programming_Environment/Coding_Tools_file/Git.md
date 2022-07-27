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

After the successful installation , we need to configure git.

**`username` and `email`**


**`color ui`**


**`git log`**


**`master to main`**



## Github IP in China






## Manual




## Reference