from PIL import Image, ImageDraw, ImageFont


def creat_name(user_name, font_path, output_image):
    # Создание изображения
    image_size = (600, 400)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Загрузка шрифта
    font_size = 48
    font = ImageFont.truetype(font_path, font_size)

    # Определение размеров текста

    text_bbox = draw.textbbox((0, 0), user_name, font=font)
    circle_diameter = text_bbox[2] - text_bbox[1]
    circle_radius = circle_diameter // 2

    # Вычисление координат для центрирования круга и текста
    circle_position = ((image_size[0] - circle_diameter) // 2, (image_size[1] - circle_diameter) // 2)

    # Вычисление координат для центрирования
    text_x = circle_position[0] + circle_radius - (text_bbox[2] - text_bbox[0]) // 2 + 2
    text_y = circle_position[1] + circle_radius - (text_bbox[3] - text_bbox[1]) // 2 + 5  # "+" вниз, "-" вверх
    text_position = (text_x, text_y)

    # Рисование текста
    draw.text(text_position, user_name, font=font, fill="black")

    # Сохранение изображения
    image.save(output_image)

    print("Изображение сохранено как 'output_image.png'")


def creat_name2(user_name, font_path2, output_image):
    image_size = (600, 400)
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    font_size = 48
    font = ImageFont.truetype(font_path2, font_size)

    text_bbox = draw.textbbox((0, 0), user_name, font=font)
    circle_diameter = text_bbox[2] - text_bbox[1]
    circle_radius = circle_diameter // 2

    circle_position = ((image_size[0] - circle_diameter) // 2, (image_size[1] - circle_diameter) // 2)

    text_x = circle_position[0] + circle_radius - (text_bbox[2] - text_bbox[0]) // 2 + 2
    text_y = circle_position[1] + circle_radius - (text_bbox[3] - text_bbox[1]) // 2 - 8
    text_position = (text_x, text_y)

    draw.text(text_position, user_name, font=font, fill="black")

    image.save(output_image)

    print("Изображение сохранено как 'output_image.png'")
