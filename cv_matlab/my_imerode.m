function output = my_imerode(img, se)
%my_imerode - 形态学腐蚀函数
%
% Syntax: output = my_imerode(img, se)
%
% 输入参数:
%   img: 输入图像
%   se: 结构元素
    output = img;
    flag = 1; % 标记是否所有像素点都重合
    for i = 1:size(img, 1)
        for j = 1:size(img, 2)
            if img(i, j) == 1
                % 遍历结构元素，判断是否所有像素点与图像像素点重合
                for r = i - floor(size(se, 1) / 2):i + floor(size(se, 1) / 2)
                    for c = j - floor(size(se, 2) / 2):j + floor(size(se, 2) / 2)
                        % 如果结构元素超出图像范围，则跳过
                        if r < 1 || r > size(img, 1) || c < 1 || c > size(img, 2)
                            continue
                        end
                        % 存在不重合的像素点，则腐蚀后的图像该i,j像素点为0
                        if se(r - i + floor(size(se, 1) / 2) + 1, c - j + floor(size(se, 2) / 2) + 1) == 1 && img(r, c) == 0
                            output(i, j) = 0;
                            flag = 0;
                            break
                        end
                        
                    end
                    % 如果并非所有像素点都重合，则跳出循环
                    if flag == 0
                        flag = 1;
                        break
                    end
                end
                
            end
        end
    end
end