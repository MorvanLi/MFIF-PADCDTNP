clear all;
close all;
 
%%%% Created by Bo Li <morvanli@stu.xjtu.edu.cn> 2023.6.18

%% parametes settting 
t_max = 110;
datasets = ['Lytro' , 'MFFW', 'MFI-WHU'];

for num =5:5

    path1 = ['./datasets/Lytro/source_1/',num2str(num),'.jpg'];
    path2 = ['./datasets/Lytro/source_2/',num2str(num),'.jpg'];

    img1 = double(imread(path1))/255;
    img2 = double(imread(path2))/255;

    if size(img1,3)>1
        img1_gray=rgb2gray(img1);
        img2_gray=rgb2gray(img2);
    else
        img1_gray=img1;
        img2_gray=img2;
    end


    [input1, input2] = clarityMeasure(img1_gray, img2_gray);          % input1 = SML+EOL(img1_gray), input2 = SML+EOL(img2_gray)
    IDM = PADCDTNP(input1, input2, t_max);                            % PADCDTNP -> get init decision map
    FDM = consistencyVerification(IDM, img1_gray, img2_gray);         % consistency verification -> get final decision map

    if size(img1,3)>1
        FDM=repmat(FDM,[1 1 3]);
    end

    F = img1.*FDM + img2.*(1-FDM);
    F = uint8(F*255);                                                 % fused image F
  
    figure;
    imshow(F, []);

end
