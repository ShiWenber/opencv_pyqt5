/**
 * @file main.cpp
 * @author ShiWenber (1210169842@qq.com)
 * @brief 
 * @version 0.1
 * @date 2023-03-28
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include <GL/freeglut.h>
#include "mygl.h"

#include <iostream>
#include <string>
#include <cmath>

void init(void) {
  glMatrixMode(GL_PROJECTION);  //< 指定投影矩阵
  // gluOrtho2D(-1.0, 1.0, -1.0, 1.0); //< 设置正交矩阵投影并指定裁剪范围
  gluOrtho2D(0, 800, 0, 600);  //< 设置正交矩阵投影并指定裁剪范围
}

void myDisplay(void) {
  glClear(GL_COLOR_BUFFER_BIT);       //< 清除颜色缓冲区
  glRectf(-0.5f, -0.5f, 0.5f, 0.5f);  //< 绘制矩形
  glFlush();                          //< 强制执行缓冲区中的OpenGL命令
}

/**
 * @brief 绘制基本图元
 * glBegin支持的方式有
 * GL_POINTS   单个顶点集
 * GL_LINES   多组双顶点线段
 * GL_LINE_STRIP   不闭合折线
 * GL_LINE_LOOP   闭合折线
 * GL_POLYGON   单个简单填充凸多边形
 * GL_QUADS   多组独立填充四边形
 * GL_QUAD_STRIP   连续填充四边形串
 * GL_TRAINGLES   多组独立填充三角形
 * GL_TRAINGLE_STRIP   线型连续填充三角形串
 * GL_TRAINGLE_FAN   扇形连续填充三角形串
 *
 * （1）单个点（100，200）；（GL_POINTS）
 * （2）线段，端点为（0， 0）和（300，100）；（GL_LINES）
 * （3）三角形，端点为（400，300），（600，300）和（500，500）；（GL_LINE_LOOP）
 * （4）填充三角形，端点为（400，50），（600，50）和（500，250）；（GL_POLYGON）
 *
 */
void dis_basic_graph_element(void) {
  glClear(GL_COLOR_BUFFER_BIT);

  //< （1）单个点（100，200）；（GL_POINTS）
  glBegin(GL_POINTS);
  glVertex2f(100, 200);
  glEnd();


  //< （2）线段，端点为（0， 0）和（300，100）；（GL_LINES）
  glBegin(GL_LINES);
  glVertex2f(0, 0);
  glVertex2f(300, 100);
  glEnd();


  //< （3）三角形，端点为（400，300），（600，300）和（500，500）；（GL_LINE_LOOP）
  glBegin(GL_LINE_LOOP);
  glVertex2f(400, 300);
  glVertex2f(600, 300);
  glVertex2f(500, 500);
  glEnd();


  //< （4）填充三角形，端点为（400，50），（600，50）和（500，250）；（GL_POLYGON）
  glBegin(GL_POLYGON);
  glVertex2f(400, 50);
  glVertex2f(600, 50);
  glVertex2f(500, 250);
  glEnd();

  glFlush();
}



void dis_linedda(void) {
  glClear(GL_COLOR_BUFFER_BIT);
  lineDDA(0, 0, 300, 100);
  glFlush();
}

int main(int argc, char *argv[]) {
  /** 对GLUT进行初始化，这个函数必须在其他的GLUT之前调用一次 */
  glutInit(&argc, argv);
  /** rgb表示在颜色缓冲区中使用红、绿、蓝三种颜色，使用INDEX的话为使用索引颜色，double表示使用双缓冲区 */
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
  glutInitWindowPosition(100, 100);
  glutInitWindowSize(800, 600);
  glutCreateWindow("OpenGL");
  init();
  //< 通过命令行参数来设置调用的函数类型
  if (argc > 1) {
    std::string str = argv[1];
    if (str == "demo") {
      glutDisplayFunc(&myDisplay);
      glutMainLoop();  //< 进入GLUT事件处理循环，如果不进入循环，程序会直接结束
    } else if (str == "element") {
      glutDisplayFunc(&dis_basic_graph_element);
      glutMainLoop();
    } else if (str == "linedda") {
      glutDisplayFunc(&dis_linedda);
      glutMainLoop();
    } else {
      std::cout << "参数错误" << std::endl;
    }
  }
  return 0;
}