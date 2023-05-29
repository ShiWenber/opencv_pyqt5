function output = mapto01(input)
    temp = input;
    reshape(temp, 1, numel(temp));
    minval = min(input);
    maxval = max(input);
    output = (input - minval) ./ (maxval - minval);
end