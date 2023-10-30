# MFIF-DCDTNP

Multi-focus Image Fusion with Parameter Adaptive Dual Channel Dynamic Threshold Neural P Systems  

## Abstract

Multi-focus image fusion (MFIF) aims to merge the focus regions of multiple source images into a single full-focus image. Decision-map methods maximize the preservation of source image information and are therefore widely used for MFIF. Many decision-map methods have been proposed, but they usually face a common problem, i.e., the blurring of the focus and defocus boundary regions easily occurs when generating the decision map. Dynamic threshold neural P (DTNP) systems have spiking and dynamic threshold mechanisms can enhance the detection accuracy of focus and defocus regions. However, DTNP systems are limited to accepting a single external input and require manual parameterization, making them unsuitable for direct use in generating decision maps for image fusion. To address these limitations, we propose variant DTNP systems called parameter adaptive dual channel DTNP (PADCDTNP) systems. The core of the PADCDTNP systems is to generate decision maps with robust boundaries to obtain high-quality fusion results. Note that the PADCDTNP systems parameters are adaptively estimated based on multiple external inputs. Comprehensive experiments on Lytro/MFFW/MFI-WHU dataset show that our method achieves advanced performance and yields comparable results to the eight representative MFIF methods. The code is released on https://github.com/MorvanLi/MFIF-PADCDTNP.



## Note:

We have submitted the article to the IEEE Transactions on Circuits and Systems for Video Technology and will release our source code as soon as the paper is accepted.

