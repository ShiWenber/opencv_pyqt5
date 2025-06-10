#include "../include/final.h"
#include <cstdio>
#include <corecrt_math_defines.h>
#include <cmath>
#include <GL/freeglut.h>
#include <GL/glu.h>

namespace final {

// 自行车动画全局变量
static float wheelRotation = 0.0f;               // 车轮旋转角度
static float bicyclePosition = -5.0f;            // 自行车位置
static int animationSpeed = 50;                  // 动画速度 (毫秒)
static bool wireframe = false;                   // 是否线框模式
static int mainMenu, speedSubMenu, fillSubMenu;  // 菜单ID

// 初始化自行车动画OpenGL设置
void initBicycleGL() {
  glClearColor(1.0f, 0.8f, 1.0f, 1.0f);  // 天蓝色背景
  glEnable(GL_DEPTH_TEST);
  glEnable(GL_LINE_SMOOTH);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  glLineWidth(2.0f);
}

// 绘制车轮
void drawWheel(float radius, bool filled) {
  const int segments = 32;
  const float angleStep = 2.0f * M_PI / segments;

  if (wireframe || !filled) {
    // 车轮外圈
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < segments; i++) {
      float angle = i * angleStep;
      glVertex2f(radius * cos(angle), radius * sin(angle));
    }
    glEnd();

    // 车轮辐条
    glBegin(GL_LINES);
    for (int i = 0; i < 8; i++) {
      float angle = i * M_PI / 4.0f + wheelRotation * M_PI / 180.0f;
      glVertex2f(0.0f, 0.0f);
      glVertex2f(radius * 0.8f * cos(angle), radius * 0.8f * sin(angle));
    }
    glEnd();
  } else {
    // 填充车轮
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(0.0f, 0.0f);
    for (int i = 0; i <= segments; i++) {
      float angle = i * angleStep;
      glVertex2f(radius * cos(angle), radius * sin(angle));
    }
    glEnd();

    // 车轮边缘
    glColor3f(0.2f, 0.2f, 0.2f);
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < segments; i++) {
      float angle = i * angleStep;
      glVertex2f(radius * cos(angle), radius * sin(angle));
    }
    glEnd();
  }
}

// 绘制自行车车架
void drawFrame() {
  glColor3f(0.8f, 0.0f, 0.0f);  // 红色车架
  glLineWidth(4.0f);

  if (wireframe) {
    glBegin(GL_LINES);
  } else {
    glBegin(GL_LINES);
  }

  // 主车架 - 三角形结构
  // 底部横梁
  glVertex2f(-1.5f, 0.0f);  // 后轮中心
  glVertex2f(1.5f, 0.0f);   // 前轮中心

  // 座管
  glVertex2f(-1.0f, 0.0f);  // 底部
  glVertex2f(-1.2f, 1.0f);  // 座椅位置

  // 头管
  glVertex2f(1.2f, 0.0f);  // 底部
  glVertex2f(1.0f, 0.8f);  // 把手位置

  // 上管
  glVertex2f(-1.2f, 1.0f);  // 座椅
  glVertex2f(1.0f, 0.8f);   // 把手

  // 下管
  glVertex2f(-1.0f, 0.0f);  // 后轮
  glVertex2f(1.0f, 0.8f);   // 把手

  glEnd();

  // 绘制座椅
  glColor3f(0.4f, 0.2f, 0.0f);  // 棕色座椅
  glLineWidth(6.0f);
  glBegin(GL_LINES);
  glVertex2f(-1.4f, 1.0f);
  glVertex2f(-1.0f, 1.0f);
  glEnd();

  // 绘制把手
  glColor3f(0.3f, 0.3f, 0.3f);  // 灰色把手
  glLineWidth(4.0f);
  glBegin(GL_LINES);
  glVertex2f(0.8f, 0.8f);
  glVertex2f(1.2f, 0.8f);
  glEnd();

  glLineWidth(2.0f);  // 恢复默认线宽
}

