/**
 * @file mygl.cpp
 * @author ShiWenber (1210169842@qq.com)
 * @brief 
 * @version 0.1
 * @date 2023-03-28
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include "mygl.h"
#include <cmath>

void lineDDA(int x0, int y0, int xEnd, int yEnd) {
  int dx = xEnd - x0, dy = yEnd - y0, steps, k; 
  float xIncrement, yIncrement, x = x0, y=y0;
  
  /**斜率小于1，则选择x作为步长，否则选择y作为步长*/
  if(fabs(dx) >fabs(dy)) {
    steps = fabs(dx);
  } else {
    steps = fabs(dy);
  }
  xIncrement = float(dx) / float(steps);
  yIncrement = float(dy) / float(steps);

  setPixel(round(x), round(y));
  for (k = 0; k < steps; k++) {
    y += xIncrement;
    x += yIncrement; 
    setPixel(round(x), round(y));
  }

}