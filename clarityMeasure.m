
function [input1, input2] = clarityMeasure(A, B)

mixFeatureA = calculateSMLFeatureMatrix(A)+ calculateEOLFeatureMatrix(A);
mixFeatureB = calculateSMLFeatureMatrix(B)+ calculateEOLFeatureMatrix(B);

input1 = abs(mixFeatureA);
input2 = abs(mixFeatureB);


end
