function [dst, hist_map] = myHisteq(src)
%myHisteq 自定义的直方均衡法
%   目标分布为平均分布
% 输入src: 原图
% 输出dst: 均衡化后的图，hist_map: src与dst之间的像素映射关系
% hist_map(1)表示的是原图的灰度取值集合，hist_map(2)表示的是均衡化后的图的灰度取值集合
if(size(src, 3) == 3)
    src = im2double(rgb2gray(src));
else
    src = im2double(src);
end
% 获得flag的行数列数便于计算
% reshape将src转化为行向量便于用hist
% 或者使用flag = flag(:)'
[r c] = size(src);
% 获得所有可能的灰度值集合
range = (0:255)./256;
src = reshape(src, 1, r*c);
% 使用hist方法获得src中的元素分布，count记录频数，elem对应灰度，皆为行向量
[counts, elems] = hist(src, unique(src));
hist_map = [elems; counts]';
% 基于第一列中的元素升序排序
hist_map = sortrows(hist_map);
% 频率累计和
sum_old = 0;
to_grays = []; % 记录映射后的灰度列表
for i = 1:length(hist_map)
    elem = hist_map(i,1);
    count = hist_map(i,2);
    sum_old = sum_old + count/sum(hist_map(:, 2));
    temp = find( range < sum_old  );
    %     获得映射后的像素
    to_grays(end + 1) = range(temp(end));
end
map = [elems; to_grays]'; % 获得映射关系
for i = 1:length(elems)
    src(find(src == elems(i))) = to_grays(i);
end
% 灰度映射表
dst = reshape(src, r, c);
end