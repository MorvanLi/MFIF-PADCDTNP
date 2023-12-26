## Title

Multi-focus Image Fusion with Parameter Adaptive Dual Channel Dynamic Threshold Neural P Systems  

## Abstract

Multi-focus image fusion (MFIF) aims to merge the focus regions of multiple source images into a single full-focus image. Decision-map methods maximize the preservation of source image information and are therefore widely used for MFIF. Many decision-map methods have been proposed, but they usually face a common problem, i.e., the blurring of the focus and defocus boundary regions easily occurs when generating the decision map. Dynamic threshold neural P (DTNP) systems embedded with spiking and dynamic threshold mechanisms are capable of effectively detecting focus and defocus regions, which can be used as a new approach for generating decision maps. However, original DTNP systems require manual configuration of parameters and are also limited to a single external input. Therefore, it is not suitable to be used directly for generating high-precision decision maps. To address these limitations, we propose variant DTNP systems called parameter adaptive dual channel DTNP (PADCDTNP) systems. The core of PADCDTNP systems is to generate decision maps with robust boundaries to obtain high-quality fusion results. Note that PADCDTNP systems parameters are adaptively estimated based on multiple external inputs. Comprehensive experiments on the Lytro/MFFW/MFI-WHU dataset show that our method achieves advanced performance and yields comparable results to the twelve representative MFIF methods. The code for both the proposed method and the comparison methods is released at https://github.com/MorvanLi/MFIF-PADCDTNP.



## Note:

All comparison methods in the [experiments branch](https://github.com/MorvanLi/MFIF-PADCDTNP/tree/experiments)

