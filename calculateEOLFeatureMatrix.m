% function EOL = Focus_Measure(I)
%     xj = padarray(I,[1 1],'symmetric');
%     EOL = conv2(xj,[-1  -4  -1;-4 20 -4;-1  -4  -1],'valid');
% %     E_2 = EOL.*EOL;
% %     FM = conv2(E_2,ones(8),'valid');
% %     Mp = FM(1:8:end,1:8:end);
% end

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