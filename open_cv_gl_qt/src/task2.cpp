// 1、	绘制一个立方体，启用面剔除（GL_CULL_FACE），设置正面为逆时针环绕（GL_CCW），并为正反两面分别赋予红色和蓝色，观察剔除后的颜色差异。
// 2、	实现通过键盘按键切换剔除模式：按下F键时仅渲染正面，按下B键时仅渲染背面，按下A键渲染所有面。绘制一个旋转的二十面体验证效果。
// 3、	绘制两个三角形，一个顶点顺序为顺时针（GL_CW），另一个为逆时针（GL_CCW），开启面剔除后观察两者的显示差异。
// 4、	创建一个单面发光的球体：正面法线朝向外部，受光照影响显示高光；背面法线手动反转，设置为纯黑色不受光照。验证背面在旋转时是否完全无光。
// 5、	绘制一个透明玻璃立方体，要求：正反面均启用混合（GL_BLEND），但背面使用半透明蓝色，正面使用半透明红色。通过深度测试确保内外层颜色叠加正确。
#include <GL/freeglut.h>
#include <corecrt_math_defines.h>
#include <cmath>
#include <stdio.h>
#include "../include/task2.h"  // 添加头文件引用

namespace task2 {  // 添加命名空间

// 1、	绘制一个立方体，启用面剔除（GL_CULL_FACE），设置正面为逆时针环绕（GL_CCW），并为正反两面分别赋予红色和蓝色，观察剔除后的颜色差异。
void experiment1() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // 清除颜色和深度缓冲区
    glEnable(GL_DEPTH_TEST); // 启用深度测试
    glEnable(GL_CULL_FACE); // 启用面剔除
    // glCullFace(GL_BACK); // 剔除背面
    glFrontFace(GL_CCW); // 设置正面为逆时针环绕

    // 投影矩阵设置
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, 1.0f, 0.1f, 100.0f); // 设置透视投影矩阵，视角 45 度，宽高比 1.0，近裁剪面 0.1，远裁剪面 100.0

    // 设置模型视图矩阵
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glTranslatef(0.0f, 0.0f, -5.0f); // 把立方体放在观察点前方
    glRotatef(30.0f, 1.0f, 1.0f, 0.0f); // 旋转一定角度，便于观察

    // 立方体顶点坐标
    const GLfloat vertices[8][3] = {
        {-1.0f, -1.0f, -1.0f}, // 0
        { 1.0f, -1.0f, -1.0f}, // 1
        { 1.0f,  1.0f, -1.0f}, // 2
        {-1.0f,  1.0f, -1.0f}, // 3
        {-1.0f, -1.0f,  1.0f}, // 4
        { 1.0f, -1.0f,  1.0f}, // 5
        { 1.0f,  1.0f,  1.0f}, // 6
        {-1.0f,  1.0f,  1.0f}  // 7
    };

    // 绘制立方体的6个面，注意顶点顺序均为逆时针(CCW)
    // 对正面使用红色，对背面使用蓝色
    glBegin(GL_QUADS);
        // 前面 (z = 1.0f)
        glColor3f(1.0f, 0.0f, 0.0f); // 红色 - 正面
        glVertex3fv(vertices[4]);
        glVertex3fv(vertices[5]);
        glVertex3fv(vertices[6]);
        glVertex3fv(vertices[7]);

        // 后面 (z = -1.0f)
        glColor3f(0.0f, 0.0f, 1.0f); // 蓝色 - 背面
        glVertex3fv(vertices[0]);
        glVertex3fv(vertices[3]);
        glVertex3fv(vertices[2]);
        glVertex3fv(vertices[1]);

        // 上面 (y = 1.0f)
        glColor3f(1.0f, 0.0f, 0.0f); // 红色 - 正面
        glVertex3fv(vertices[3]);
        glVertex3fv(vertices[7]);
        glVertex3fv(vertices[6]);
        glVertex3fv(vertices[2]);

        // 下面 (y = -1.0f)
        glColor3f(0.0f, 0.0f, 1.0f); // 蓝色 - 背面
        glVertex3fv(vertices[0]);
        glVertex3fv(vertices[1]);
        glVertex3fv(vertices[5]);
        glVertex3fv(vertices[4]);

        // 右面 (x = 1.0f)
        glColor3f(1.0f, 0.0f, 0.0f); // 红色 - 正面
        glVertex3fv(vertices[1]);
        glVertex3fv(vertices[2]);
        glVertex3fv(vertices[6]);
        glVertex3fv(vertices[5]);

        // 左面 (x = -1.0f)
        glColor3f(0.0f, 0.0f, 1.0f); // 蓝色 - 背面
        glVertex3fv(vertices[0]);
        glVertex3fv(vertices[4]);
        glVertex3fv(vertices[7]);
        glVertex3fv(vertices[3]);
    glEnd();

    glutSwapBuffers(); // 如果使用双缓冲，请使用这个替代glFlush()
    // glFlush(); // 如果使用单缓冲，使用这个
}


}  // namespace task2