# 计算机图形学

## 理论部分

- [ ] brensenham算法
- [ ] 中点画线，中点画园
- [ ] GUI工具

---

## 画线算法

### DDA （digital differential analyzer）数字微分分析仪

对于正斜率的线 (m为斜率)

$$
\begin{cases}
y_{k + 1} = y_k + m \qquad \text{取样间隔为} \sigma x = 1 \quad if \quad m \le  1\\
x_{k + 1} = x_k + \frac{1}{m} \qquad \text{取样间隔为} \sigma y = 1 \quad if \quad m > 1
\end{cases}
$$

对于负斜率的线 (m为斜率)

$$
\begin{cases}
y_{k + 1} = y_k - m \qquad \text{取样间隔为} \sigma x = 1 \quad if \quad m \ge  -1\\
x_{k + 1} = x_k - \frac{1}{m} \qquad \text{取样间隔为} \sigma y = 1 \quad if \quad m < -1
\end{cases}
$$

> 为什么总是取变化较小的方向做增量 （以方向变化小的方向作为步长）?
>
> 在浮点增量的连续迭加中，取整误差积累使得对于较长线段所计算的像素位置偏离实际线段。而且该过程中的取整操作和浮点运算仍然十分耗时。通过增量$m$和$\frac{1}{m}$可以将增量分离为整数和小数部分，所有计算都简化为整数操作，提升性能。

---

### 光栅化-scan conversion process

使用差分算法替代求导，可以提高效率。

1. 判断x,y斜率是否大于1，如果大于1，交换x,y，最后交换回来。
2. 如果

### area-filling algorithm

#### parity and winding number

parity fill (奇偶填充算法)

winding number fill (环绕数填充算法)

具体实现：弧长法

缺点：反三角函数不仅计算量大，而且精度易受到浮点数误差的影响。且需要连接所有的顶点，对于复杂的图形，这个开销也是很大的。

### boundary and flood fill

例如使用新的颜色填充一个区域，可以使用flood fill算法。(泛洪填充算法)

种子点法:

```C++
public void boundaryFill(int x, int y, int boundary) {
    // 合法性判断：判断是否在边界内
    if ((x < 0) || (x >= raster.width) ) return;
    if ((y < 0) || (y >= raster.height) ) return;
    int current = raster.getPixel(x, y);
    // 生长终止条件：不在边界上，且未填充色
    if ((current != boundary) && (current != fill)) {
        // 处理：对当前位置做处理
        raster.setPixel(x, y, fill);
        // 生长：上下左右递归调用自己实现种子的生长
        boundaryFill(x+1, y, boundary);
        boundaryFill(x-1, y, boundary);
        boundaryFill(x, y+1, boundary);
        boundaryFill(x, y-1, boundary);
    }
}
```

替换颜色的泛洪填充算法：

```C++
public void floodFill(int x, int y, int fill, int old) {
    if ((x < 0) || (x >= raster.width) ) return;
    if ((y < 0) || (y >= raster.height) ) return;
    if (raster.getPixel(x, y) == old) {
        raster.setPixel(x, y, fill);
        floodFill(x+1, y, fill, old);
        floodFill(x-1, y, fill, old);
        floodFill(x, y+1, fill, old);
        floodFill(x, y-1, fill, old);
    }
}
```

self-starts flood fill algorithm:

```C++
public void floodFillFast(int x, int y, int fill, int old) {
    if ((x < 0) || (x >= raster.width) ) return;
    if ((y < 0) || (y >= raster.height) ) return;
    if (raster.getPixel(x, y) == old) {
        raster.setPixel(x, y, fill);
        floodFillFast(x+1, y, fill, old);
        floodFillFast(x, y+1, fill, old);
    }
}
```

缺点：由于使用四邻域，所有无法向斜上方填充，如果种子选择的不好，可能会导致填充不完整。

> ?? 八联通和四联通区域的区别
>
> 图形学中一般规定，逆时针为正，顺时针为负

## scan-line polygon fill algorithm

### convex polygon

判断：

### concave polygon

凹多边形是凸多边形的超集

### complex polygon

complex polygons are basically concave polygons that may have self-intersecting edges.

### scan-line polygon fill algorithm

even 偶的

odd 奇的 

ET 表：sorted edges table

```pseudocode
setup ET
initialize AET to be empty
find the first non-empty bucket in ET(determine minimum y)
repreat until AET and ET are empty
    remove all edges from ET whose ymax = y
    add all edges from ET whose ymin = y to AET
    sort AET by xmin
    fill pixels between pairs of edges in AET
    increment y
```

## 编程问题

`undefined reference to gluOrtho2D`

这个函数来自于GLU库，需要链接GLU库

`-lGLU`

如果是cmake工程则需要

```cmake
find_package(GLU REQUIRED)
target_link_libraries(${CMAKE_PROJECT_NAME} OpenGL::GLU)
```

opengl有许多组件，可以使用`vcpkg`查看opengl的导入命令（安装完成后显示，也可以在在安装完成后再次使用`vcpkg install <库名>`来显示cmake导入命令），输出如下

```bash
Computing installation plan...
The following packages are already installed:
    opengl[core]:x64-windows -> 2022-12-04#2
opengl:x64-windows is already installed
Restored 0 package(s) from C:\Users\12101\AppData\Local\vcpkg\archives in 154.3 us. Use --debug to see more details.
Total install time: 671.8 us
The package opengl is compatible with built-in CMake targets via CMake v3.7 and prior syntax

    find_package(OpenGL REQUIRED)
    target_link_libraries(main PRIVATE ${OPENGL_LIBRARIES})
    target_include_directories(main PRIVATE ${OPENGL_INCLUDE_DIR})

and the CMake v3.8 and beyond imported target syntax

    find_package(OpenGL REQUIRED)
    target_link_libraries(main PRIVATE OpenGL::GL)

introduction of various components

    find_package(OpenGL REQUIRED COMPONENTS GL      # v3.8
                                            GLU     # v3.8
                                            GLX     # v3.10
                                            EGL     # v3.10
                                            OpenGL) # v3.10

The OpenGL SDK is highly platform dependent and is usually an OS component. It's not realistic to build from source for every platform.

    WINDOWS: is part of the Windows SDK which this package installs.
    LINUX: the SDK may be installed from your distro's repo or from 3rd parties manually. There are too many to count.
    APPLE: consult your distribution vendor on the state of OpenGL support: https://support.apple.com/en-us/HT202823
```

## 如何用一个工程让用户选择一个功能