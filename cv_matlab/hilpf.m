function output = hilpf(input, D0, tag)
% input 为输入图像,有模板的理想高/低通滤波器, D0截至频率,tag为0时高通，为1时低通
    [r, c] = size(input);
    h_ilpf = zeros(r, c);
    for i = 1:r
        for j = 1:c
            if sqrt((i - r/2)^2 + (j - c/2)^2) <= D0
                if tag == 0
                    h_ilpf(i, j) = 0;
                else
                    h_ilpf(i, j) = 1;
                end
            else
                if tag == 0
                    h_ilpf(i, j) = 1;
                else
                    h_ilpf(i, j) = 0;
                end
            end
        end
    end 
    output = h_ilpf;
end