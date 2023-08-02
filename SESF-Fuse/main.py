import os
from skimage import io
from nets.sesf_net import SESF_Fuse
import glob

def prepare_data(dataset):
    data_dir = os.path.join(os.sep, (os.path.join(os.getcwd(), dataset)))
    data = glob.glob(os.path.join(data_dir, "*.jpg"))
    data.extend(glob.glob(os.path.join(data_dir, "*.bmp")))
    data.sort(key=lambda x: int(x.split('/')[-1].split('.')[0]))
    return data


def main(input_dir, output_dir):
    """
    Image Fusion
    :param input_dir: str, input dir with all images stores in one folder
    :param output_dir: str, output dir with all fused images
    :return:
    """
    sesf = SESF_Fuse("cse")
    data_ir = prepare_data('./data/MFI-WHU/source_1/')
    data_vi = prepare_data('./data/MFI-WHU/source_2/')
    # images_name = sorted(list({item[:-6] for item in os.listdir(input_dir)}))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_name_ir, image_name_vi in zip(data_ir, data_vi):

        img1 = io.imread(image_name_ir)
        img2 = io.imread(image_name_vi)
        fused = sesf.fuse(img1, img2)
        io.imsave(os.path.join(output_dir, image_name_ir.split('/')[-1].split('.')[0] + ".png"), fused)


if __name__ == "__main__":
    input_dir = os.path.join(os.getcwd(), "data", "multi_focus")
    output_dir = os.path.join(os.getcwd(), "data", "result", "SESF-WHU")
    main(input_dir, output_dir)
