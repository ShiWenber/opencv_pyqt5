#include <iostream>
#include <gtest/gtest.h>

// Function to be tested
int add(int a, int b) {
    return a + b;
}

// Test case for the add function
TEST(AddFunctionTest, PositiveNumbers) {
    EXPECT_EQ(add(1, 2), 3);
    EXPECT_EQ(add(10, 20), 30);
}

TEST(AddFunctionTest, NegativeNumbers) {
    EXPECT_EQ(add(-1, -2), -3);
    EXPECT_EQ(add(-10, -20), -30);
}

TEST(AddFunctionTest, MixedNumbers) {
    EXPECT_EQ(add(-1, 2), 1);
    EXPECT_EQ(add(10, -20), -10);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}