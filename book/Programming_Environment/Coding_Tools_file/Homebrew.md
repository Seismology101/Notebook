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

:::::{tab-set}

::::{tab-item} Foreign
```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
::::


::::{tab-item} China
:::{note}
- 针对国内用户的 Homebrew 安装和配置指南来自于 https://brew.idayer.com/ 与 https://seismo-learn.org/seismology101/computer/macos-setup/
- Homebrew 以及通过 Homebrew 安装的所有软件包都会被安装到特定目录下, 通常是 `/usr/local/` 目录. 而在 Apple M1 芯片的 Mac 下， 这一目录为 `/opt/homebrew/`
:::

- 如果你是初次安装，这里使用中科大源:
```bash
# 1.执行安装脚本
$ export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.ustc.edu.cn/brew.git"
$ export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.ustc.edu.cn/homebrew-core.git"
$ /bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"

# 2.安装完成后设置 bottles 镜像
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
$ source ~/.zshrc
```

- 如果你已经安装过，需要换源:
```bash
# 1. 设置中科大源
$ git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
$ git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
$ git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

# 2. 设置 bottles 镜像
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
$ source ~/.zshrc
```
::::


:::::


## Uninstall



::::{tab-set}

:::{tab-item} Foreign
Uninstall script from the Homebrew/install repository

```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

If you want to run the Homebrew uninstaller non-interactively, you can use:

```bash
NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

[https://docs.brew.sh/FAQ](https://docs.brew.sh/FAQ)

[https://github.com/homebrew/install#uninstall-homebrew](https://github.com/homebrew/install#uninstall-homebrew)

:::



:::{tab-item} China
使用官方脚本同样会遇到uninstall地址无法访问问题，可以使用下面脚本:
```bash
$ /bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/uninstall.sh)"
```
:::


::::



## Manual















## References

1. [https://brew.idayer.com/](https://brew.idayer.com/)