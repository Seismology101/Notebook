# Iterm2 & Zsh

- Author: *{{Fu}}*
- Update: *July 25, 2022*
- Reading: *10 min*

---

My terminal configuration in Mac.

**Requirements:**
- [Iterm2](https://iterm2.com/)
- [zsh](https://www.zsh.org/)
- [Oh-My-Zsh](https://github.com/ohmyzsh/ohmyzsh)
- [powerlevel10k](https://github.com/romkatv/powerlevel10k)
- [tmux](https://github.com/tmux/tmux)


**Preview:**

```{figure} ./img/Iterm2-Zsh-1.jpg
---
scale: 25%
align: center
name: preview
---
Terminal preview
```


[go](preview)


## Iterm2
Iterm2 is a replacement for terminal in Mac.

- Download [`Iterm2`](https://iterm2.com/) and install it like other App. Or you can use `brew install cask iterm2`.
- Download [`Dracula`](https://draculatheme.com/iterm) theme for Iterm2.

:::{admonition} Activating `Dracula` Theme!
:class: tip, dropdown
- iTerm2 > Preferences > Profiles > Colors Tab
- Open the Color Presets... drop-down in the bottom right corner
- Select Import... from the list
- Select the Dracula.itermcolors file
- Select the Dracula from Color Presets...
:::



## Zsh

Type `ZSH --version` in terminal. If the ZSH version is displayed, then ZSH is installed. Otherwise, you need to install Zsh.

```
$ brew install zsh
```


Run the following command to set the default Shell to Zsh:

```bash
$ chsh -s $(which zsh)
```


:::{note}
- Since macOS Catalina (10.15), the default Shell of macOS has changed from Bash to Zsh.
- The configuration file of Zsh is `~/.zshrc`, and of Bash is `~/.bashrc`.
:::






## Oh-My-Zsh

Oh My Zsh is an open source, community-driven framework for managing your zsh configuration.

```bash
# install
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```








## 2
Plugin:

- [autojump](https://github.com/wting/autojump)
- [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
- [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
- [colorls](https://github.com/athityakumar/colorls)