import glob
from PIL import Image


class GIFConvertor:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        GIF Convertor Constructor
        :param path_in: Original Image Path (Ex. images/*.png)
        :param path_out: Output Image Path (Ex. output/filename.png)
        :param resize: Resizing Size (default 320 x 240)
        """
        self.path_in = path_in or './*.png'
        self.path_out = path_out or './output.gif'
        self.resize = resize

    def convert_gif(self):
        """
        Convert Images into a GIF file
        :return: gif image file
        """
        print(self.path_in, self.path_out, self.resize)
        img, *images = [Image.open(f).resize(self.resize, Image.LANCZOS) for f in sorted(glob.glob(self.path_in))]

        try:
            img.save(
                fp=self.path_out,
                format='GIF',
                append_images=images,
                save_all=True,
                duration=500,
                loop=0
            )
        except IOError:
            print("IOError: Unable to convert the find or open images -", img)


if __name__ == '__main__':
    # class test
    c = GIFConvertor("../../support/images/*.png", "../../support/image_out/result.gif")
    c.convert_gif()
    print(GIFConvertor.convert_gif.__doc__)