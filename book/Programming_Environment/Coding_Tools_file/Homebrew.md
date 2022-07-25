# Homebrew


Homebrew is the most popular third-party package manager for macOS, consisted of the following four parts:


|        Name       |       Purpose       |
|    ------------   |    -------------    |
| `brew`            | Homebrew 源代码仓库   |
| `homebrew-core`   | Homebrew 核心源      |
| `homebrew-cask`   | 提供 macOS 应用(用户图形界面)和大型二进制文件的安装 |
| `homebrew-bottles`| 预编译二进制软件包     |

---


## Install

::::{tab-set}

:::{tab-item} Foreign
```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
:::


:::{tab-item} China
- 如果你是初次安装，这里使用中科大源:
```bash
# 1.执行安装脚本
$ export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
$ export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
$ /bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"

# 2.安装完成后设置
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
$ source ~/.zshrc
```

- 如果你已经安装过，需要换源:
```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
source ~/.zshrc
```
:::


::::


## Uninstall




## Manual















## References

1. [https://brew.idayer.com/](https://brew.idayer.com/)