// 绘制完整的自行车
void drawBicycle() {
  glPushMatrix();

  // 移动自行车到当前位置
  glTranslatef(bicyclePosition, 0.0f, 0.0f);

  // 绘制车架
  drawFrame();

  // 绘制后轮
  glPushMatrix();
  glTranslatef(-1.5f, 0.0f, 0.0f);
  glRotatef(wheelRotation, 0.0f, 0.0f, 1.0f);
  glColor3f(0.2f, 0.2f, 0.2f);  // 深灰色轮胎
  drawWheel(0.5f, true);
  glPopMatrix();

  // 绘制前轮
  glPushMatrix();
  glTranslatef(1.5f, 0.0f, 0.0f);
  glRotatef(wheelRotation, 0.0f, 0.0f, 1.0f);
  glColor3f(0.2f, 0.2f, 0.2f);  // 深灰色轮胎
  drawWheel(0.5f, true);
  glPopMatrix();

  glPopMatrix();
}

// 动画定时器
void timer(int value) {
  // 更新车轮旋转
  wheelRotation += 5.0f;
  if (wheelRotation >= 360.0f) {
    wheelRotation -= 360.0f;
  }

  // 更新自行车位置
  bicyclePosition += 0.05f;
  if (bicyclePosition > 6.0f) {
    bicyclePosition = -6.0f;
  }

  glutPostRedisplay();
  glutTimerFunc(animationSpeed, timer, 0);
}

// 自行车动画主函数
void bicycleAnimation() {
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  // 设置2D正交投影
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(-8.0, 8.0, -4.0, 4.0);

  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();

  // // 绘制地面
  // glColor3f(0.2f, 0.7f, 0.2f);  // 绿色地面
  // glBegin(GL_QUADS);
  // glVertex2f(-8.0f, -2.0f);
  // glVertex2f(8.0f, -2.0f);
  // glVertex2f(8.0f, -1.0f);
  // glVertex2f(-8.0f, -1.0f);
  // glEnd();

  // 绘制道路
  glColor3f(0.3f, 0.3f, 0.3f);  // 灰色道路
  glBegin(GL_QUADS);
  glVertex2f(-8.0f, -1.0f);
  glVertex2f(8.0f, -1.0f);
  glVertex2f(8.0f, -0.5f);
  glVertex2f(-8.0f, -0.5f);
  glEnd();

  // 绘制道路中线
  glColor3f(1.0f, 1.0f, 0.0f);  // 黄色中线
  glLineWidth(2.0f);
  glBegin(GL_LINES);
  for (float x = -8.0f; x < 8.0f; x += 1.0f) {
    glVertex2f(x, -0.75f);
    glVertex2f(x + 0.5f, -0.75f);
  }
  glEnd();

  // 绘制自行车
  drawBicycle();

  glutSwapBuffers();
}

// 鼠标点击处理
void mouse(int button, int state, int x, int y) {
  if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN) {
    glutAttachMenu(GLUT_RIGHT_BUTTON);
  }
}

// 速度子菜单处理
void speedMenu(int value) {
  switch (value) {
    case 1:  // 高速
      animationSpeed = 20;
      break;
    case 2:  // 中速
      animationSpeed = 50;
      break;
    case 3:  // 低速
      animationSpeed = 100;
      break;
  }
}

// 填充模式子菜单处理
void fillMenu(int value) {
  switch (value) {
    case 1:  // 线框图
      wireframe = true;
      break;
    case 2:  // 填充图
      wireframe = false;
      break;
  }
  glutPostRedisplay();
}

// 主菜单处理
void menu(int value) {
  // 主菜单项处理（如果需要的话）
}

// Crank-slider mechanism animation global variables
static float crankAngle = 0.0f;        // Crank rotation angle in degrees
static float crankRadius = 1.5f;       // Crank radius
static float rodLength = 3.0f;         // Connecting rod length
static bool continuousMotion = false;  // Continuous motion flag
static bool clockwise = true;          // Direction of continuous motion
static float animationStep = 5.0f;     // Animation step size
static int crankTimerSpeed = 50;       // Timer speed for continuous motion

// 添加静态变量来存储曲柄端点位置
static CrankEndPoint currentCrankEnd = {0.0f, 0.0f, 0.0f, 1.0f};

// Initialize crank-slider animation OpenGL settings
void initCrankSliderGL() {
  currentCrankEnd.centerX = 0.0f;
  currentCrankEnd.centerY = 2.0f;
  glClearColor(0.0f, 0.2f, 0.5f, 1.0f);  // Blue background
  glEnable(GL_DEPTH_TEST);
  glEnable(GL_LINE_SMOOTH);
  glEnable(GL_BLEND);
  glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
  glLineWidth(2.0f);
  glPointSize(8.0f);
}

