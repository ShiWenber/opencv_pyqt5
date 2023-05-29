function output = hblpf(input, D0, n, tag)
%hblpf - 巴特沃斯高/低通滤波器
%
% Syntax: output = hblpf(input)
%
% Long description
    [M, N] = size(input);
    output = zeros(M, N);
    for u = 1:M
        for v = 1:N
            D = sqrt((u - M / 2)^2 + (v - N / 2)^2);
            if tag == 0
                output(u, v) = 1 / (1 + (sqrt(2) - 1) * (D0 / D)^(2 * n));
            else
                output(u, v) = 1 / (1 + (sqrt(2) - 1) * (D / D0)^(2 * n));
            end
        end
    end
end