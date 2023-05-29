function dst = imLinearAdjust_n(src, points, ks)
%imLinearAdjust三段式线性变化
%   输入src: 输入的图片， points: 区间点集，不含0,1
%   ks: 斜率集
if(size(src, 3) == 3)
    src = im2double(rgb2gray(src));
else
    src = im2double(src);
end
x1 = find(0 <= src & src < points(1));
src(x1) = ks(1).*src(x1);
% 每个区间中的y轴变化量，为了保证折线连续
dy = ks(1)*points(1);
for i = 2:length(points)
    x = find(points(i-1) <= src & src < points(i));
    src(x) = ks(i).*(src(x)-points(i-1)) + dy;
    dy = dy + ks(i)*(points(i) - points(i-1));
end
xn = find(points(length(points)) <= src & src <= 1);
src(xn) = ks(length(ks)) .* (src(xn)-points(length(points))) + dy;
% 用lambda函数写一个循环，同时可以用变长参数列表
dst = src;
end