// Calculate slider position based on crank angle
float calculateSliderPosition() {
  // 使用存储的端点位置计算
  float crankX = currentCrankEnd.x - currentCrankEnd.centerX;
  float crankY = currentCrankEnd.y - currentCrankEnd.centerY;

  // 检查连杆长度是否足够
  float minRequiredLength = sqrt(crankX * crankX + crankY * crankY);
    if (rodLength < minRequiredLength) {
        // 如果连杆太短，可以：
        // 1. 返回一个错误值
        // 2. 调整连杆长度
        // 3. 打印警告信息
        printf("Warning: Rod length %.2f is too short! Minimum required: %.2f\n", 
               rodLength, minRequiredLength);
        return crankX; // 返回最小可能距离
    }

    // 检查平方根内的值是否为负
    float underRoot = rodLength * rodLength - crankY * crankY;
    if (underRoot < 0) {
        printf("Warning: Invalid geometry configuration!\n");
        return crankX;
    }

  // Using law of cosines to find slider position
  float sliderX = crankX + sqrt(rodLength * rodLength - crankY * crankY);
  return sliderX;
}

// Draw the crank (rotating arm)
void drawCrank() {
    glPushMatrix();
    // Crank center point (pivot)
    glColor3f(1.0f, 1.0f, 1.0f);  // White center point
    glBegin(GL_POINTS);
    // 更新圆心坐标
    
    glVertex2f(currentCrankEnd.centerX, currentCrankEnd.centerY);
    glEnd();

    // Crank arm
    glColor3f(1.0f, 1.0f, 0.0f);  // Yellow crank
    glLineWidth(6.0f);
    glBegin(GL_LINES);
    glVertex2f(currentCrankEnd.centerX, currentCrankEnd.centerY);  // Crank pivot point
    // 计算并存储端点位置
    currentCrankEnd.x = currentCrankEnd.centerX + crankRadius * cos(crankAngle * M_PI / 180.0f);
    currentCrankEnd.y = currentCrankEnd.centerY + crankRadius * sin(crankAngle * M_PI / 180.0f);
    glVertex2f(currentCrankEnd.x, currentCrankEnd.y);
    glEnd();

    // Crank end point (pin)
    glColor3f(0.8f, 0.8f, 0.2f);  // Dark yellow
    glBegin(GL_POINTS);
    glVertex2f(currentCrankEnd.x, currentCrankEnd.y);
    glEnd();

    glPopMatrix();
}

// Draw the connecting rod
void drawConnectingRod() {
    float sliderX = calculateSliderPosition();

    glColor3f(0.0f, 0.8f, 0.0f);  // Green connecting rod
    glLineWidth(4.0f);
    glBegin(GL_LINES);
    glVertex2f(currentCrankEnd.x, currentCrankEnd.y);  // 使用存储的端点位置
    glVertex2f(sliderX, 0.0f);
    glEnd();

    // Rod end points
    glColor3f(0.0f, 0.6f, 0.0f);  // Dark green
    glBegin(GL_POINTS);
    glVertex2f(currentCrankEnd.x, currentCrankEnd.y);
    glVertex2f(sliderX, 0.0f);
    glEnd();
}

// Draw the slider block
void drawSlider() {
  float sliderX = calculateSliderPosition();

  glPushMatrix();
  glTranslatef(sliderX, 0.0f, 0.0f);
  // Slider block
  glColor3f(1.0f, 1.0f, 1.0f);  // White slider
  glBegin(GL_QUADS);
  glVertex2f(-0.3f, -0.4f);
  glVertex2f(0.3f, -0.4f);
  glVertex2f(0.3f, 0.4f);
  glVertex2f(-0.3f, 0.4f);
  glEnd();

  // Slider outline
  glColor3f(0.8f, 0.8f, 0.8f);  // Light gray outline
  glLineWidth(2.0f);
  glBegin(GL_LINE);
  glVertex2f(0.0f, 0.4f);
  glVertex2f(0.0f, -0.4f);
  glEnd();

  glPopMatrix();
}

// Draw the slider track
void drawTrack() {
  glColor3f(1.0f, 1.0f, 0.0f);  // Yellow track
  glLineWidth(3.0f);
  glBegin(GL_LINES);
  glVertex2f(-1.0f, 0.5f);
  glVertex2f(6.0f, 0.5f);
  glVertex2f(-1.0f, -0.5f);
  glVertex2f(6.0f, -0.5f);
  glEnd();

  // Track end caps
  glBegin(GL_LINES);
  glVertex2f(-1.0f, -0.5f);
  glVertex2f(-1.0f, 0.5f);
  glVertex2f(6.0f, -0.5f);
  glVertex2f(6.0f, 0.5f);
  glEnd();
}

