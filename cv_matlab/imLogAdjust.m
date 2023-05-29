function dst = imLogAdjust(src,lambda,base)
%imLogAdjust 输入255范围值的图像，输出归一化并进行了对数变换的double类型的图像
%   此处提供详细说明
if(size(src, 3) == 3)
    src = im2double(rgb2gray(src));
else
    src = im2double(src);
end
% 换底公式来表示各种对数，对数内+1使得结果偏移到正数范围
dst = lambda.*log(1 + src)./log(base);
end