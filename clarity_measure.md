```matlab
计算空间频率

SF= \sqrt{(RF)^2+(CF)^2} 

 RF=\sqrt{\frac{1}{M*N}\sum_{x=1}^{M} \sum_{y=2}^{N}[f(x,y)-f(x,y-1)]^2 } 

CF=\sqrt{\frac{1}{M*N}\sum_{x=2}^{M} \sum_{y=1}^{N}[f(x,y)-f(x-1,y)]^2 } 

function SF= calculateSFFeatureMatrix(f)
    [M, N] = size(f);
    
    % Initialize matrices
    RF = zeros(M, N);
    CF = zeros(M, N);
    SF = zeros(M, N);
    
    % Calculate RF
    for x = 1:M
        for y = 2:N
            RF(x, y) = (f(x, y) - f(x, y-1))^2;
        end
    end
    RF = sqrt(sum(RF(:)) / (M * N));
    
    % Calculate CF
    for x = 2:M
        for y = 1:N
            CF(x, y) = (f(x, y) - f(x-1, y))^2;
        end
    end
    CF = sqrt(sum(CF(:)) / (M * N));
    
    % Calculate SF
    for x = 1:M
        for y = 1:N
            SF(x, y) = sqrt(RF^2 + CF^2);
        end
    end
end
```





```matlab
EOL=\sum_{x}^{}\sum_{y}^{}(f_{xx}+f_{yy})^2  

(f_{xx}+f_{yy})=-f(x-1,y-1)-4f(x-1,y)-f(x-1,y+1)-4f(x,y-1)+20f(x,y)-4f(x,y+1)-f(x+1,y-1)-4f(x+1,y)-f(x+1,y+1)

function EOL = calculateEOLFeatureMatrix(f)
    [M, N] = size(f);
    
    % Initialize matrix
    EOL = zeros(M, N);
    
    % Calculate EOL
    for x = 2:M-1
        for y = 2:N-1
            f_xx_yy = -f(x-1, y-1) - 4*f(x-1, y) - f(x-1, y+1) - 4*f(x, y-1) + 20*f(x, y) - 4*f(x, y+1) - f(x+1, y-1) - 4*f(x+1, y) - f(x+1, y+1);
            EOL(x, y) = (f_xx_yy)^2;
        end
    end
    
    % Normalize EOL values
    EOL = EOL / max(EOL(:));
end

```





```matlab
function EOG = calculateEOG(f)
    [rows, cols] = size(f);
    EOG = zeros(rows, cols);
    
    for x = 1:rows-1
        for y = 1:cols-1
            fx = f(x+1, y) - f(x, y);
            fy = f(x, y+1) - f(x, y);
            EOG(x, y) = fx^2 + fy^2;
        end
    end
end

```