// Draw reference grid and axes
void drawGrid() {
  // Draw circular path for crank motion
  glColor3f(1.0f, 1.0f, 1.0f);  // White circular path
  glLineWidth(1.0f);
  glBegin(GL_LINE_LOOP);
  const int segments = 64;
  for (int i = 0; i < segments; i++) {
    float angle = 2.0f * M_PI * i / segments;
    glVertex2f(currentCrankEnd.centerX + crankRadius * cos(angle), currentCrankEnd.centerY + crankRadius * sin(angle));
  }
  glEnd();
  
  // Draw axes (x and y)
  glColor3f(1.0f, 1.0f, 1.0f);  // White axes
  glLineWidth(1.0f);
  glBegin(GL_LINES);
  // X-axis
  glVertex2f(-6.0f, 0.0f);
  glVertex2f(6.0f, 0.0f);
  // Y-axis
  glVertex2f(0.0f, -4.0f);
  glVertex2f(0.0f, 4.0f);
  glEnd();
}

// Crank-slider animation main function
void crankSliderAnimation() {
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

  // Set up 2D orthographic projection
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluOrtho2D(-6.0, 6.0, -4.0, 4.0);

  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
  // Draw grid and axes
  drawGrid();

  // Draw slider track
  drawTrack();

  // Draw mechanism components
  drawCrank();
  drawConnectingRod();
  drawSlider();

  // Draw labels
  glColor3f(1.0f, 1.0f, 1.0f);  // Black text
  glRasterPos2f(-5.5f, 3.5f);
  const char* instructions =
      "Controls: Left Click = Step | Up/Down = Step CW/CCW | Space = "
      "Continuous CW | Enter = Continuous CCW | S = Stop";
  for (const char* c = instructions; *c != '\0'; c++) {
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, *c);
  }

  // Display current angle
  glRasterPos2f(-5.5f, 3.0f);
  char angleText[50];
  snprintf(angleText, sizeof(angleText), "Crank Angle: %.1f degrees",
           crankAngle);
  for (const char* c = angleText; *c != '\0'; c++) {
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, *c);
  }

  glutSwapBuffers();
}

// Timer function for continuous motion
void crankTimer(int value) {
  if (continuousMotion) {
    if (clockwise) {
      crankAngle += animationStep;
    } else {
      crankAngle -= animationStep;
    }

    // Keep angle in 0-360 range
    if (crankAngle >= 360.0f) {
      crankAngle -= 360.0f;
    } else if (crankAngle < 0.0f) {
      crankAngle += 360.0f;
    }

    glutPostRedisplay();
    glutTimerFunc(crankTimerSpeed, crankTimer, 0);
  }
}

// Mouse click handler for crank-slider
void crankMouse(int button, int state, int x, int y) {
  if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
    // Advance one position (clockwise)
    crankAngle += animationStep;
    if (crankAngle >= 360.0f) {
      crankAngle -= 360.0f;
    }
    glutPostRedisplay();
  }
}

// Keyboard handler for crank-slider
void crankKeyboard(int key, int x, int y) {
  switch (key) {
    case GLUT_KEY_UP:
      // Clockwise one step
      crankAngle += animationStep;
      if (crankAngle >= 360.0f) {
        crankAngle -= 360.0f;
      }
      glutPostRedisplay();
      break;

    case GLUT_KEY_DOWN:
      // Counterclockwise one step
      crankAngle -= animationStep;
      if (crankAngle < 0.0f) {
        crankAngle += 360.0f;
      }
      glutPostRedisplay();
      break;
  }
}

// Regular keyboard handler for crank-slider
void crankKeyboardRegular(unsigned char key, int x, int y) {
  switch (key) {
    case ' ':  // Space key - continuous clockwise
      continuousMotion = true;
      clockwise = true;
      glutTimerFunc(crankTimerSpeed, crankTimer, 0);
      break;

    case '\r':  // Enter key - continuous counterclockwise
    case '\n':
      continuousMotion = true;
      clockwise = false;
      glutTimerFunc(crankTimerSpeed, crankTimer, 0);
      break;

    case 's':  // S key - stop motion
    case 'S':
      continuousMotion = false;
      break;

    case 27:  // Escape key - exit
      exit(0);
      break;
  }
}

}  // namespace final
