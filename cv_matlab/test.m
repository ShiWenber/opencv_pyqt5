% 读入一幅灰度图像，使用不同的边缘检测算子（正交梯度， Roberts, Prewitt, Sobel
% 算子）提取图像边缘，建议不要全部使用matlab自带的edge函数，至少自己实现一个边缘检测算子。


% 将读入的图像转化为灰度图
% i = im2double(imread("character.jpg"));
i = im2double(imread("cameraman.tif"));
figure(),imshow(i);

% 正交梯度算子边缘检测
wh = [
    0,0,0;
    -1,1,0;
    0,0,0];
wv = [
    0,-1,0;
    0,1,0;
    0,0,0];
i_h = imfilter(i, wh);
i_v = imfilter(i, wv);
figure(1),subplot(1,2,1),imshow(i_h),title("水平");
subplot(1,2,2),imshow(i_v),title("垂直");


% 正交梯度算子边缘检测（向后差分）
k = 1;
wh = [
    0,0,0;
    -1,1,0;
    0,0,0];
wv = [
    0,-1,0;
    0,1,0;
    0,0,0];
% 正交梯度算子边缘检测（向后差分）
Wx = [0,0,0;
    0,-1,1;
    0,0,0
    ];
Wy = [0,0,0;
    0,-1,0;
    0, 1, 0
    ];
i_h = imfilter(i, k.*wh);
i_v = imfilter(i, k.*wv);
% 梯度合成
i_g = sqrt(i_h.^2 + i_v.^2);
i_h_2 = imfilter(i, k.*Wx);
i_v_2 = imfilter(i, k.*Wy);
% 梯度合成
i_g_2 = sqrt(i_h_2.^2 + i_v_2.^2);
figure(),subplot(2,3,1),imshow(i_h),title("水平向后");
subplot(2,3,2),imshow(i_v),title("垂直向后");
subplot(2,3,3), imshow(i_h_2),title("水平向前");
subplot(2,3,4), imshow(i_v_2),title("垂直向前");
subplot(2,3,5), imshow(i_g),title("向后");
subplot(2,3,6), imshow(i_g_2),title("向前");


% roberts算子边缘检测
wh_roberts = [
    -1,0,0;
    0,1,0;
    0,0,0];
wv_roberts = [
    0,-1,0;
    1,0,0;
    0,0,0];
i_h_roberts = imfilter(i, wh_roberts);
i_v_roberts = imfilter(i, wv_roberts);
% 梯度合成
i_roberts = sqrt(i_h_roberts.^2 + i_v_roberts.^2);
i_roberts_edge = edge(i, "roberts");
figure(),subplot(2,2,1),imshow(i_h_roberts),title("水平roberts");
subplot(2,2,2),imshow(i_v_roberts),title("垂直roberts");
subplot(2,2,3),imshow(i_roberts),title("roberts");
subplot(2,2,4),imshow(i_roberts_edge),title("roberts边缘");

% prewitt算子边缘检测
k = 1/3;
wh_prewitt = [
    -1, 0, 1;
    -1, 0, 1;
    -1, 0, 1];
wv_prewitt = [
    -1, -1, -1;
    0, 0, 0;
    1, 1, 1];
i_h_prewitt = imfilter(i, k*wh_prewitt);
i_v_prewitt = imfilter(i, k*wv_prewitt);
% 梯度合成
i_prewitt = sqrt(i_h_prewitt.^2 + i_v_prewitt.^2);
i_prewitt_edge = edge(i, "prewitt");
figure(),subplot(2,2,1),imshow(i_h_prewitt),title("水平prewitt");
subplot(2,2,2),imshow(i_v_prewitt),title("垂直prewitt");
subplot(2,2,3),imshow(i_prewitt),title("prewitt");
subplot(2,2,4),imshow(i_prewitt_edge),title("prewit边缘");

% sobel算子边缘检测
k = 1/4;
wh_sobel = [
    -1, 0, 1;
    -2, 0, 2;
    -1, 0, 1];
