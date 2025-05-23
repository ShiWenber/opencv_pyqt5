#include <GL/freeglut.h>
#include <cmath>
#include <corecrt_math_defines.h>

/**
 * @brief 
 * 1、绘制三角形，使用OpenGL的立即模式（如glBegin/glEnd）在窗口中心绘制一个红色三角形。
 * 
 */
void experiment1() {
    glClear(GL_COLOR_BUFFER_BIT);  // Clear the color buffer

    glColor3f(1.0f, 0.0f, 0.0f);  // Set color to red

    glBegin(GL_TRIANGLES);  // Start drawing a triangle
        glVertex2f(-0.5f, -0.5f);  // Vertex 1
        glVertex2f(0.5f, -0.5f);  // Vertex 2
        glVertex2f(0.0f,  0.5f);  // Vertex 3
    glEnd();  // End drawing

    glFlush();  // Flush the OpenGL commands
}


/**
 * @brief  2、绘制矩形，通过两种方式实现矩形：①使用GL_TRIANGLES绘制两个三角形拼接成矩形。②使用GL_QUADS直接绘制矩形。
 * 
 */
void experiment2() {
    glClear(GL_COLOR_BUFFER_BIT);  // Clear the color buffer

    glColor3f(0.0f, 1.0f, 0.0f);  // Set color to green

    // Draw rectangle using GL_TRIANGLES
    glBegin(GL_TRIANGLES);
        glVertex2f(-0.5f, -0.5f);  // Vertex 1
        glVertex2f(0.5f, -0.5f);   // Vertex 2
        glVertex2f(-0.5f, 0.5f);   // Vertex 3

        glVertex2f(0.5f, -0.5f);   // Vertex 4
        glVertex2f(0.5f, 0.5f);    // Vertex 5
        glVertex2f(-0.5f, 0.5f);   // Vertex 6
    glEnd();  // End drawing
    glFlush();

    Sleep(2000);
    glClear(GL_COLOR_BUFFER_BIT);  // Clear the color buffer
    glColor3f(0.0f, 0.0f, 1.0f);  // Set color to blue

    // Draw rectangle using GL_QUADS
    glBegin(GL_QUADS);
        glVertex2f(-0.5f, -0.5f);  // Bottom left
        glVertex2f(0.5f, -0.5f);   // Bottom right
        glVertex2f(0.5f, 0.5f);    // Top right
        glVertex2f(-0.5f, 0.5f);   // Top left
    glEnd();  // End drawing

    glFlush();  // Flush the OpenGL commands
}


/**
 * @brief 3、颜色渐变图形。绘制一个四边形，四个顶点的颜色分别为红、绿、蓝、黄，实现颜色插值效果。
 * 
 */
void experiment3() {
    glClear(GL_COLOR_BUFFER_BIT);  // Clear the color buffer

    // Draw a quadrilateral with color interpolation
    glBegin(GL_QUADS);
        glColor3f(1.0f, 0.0f, 0.0f);  // Red
        glVertex2f(-0.5f, -0.5f);     // Bottom left

        glColor3f(0.0f, 1.0f, 0.0f);  // Green
        glVertex2f(0.5f, -0.5f);      // Bottom right

        glColor3f(0.0f, 0.0f, 1.0f);  // Blue
        glVertex2f(0.5f, 0.5f);       // Top right

        glColor3f(1.0f, 1.0f, 0.0f);  // Yellow
        glVertex2f(-0.5f, 0.5f);      // Top left
    glEnd();  // End drawing

    glFlush();  // Flush the OpenGL commands
}

/**
 * @brief 
 * 4、用OPENGL画一个房子（包含房顶和窗户）。
 * 
 */
void experiment4() {
    glClear(GL_COLOR_BUFFER_BIT);  // Clear the color buffer

    // Draw the house base
    glColor3f(0.8f, 0.5f, 0.2f);  // Brown color
    glBegin(GL_QUADS);
        glVertex2f(-0.5f, -0.5f);  // Bottom left
        glVertex2f(0.5f, -0.5f);   // Bottom right
        glVertex2f(0.5f, 0.5f);    // Top right
        glVertex2f(-0.5f, 0.5f);   // Top left
    glEnd();  // End drawing

    // Draw the roof
    glColor3f(1.0f, 0.0f, 0.0f);  // Red color
    glBegin(GL_TRIANGLES);
        glVertex2f(-0.6f, 0.5f);   // Left vertex
        glVertex2f(0.6f, 0.5f);    // Right vertex
        glVertex2f(0.0f, 1.0f);     // Top vertex
    glEnd();  // End drawing

    // Draw the window
    glColor3f(1.0f, 1.0f, 1.0f);  // White color
    glBegin(GL_QUADS);
        glVertex2f(-0.2f, -0.2f);   // Bottom left
        glVertex2f(0.2f, -0.2f);     // Bottom right
        glVertex2f(0.2f, 0.2f);      // Top right
        glVertex2f(-0.2f, 0.2f);     // Top left
    glEnd();  // End drawing

    glFlush();  // Flush the OpenGL commands
}

/**
 * @brief
 * 5、用OPENGL画一个太阳和人。
 */
// 绘制圆形
void drawCircle(float x, float y, float radius) {
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(x, y); // 圆心
    for (int i = 0; i <= 100; i++) {
        float angle = 2.0f * M_PI * i / 100;
        float dx = radius * cos(angle);
        float dy = radius * sin(angle);
        glVertex2f(x + dx, y + dy);
    }
    glEnd();
}

// 绘制太阳
void drawSun() {
    glColor3f(1.0f, 1.0f, 0.0f); // 黄色
    drawCircle(0.5f, 0.8f, 0.1f); // 太阳圆心

    // 绘制太阳光芒
    glBegin(GL_LINES);
    for (int i = 0; i < 12; i++) {
        float angle = 2.0f * M_PI * i / 12;
        float x1 = 0.5f + 0.1f * cos(angle);
        float y1 = 0.8f + 0.1f * sin(angle);
        float x2 = 0.5f + 0.15f * cos(angle);
        float y2 = 0.8f + 0.15f * sin(angle);
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }
    glEnd();
}

// 绘制人
void drawPerson() {
    glColor3f(0.0f, 0.0f, 1.0f); // 蓝色
    drawCircle(0.0f, 0.2f, 0.05f); // 头部

    glBegin(GL_LINES);
    // 身体
    glVertex2f(0.0f, 0.2f);
    glVertex2f(0.0f, 0.0f);

    // 左臂
    glVertex2f(0.0f, 0.15f);
    glVertex2f(-0.1f, 0.05f);

    // 右臂
    glVertex2f(0.0f, 0.15f);
    glVertex2f(0.1f, 0.05f);

    // 左腿
    glVertex2f(0.0f, 0.0f);
    glVertex2f(-0.05f, -0.1f);

    // 右腿
    glVertex2f(0.0f, 0.0f);
    glVertex2f(0.05f, -0.1f);
    glEnd();
}

// 显示回调函数
void experiment5() {
    glClear(GL_COLOR_BUFFER_BIT);

    drawSun();    // 绘制太阳
    drawPerson(); // 绘制人

    glFlush();
}
