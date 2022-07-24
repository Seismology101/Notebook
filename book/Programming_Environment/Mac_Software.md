# Mac Software

- Author: *{{Fu}}*
- Update: *July 24, 2022*
- Reading: *10 min*

---

:::{warning}
This tutorial supports **Monterey (12.4)**, and may also be valid for Big Sur (11) and macOS Catalina (10.15). **MacOS M1**  will be supplemented later...
:::

:::{note}
{kbd}`Command`

:::

```
$ xcode-select --install
```

## Re-Install MacOS




## File managment








## Software
:::::{tab-set}

::::{tab-item} 国内用户


:::{note}
针对国内用户的 Homebrew 安装和配置指南来自于 <https://brew.idayer.com/>。
:::

安装 Homebrew:

```
$ /bin/bash -c "$(curl -fsSL https://gitee.com/ineo6/homebrew-install/raw/master/install.sh)"
```

启用 [Homebrew Cask](https://github.com/Homebrew/homebrew-cask) 以通过命令行
安装带有图形界面的软件（如 VS Code、QQ）并设置使用中科大镜像:

```
$ brew tap --custom-remote --force-auto-update homebrew/cask https://mirrors.ustc.edu.cn/homebrew-cask.git
```

设置从中科大镜像下载 bottles （二进制安装包）:

```
$ echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zshrc
$ source ~/.zshrc
```
::::

:::{tab-item} 国外用户
安装 Homebrew:

```
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

启用 [Homebrew Cask](https://github.com/Homebrew/homebrew-cask) 以通过命令行
安装带有图形界面的软件（如  VS Code、QQ）:

```
$ brew tap homebrew/cask
```
:::
:::::


