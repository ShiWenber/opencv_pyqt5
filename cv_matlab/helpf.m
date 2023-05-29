function output = helpf(input, D0, n, tag)
%hglpf - 指数高/低通滤波器
%
% Syntax: output = hglpf(input,D0,n,tag )
%
% Long description
[M, N] = size(input);
output = zeros(M, N);
for u = 1:M
    for v = 1:N
        D = sqrt((u - M/2)^2 + (v - N/2)^2);
        if tag == 0
            output(u, v) = exp(-(D0/D)^n / sqrt(2));
        else
            output(u,v) = exp(-(D/D0)^n / sqrt(2));
        end
    end
end
end