function dst = imLinearAdjust(src, a, b, k1, k2, k3)
%imLinearAdjust三段式线性变化
%   输入src: 输入的图片， a: 变换曲线的第一个转折点，b: 变换曲线的第二个转折点
%   k1: 第一段曲线的斜率，k2: 第二段曲线的斜率，k3: 第三段曲线的斜率
if(size(src, 3) == 3)
    src = im2double(rgb2gray(src));
else
    src = im2double(src);
end
x1 = find(0 <= src & src < a );
src(x1) = k1 .* src(x1);
x2 = find(a <= src & src < b);
src(x2) = k2 .* (src(x2)-a) + k1 * a;
x3 = find(b <= src & src <= 1);
src(x3) = k3 .* (src(x3)-b) + k1 * a + k2 * (b - a);
% 用lambda函数写一个循环，同时可以用变长参数列表
dst = src;
end