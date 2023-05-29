function output = my_imdilate(img, se)
%my_imdilate - imdilate膨胀函数
%
% Syntax: output = my_imdilate(img, se)
%
% 参数说明:
% img: 输入图像
% se: 结构元素
output = img;
for i = 1:size(img, 1)
    for j = 1:size(img, 2)
        if img(i, j) == 1
            % 遍历结构元素，判断是否和图像像素相交，相交就将所有的结构元素覆盖到图像上
            for r = i - floor(size(se, 1) / 2):i + floor(size(se, 1) / 2)
                for c = j - floor(size(se, 2) / 2):j + floor(size(se, 2) / 2)
                    % 判断结构元素是否超出图像范围
                    if r > 0 && r <= size(img, 1) && c > 0 && c <= size(img, 2)
                        if se(r - i + floor(size(se, 1) / 2) + 1, c - j + floor(size(se, 2) / 2) + 1) == 1
                            output(r, c) = 1;
                        end
                    end
                end
            end
        end
    end
end
end