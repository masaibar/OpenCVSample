# -*- coding:utf-8 -*-

from PolkaDotsCollage import PolkaDotsCollage

# image_path = "images/lena.png"
IMAGE_PATH = "images/kojiruri.png"

def main():
    mizutama = PolkaDotsCollage(IMAGE_PATH)
    mizutama.exec()


if __name__ == "__main__":
    main()