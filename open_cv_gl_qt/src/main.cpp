// #include <GL/freeglut.h>
// #include <cmath>
// #include <corecrt_math_defines.h>
// #include "../include/final.h"

// // Main function
// int main(int argc, char** argv) {
//     // Initialize the GLUT library
//     glutInit(&argc, argv);

//     // Set the initial display mode for double buffering and depth
//     glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

//     // Set the initial window position and size
//     glutInitWindowPosition(100, 100);
//     glutInitWindowSize(800, 600);

//     // Create the window with the title "Crank-Slider Mechanism"
//     glutCreateWindow("Crank-Slider Mechanism");

//     // Initialize OpenGL settings
//     final::initCrankSliderGL();

//     // Register the display callback function
//     glutDisplayFunc(final::crankSliderAnimation);
    
//     // Register mouse and keyboard callbacks
//     glutMouseFunc(final::crankMouse);
//     glutSpecialFunc(final::crankKeyboard);
//     glutKeyboardFunc(final::crankKeyboardRegular);

//     // Enter the GLUT event processing loop
//     glutMainLoop();

//     return 0;
// }