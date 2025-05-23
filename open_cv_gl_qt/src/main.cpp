#include <GL/freeglut.h>
#include <cmath>
#include <corecrt_math_defines.h>
#include "task1.h"

// Function to initialize OpenGL settings
void initGL() {
    // Set the background color to black
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
}

// Function to handle the rendering of the scene
void display() {
    // Clear the color buffer
    glClear(GL_COLOR_BUFFER_BIT);

    // Set the drawing color to white
    glColor3f(1.0f, 1.0f, 1.0f);

    // Draw a rectangle
    glBegin(GL_QUADS);
        glVertex2f(-0.5f, -0.5f);
        glVertex2f( 0.5f, -0.5f);
        glVertex2f( 0.5f,  0.5f);
        glVertex2f(-0.5f,  0.5f);
    glEnd();

    // Flush the OpenGL commands and make sure they get rendered
    glFlush();
}

// Main function
int main(int argc, char** argv) {
    // Initialize the GLUT library
    glutInit(&argc, argv);

    // Set the initial display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    // Set the initial window position and size
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(500, 500);

    // Create the window with the title "FreeGLUT Example"
    glutCreateWindow("FreeGLUT Example");

    // Initialize OpenGL settings
    initGL();

    // Register the display callback function
    glutDisplayFunc(experiment5);  // 可以调用任何 experiment 函数

    // Enter the GLUT event processing loop
    glutMainLoop();

    return 0;
}