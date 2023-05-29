function [T] = bestT(i)
%bestT 输入一张灰度图，返回最佳阈值
% 基于图像直方图计算最优分割阈值（使用迭代法自适应寻找最优阈值），并根据此阈值对图像进行分割。
if(size(i, 3) == 3)
    i = im2double(rgb2gray(i));
else
    i = im2double(i);
end
% 使用hist函数计算图像直方图
[rows, cols] = size(i);
range = 0:255./255;
% 获得所有可能的灰度值集合
i_temp = reshape(i, 1, rows*cols);
% 使用hist方法获得src中元素分布，count记录频数，elem对应灰度，皆为行向量
[counts, elems] = hist(i_temp, unique(i_temp));
hist_map = [elems;counts]';
% 基于第一列中的元素升序排序
hist_map = sortrows(hist_map);

% 迭代最大次数
M = 100;
% 使用迭代法
% 初始化阈值
T = (min(elems) + max(elems)) /2;
T_old = T;
k = 1;
while T == T_old | k > M
    % 求阈值两边的灰度期望
    N1 = sum(hist_map(hist_map(:,1) < T, 2));
    T1 = sum(hist_map(hist_map(:,1) < T, 1).*hist_map(hist_map(:,1) < T, 2)) / N1;
    N2 = sum(hist_map(hist_map(:,1) > T, 2));
    T2 = sum(hist_map(hist_map(:,1) > T, 1).*hist_map(hist_map(:,1) > T, 2)) / N2;
    % 记录上一次迭代的阈值
    T_old = T;
    % 求解新的阈值
    T = (T1 + T2) / 2;   
    k = k + 1;
end
end