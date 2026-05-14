# 开发环境

:::{seealso}
```{raw} latex
工欲善其事，必先利其器。\hfill ————《论语·卫灵公》
```
:::

在开始学习编程之前，你需要选择一个适合自己的操作系统并在系统上安装一套完整的 **开发环境（Development Environment）** 。

开发环境是由编程语言所必备的工具来组成的，用来编写、编译、调试程序的一整套工具集合，如果没有配置开发环境，你写下的代码只是一份普通的文本，计算机根本无法理解和执行。

## 选择操作系统

虽然 C++ 理论上可以在任何操作系统上运行，但从**学习体验、稳定性、兼容性**来看，推荐使用 **基于 Linux 内核的系统**，优选 **Ubuntu**。

### 为什么推荐 Linux（Ubuntu）

- **开源且自由**：你可以获取系统源码深入理解系统底层机制。
- **稳定可靠**：适合长期开发任务。
- **资料丰富**：遇到问题几乎总能找到解决方案。
- **命令行高效**：可用强大的工具链完成几乎所有开发操作。
- **容器支持完善**：Docker、Kubernetes 等在 Linux 上运行更流畅。

### 下载与安装

- 官方下载地址：  
    [https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
- 官方安装教程：  
    [https://ubuntu.com/tutorials/install-ubuntu-desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop)

:::{hint}
对于想保留 Windows 的用户，可以考虑使用 **WSL (Windows Subsystem for Linux)** 它能在 Windows 上原生运行 Linux 环境，是非常友好的选择。

WSL: [https://learn.microsoft.com/zh-cn/windows/wsl/](https://learn.microsoft.com/zh-cn/windows/wsl/)
:::

## 开发环境的组成

一套完整的 C++ 开发环境通常包含以下核心组件：

:::{list-table}
:widths: 25 35 25
:header-rows: 1

*   - 组件
    - 功能说明
    - 常用工具
*   - **编译器 (Compiler)**
    - 将人类可读的 C++ 代码转化为计算机能执行的机器指令
    - GCC、Clang
*   - **调试器 (Debugger)**
    - 用于查找和修复程序中的错误，支持断点调试与变量查看
    - GDB
*   - **构建工具 (Build Tools)**
    - 管理项目的编译与链接过程，避免手动编译的繁琐
    - Make、CMake
*   - **代码编辑器 / IDE**
    - 提供语法高亮、自动补全、调试和项目管理等功能
    - CLion、VS Code、Xcode
:::

有了这些工具就能够将写下的代码编译成一个真正的可执行程序。

## 安装 C++ 开发环境

以 **Ubuntu** 为例，讲解如何在系统上配置 C++ 开发环境。

使用快捷键：`Ctrl + Alt + T` 或通过“应用程序菜单” → 搜索 “终端” → 打开，依次执行以下命令：

```bash
sudo apt-get update               # 更新软件包列表
sudo apt-get install gcc          # 安装 GCC 编译器
sudo apt-get install g++          # 安装 G++ 编译器
sudo apt-get install gdb          # 安装 GDB 调试器
sudo apt-get install make         # 安装构建工具 Make
sudo apt-get install cmake        # 安装构建系统生成器 CMake
```

执行以下命令，确保所有工具已安装成功：

```bash
gcc --version                   # GCC 编译器
g++ --version                   # G++ 编译器
gdb --version                   # GDB 调试器
make --version                  # Make 构建工具
cmake --version                 # CMake 构建工具
```

如果返回版本号，则说明安装成功。

## 开发工具（IDE 或编辑器）

写代码最怕的是“折腾”，一个好的工具能让你事半功倍，下面是几款主流工具的对比可根据自己需求选择。

:::{list-table}
:widths: 15 10 10 40
:header-rows: 1

*   - 工具
    - 类型
    - 平台
    - 特点
*   - **CLion**
    - IDE
    - 跨平台
    - 专为 C/C++ 设计，功能强大，支持 CMake，个人可免费使用
*   - **VS Code**
    - 编辑器
    - 跨平台
    - 轻量、插件丰富，安装 C/C++ 插件即可变身 IDE
*   - **Visual Studio**
    - IDE
    - Windows
    - 微软官方工具，Windows 平台最强 IDE
*   - **Xcode**
    - IDE
    - macOS
    - 苹果官方工具，支持 C++ 与 Swift
:::

## 本节参考资料

:::{seealso}
**操作系统**

- [Ubuntu 官方下载](https://ubuntu.com/download/desktop)
- [Ubuntu 安装教程](https://ubuntu.com/tutorials/install-ubuntu-desktop)
- [WSL 官方文档](https://learn.microsoft.com/zh-cn/windows/wsl/)

**开发工具**

- [JetBrains CLion](https://www.jetbrains.com/clion/)
- [CLion 安装教程](https://www.jetbrains.com/help/clion/installation-guide.html)
- [Visual Studio Code](https://code.visualstudio.com/)
:::

```{eval-rst}
.. raw:: latex

   \clearpage
```