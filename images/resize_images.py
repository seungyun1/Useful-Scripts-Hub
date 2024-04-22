import argparse
import os
import PIL.Image as Image

def main(args):
    input_dir = args['input_dir']
    output_dir = args['output_dir']
    width = args['width']
    height = args['height']

    resize_images(input_dir, output_dir, width, height)


def resize_images(input_dir, output_dir, width, height):
    """Resizes all images in the given input directory and saves them to the output directory.

    Args:
        input_dir: The directory containing the images to be resized.
        output_dir: The directory to save the resized images.
        width: The desired width of the resized images.
        height: The desired height of the resized images.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            image = Image.open(input_path)
            resized_image = image.resize((width, height))
            resized_image.save(output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, help='Input images path', required=True)
    parser.add_argument('--output_dir', type=str, help='Output images path', required=True)
    parser.add_argument('--width', type=int, help='Width of the image being resized', required=True)
    parser.add_argument('--height', type=int, help='Height of the image being resized', required=True)

    main(vars(parser.parse_args()))
