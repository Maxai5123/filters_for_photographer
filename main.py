from PIL import Image, ImageDraw, ImageOps, ImageFilter
import argparse



def get_black_and_white_image(image):
    black_and_white_photo = image.convert('L')
    black_and_white_photo.save('image/black-and-white-photo.jpg')
    

def get_high_contrast_image(image):
    high_contrast_photo = ImageOps.autocontrast(image, cutoff=6)
    high_contrast_photo.save('image/high-contrast-photo.jpg')


def get_blured_image(image):
    blured_photo = image.filter(ImageFilter.GaussianBlur(radius=2.7))
    blured_photo.save('image/blured-photo.jpg')


def get_median_image(image):
    median_photo = image.filter(ImageFilter.MedianFilter(size=9))
    median_photo.save('image/median-photo.jpg')


def get_framed_image(image):
    width, height = image.size
    
    framed_photo = image.transform((width + 500, height + 500), Image.EXTENT,
                            (-50, -50, width + 50, height + 50), Image.BILINEAR)
    framed_photo.save('image/framed-photo.jpg')



def get_sepia_image(image):
    sepia_r = 112
    sepia_g = 66
    sepia_b = 20
    sepia_photo = Image.new('RGB', image.size)
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x,y)):
                r, g, b = image.getpixel((x,y))
                new_r = int(r * 0.393 + g * 0.769 + b * 0.189)
                new_g = int(r * 0.349 + g * 0.686 + b * 0.168)
                new_b = int(r * 0.272 + g * 0.534 + b * 0.131)
                sepia_r = min(new_r, 255)
                sepia_g = min(new_g, 255)
                sepia_b = min(new_b, 255)
                sepia_photo.putpixel((x,y), (sepia_r, sepia_g, sepia_b))
            else:
                return print("Сепии не будет")
    sepia_photo.save('image/sepia-photo.jpg')


def main():
    
    # Создаем парсер
    parser = argparse.ArgumentParser(description='Пример использования argparse')
    
    # Добавляем аргументы
    parser.add_argument('-p', '--photo_name', help='Название файла с исходным изображением', default='image/photo.jpg')
    parser.add_argument('--sepia', help='подключение фильтра сепии', action='store_true')
    parser.add_argument('--black_white', help='подключение чёрно-белого фильтра', action='store_true')
    parser.add_argument('--blur', help='подключение заблюренного фильтра', action='store_true')
    parser.add_argument('--frame', help='подключение рамки для фото', action='store_true')
    parser.add_argument('--median', help='подключение мединного фильтра', action='store_true')
    parser.add_argument('--contrast', help='подключение контрастного фильтра', action='store_true')
    
    # Парсим аргументы
    args = parser.parse_args()

    photo = Image.open(args.photo_name)

    if args.sepia:
        get_sepia_image(photo)
    
    if args.black_white:
        get_black_and_white_image(photo)
    
    if args.blur:
        get_blured_image(photo)
    
    if args.frame:
        get_framed_image(photo)
    
    if args.contrast:
        get_high_contrast_image(photo)
    
    if args.median:
        get_median_image(photo)


if __name__ == "__main__":
    main()