function [output] = common(input, D0, n)
%UNTITLED5 此处提供此函数的摘要
%   此处提供详细说明
 
[M, N] = size(input);
output = zeros(M, N);
for u = 1:M
    for v = 1:N
        D = sqrt((u - M/2)^2 + (v - N/2)^2);
        if D <= D0
            output(u, v) = 0;
        end
    end
end

end