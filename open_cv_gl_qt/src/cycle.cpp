#include <GL/freeglut.h>
#include <cmath>
#include <corecrt_math_defines.h>
#include "../include/final.h"

// Main function
int main(int argc, char** argv) {
    // Initialize the GLUT library
    glutInit(&argc, argv);

    // Set the initial display mode for double buffering and depth
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

    // Set the initial window position and size
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(800, 600);

    // Create the window with the title "Bicycle Animation"
    glutCreateWindow("Bicycle Animation");

    // Initialize OpenGL settings
    final::initBicycleGL();

    // Register the display callback function
    glutDisplayFunc(final::bicycleAnimation);
    
    // Register mouse callback
    glutMouseFunc(final::mouse);
    
    // Create menus
    int speedSubMenu = glutCreateMenu(final::speedMenu);
    glutAddMenuEntry("High Speed", 1);
    glutAddMenuEntry("Medium Speed", 2);
    glutAddMenuEntry("Low Speed", 3);
    
    int fillSubMenu = glutCreateMenu(final::fillMenu);
    glutAddMenuEntry("Wireframe", 1);
    glutAddMenuEntry("Filled", 2);
    
    int mainMenu = glutCreateMenu(final::menu);
    glutAddSubMenu("Speed", speedSubMenu);
    glutAddSubMenu("Fill Mode", fillSubMenu);
    
    glutAttachMenu(GLUT_RIGHT_BUTTON);
    
    // Start the timer
    glutTimerFunc(50, final::timer, 0);

    // Enter the GLUT event processing loop
    glutMainLoop();

    return 0;
}