wv_sobel = [
    -1, -2, -1;
    0, 0, 0;
    1, 2, 1];
i_h_sobel = imfilter(i, k*wh_sobel);
i_v_sobel = imfilter(i, k*wv_sobel);
% 梯度合成
i_sobel = sqrt(i_h_sobel.^2 + i_v_sobel.^2);
i_sobel_edge = edge(i, "sobel");
figure(),subplot(2,2,1),imshow(i_h_sobel),title("水平sobel");
subplot(2,2,2),imshow(i_v_sobel),title("垂直sobel");
subplot(2,2,3),imshow(i_sobel),title("sobel");
subplot(2,2,4),imshow(i_sobel_edge),title("sobel边缘");




% 使用8方向 kirsch 方向梯度模板检测图像的边缘方向，将结果在同一窗口中显示。
[rows, cols] = size(i);
k = 1/15;
% 东
h_kirsch_1 = [
    -3, -3, 5;
    -3, 0, 5;
    -3, -3, 5];
% 东北
h_kirsch_2 = [
    -3, 5, 5;
    -3, 0, 5;
    -3, -3, -3];
% 北
h_kirsch_3 = [
    5, 5, 5;
    -3, 0, -3;
    -3, -3, -3];
% 西北
h_kirsch_4 = [
    5, 5, -3;
    5, 0, -3;
    -3, -3, -3];
% 西
h_kirsch_5 = [
    5, -3, -3;
    5, 0, -3;
    5, -3, -3];
% 西南
h_kirsch_6 = [
    -3, -3, -3;
    5, 0, -3;
    5, 5, -3];
% 南
h_kirsch_7 = [
    -3, -3, -3;
    -3, 0, -3;
    5, 5, 5];
% 东南
h_kirsch_8 = [
    -3, -3, -3;
    -3, 0, 5;
    -3, 5, 5];

i_kirsch_1 = imfilter(i, k*h_kirsch_1);
i_kirsch_2 = imfilter(i, k*h_kirsch_2);
i_kirsch_3 = imfilter(i, k*h_kirsch_3);
i_kirsch_4 = imfilter(i, k*h_kirsch_4);
i_kirsch_5 = imfilter(i, k*h_kirsch_5);
i_kirsch_6 = imfilter(i, k*h_kirsch_6);
i_kirsch_7 = imfilter(i, k*h_kirsch_7);
i_kirsch_8 = imfilter(i, k*h_kirsch_8);
figure(),subplot(2,4,1),imshow(i_kirsch_1),title("东");
subplot(2,4,2),imshow(i_kirsch_2),title("东北");
subplot(2,4,3),imshow(i_kirsch_3),title("北");
subplot(2,4,4),imshow(i_kirsch_4),title("西北");
subplot(2,4,5),imshow(i_kirsch_5),title("西");
subplot(2,4,6),imshow(i_kirsch_6),title("西南");
subplot(2,4,7),imshow(i_kirsch_7),title("南");
subplot(2,4,8),imshow(i_kirsch_8),title("东南");
% 以最大梯度作为边缘点强度
for r = 1:rows
    for c = 1:cols
        i_kirsch(r, c) = max([i_kirsch_1(r, c), i_kirsch_2(r, c), i_kirsch_3(r, c), i_kirsch_4(r, c), i_kirsch_5(r, c), i_kirsch_6(r, c), i_kirsch_7(r, c), i_kirsch_8(r, c)]);
    end
end

figure(),imshow(i_kirsch),title("kirsch");

% 基于图像直方图计算最优分割阈值（使用迭代法自适应寻找最优阈值），并根据此阈值对图像进行分割。
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
T = (min(elems) + max(elems)) /2
k = 1
while T == T_old or k > M
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


% 根据阈值对图像进行分割
i_copy = i;
i_copy(i < T) = 0;
i_copy(i >= T) = 255;
figure(),subplot(1,2,1),imshow(i),title("原图");
subplot(1,2,2),imshow(i_copy),title("分割图");
