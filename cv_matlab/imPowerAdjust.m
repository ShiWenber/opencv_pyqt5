function dst = imPowerAdjust(src, lambda, power)
%UNTITLED3 此处提供此函数的摘要
%   此处提供详细说明
if(size(src, 3) == 3)
    src = im2double(rgb2gray(src));
else
    src = im2double(src);
end
dst = lambda.*(src.^power);
end