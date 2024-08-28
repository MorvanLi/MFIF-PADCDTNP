    
function FDM = consistencyVerification(decisionMap, img1_gray, img2_gray)
    [hei, wid] = size(img1_gray);
    ratio=0.01; %it could be mannually adjusted according to the characteristic of source images
    area=ceil(ratio*hei*wid);
    tempMap1=bwareaopen(decisionMap,area);
    tempMap2=1-tempMap1;
    tempMap3=bwareaopen(tempMap2,area);
    decisionMap=1-tempMap3;
    imgf_gray=img1_gray.*decisionMap+img2_gray.*(1-decisionMap);
    decisionMap = guidedfilter(imgf_gray,decisionMap,3,0.1);
    FDM = decisionMap;
end

