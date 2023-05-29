function [h] = genlaplacian(n)
%genlaplacian 产生任一奇数尺寸n的整数拉普拉斯算子
h = ones(n,n);
% 中心位置特殊取值,因为matlab以1开始，所以上取整
h(ceil(n/2), ceil(n/2)) = -(n^2 -1);
end