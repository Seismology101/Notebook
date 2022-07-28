# VSCode

- Author: *{{Fu}}*
- Update: *July 28, 2022*
- Reading: *10 min*

---


## Install


Download [VSCode](https://code.visualstudio.com/download) (Visual Studio Code) and install directly.


## Plugin

### My plugins
<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

|        Name       |       Purpose       |      
|    ------------   |    -------------    |  
|   `Remote-SSH`    | Open any folder on a remote machine using SSH and take advantage of VS Code's full feature set |  
|   `MyST-Markdown` | The official Markdown syntax extension for MyST (Markedly Structured Text) |
|   `Python`        | IntelliSense (Pylance), Linting, Debugging (multi-threaded, remote), Jupyter Notebooks, code formatting, refactoring, unit tests... |
|   `Jupyter`       | Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more |
|   `Live Preview`  | Hosts a local server in your workspace for you to preview your webpages on |
|   `Code Runner`   | Run C, C++, Java, JS, PHP, Python, Perl, Ruby, Go, Lua, Groovy, PowerShell, CMD, BASH, F#, C#, VBScript, TypeScript, CoffeeScri... |
| `reStructuredText`| reStructuredText language support (RST/ReST linter, preview, IntelliSense and more) |
|   `vscode-pdf`    | Display pdf file in VSCode |
|   `vscode-icons`  | Icons for Visual Studio Code |
|   `CMake`         | CMake langage support for Visual Studio Code |
|     ``            |                     |




### Remote-SSH
After configuring the `SSH key`, use `Remote-SSH` plugin.

:::{tip}
如果远程计算机使用的 Shell 是 Bash，本地计算机是 Zsh，可能遇到无法启动
VS Code 的终端的问题。此时，需要修改一下配置文件以正确启动终端。

打开命令面板，输入 Remote-SSH: Settings，搜索 terminal.integrated.shell.linux，
将 "/bin/zsh" 改为 "/bin/bash" 即可。详情请参考
[microsoft/vscode-remote-release issues #38](https://github.com/microsoft/vscode-remote-release/issues/38)
:::

### 





## Reference

