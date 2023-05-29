function [output] = inRange(hsv, lower, upper)
%UNTITLED2 此处提供此函数的摘要
%   此处提供详细说明
    if all(hsv <= upper) && all(hsv >= lower)
        output = [1, 1, 1]
    else
        output = [0, 0, 0]
    end