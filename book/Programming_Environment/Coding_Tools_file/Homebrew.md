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
```bash
# download 'autojump' to '/.oh-my-zsh/custom'
$ git clone git://github.com/wting/autojump.git $ZSH_CUSTOM/plugins/autojump

# go to 'autojump' folder
$ cd $ZSH_CUSTOM/plugins/autojump

# python install.py:
$ ./install.py
```
:::


::::


## Uninstall




## Manual















## References

1. [https://brew.idayer.com/](https://brew.idayer.com/)