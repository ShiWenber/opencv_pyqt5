function output = hglpf(input, D0, tag)
%hglpf - 高斯高/低通滤波器
%
% Syntax: output = hglpf(input, D0)
%
% Long description
    [M, N] = size(input);
    output = zeros(M, N);
    H = zeros(M, N);
    for u = 1:M
        for v = 1:N
            D = sqrt((u - M/2)^2 + (v - N/2)^2);
            if tag == 0
                 H(u, v) = exp(-D0^2/(2*D^2));
            else
                H(u, v) = exp(-D^2/(2*D0^2));
            end
        end
    end
    output = H;
end