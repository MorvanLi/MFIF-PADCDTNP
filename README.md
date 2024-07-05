## Title

Multi-focus Image Fusion with Parameter Adaptive Dual Channel Dynamic Threshold Neural P Systems  

## Abstract

Multi-focus image fusion (MFIF) is an important technique that aims to combine the focused regions of multiple source images into a fully clear image. Decision-map methods are widely used in MFIF to maximize the preservation of information from the source images. While many decision-map methods have been proposed, they often struggle with inaccuracies in determining focus and non-focus boundaries, further affecting the quality of the fused images. Dynamic threshold neural P (DTNP) systems are computational models inspired by biological spiking neurons, featuring dynamic threshold and spiking mechanisms to better distinguish focused and unfocused regions for decision map generation. However, original DTNP systems require manual parameter configuration and have only one stimulus. Therefore, they are not suitable to be used directly for generating high-precision decision maps. To overcome these limitations, we propose a variant called parameter adaptive dual channel DTNP (PADCDTNP) systems. Inspired by the spiking mechanisms of PADCDTNP systems, we further develop a new MFIF method. As a new neural model, PADCDTNP systems adaptively estimate parameters according to multiple external inputs to produce decision maps with robust boundaries, resulting in high-quality fusion results. Comprehensive experiments on the Lytro/MFFW/MFI-WHU dataset show that our method achieves advanced performance and yields comparable results to the fourteen representative MFIF methods. In addition, compared to the standard DTNP systems, PADCDTNP systems improve the fusion performance and fusion efficiency on the three datasets by 5.69% and 86.03%, respectively. The code for both the proposed method and the comparison methods is released at https://github.com/MorvanLi/MFIF-PADCDTNP.


## Note:

All comparison methods in the [experiments branch](https://github.com/MorvanLi/MFIF-PADCDTNP/tree/experiments)

## Implementation details

{For the image fusion task, PADCDTNP systems use a single-layer network architecture that maintains a one-to-one correspondence between its neurons and the pixels of the input image. PADCDTNP systems are based on iterative computation, and time complexity can be formulated as $O(t_{max} \times m \times n)$, where $m \times n$ represents the total number of neurons in the model, determined by the input image size, and $t_{max}$ denotes the maximum number of iterations, which is set to 110. The proposed fusion method is implemented in Matlab 2023a and on an Intel (R) Xeon (R) Gold 6346 CPU running at 3.1 GHz with 80 GB of RAM. All compared DL-based methods are reproduced on one NVIDIA A100 GPU. We used open-source code and fixed all parameters according to recommendations provided in the relevant publications.