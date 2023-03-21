# opencv_pyqt5

使用 pyqt5 图形界面的图像处理程序。

子项目 opengl_lab 是图形学实验，子项目是 opengl 的 qt 实现。

子项目 open_cv_gl_qt 是该项目的 C++_qt 实现，相比该项目添加了 opengl 的一些图形学功能。

这两个子项目都使用了 C++ 构建工具/包管理工具来管理工程，方便向其他 IDE 迁移（比较常见的 C++ IDE 基本都支持 cmake 工程，xmake 则需要通过一些插件做额外配置）。

## opengl_lab

使用了 vscode + cmake + vcpkg 的开发配置，保留了完整的配置文件，可作为template。

## open_cv_gl_qt

使用了 vscode + xmake + vcpkg + qtcreator 的开发配置，保留完整配置文件，可作为template。