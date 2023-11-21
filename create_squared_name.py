from create_name_circle import *
from PIL import Image, ImageDraw, ImageFont


class FontCreation2(FontCreation):
    def name_square(self):
        image_size = (600, 400)
        background_color = (255, 255, 255)

        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)

        font_size = 48
        font = ImageFont.truetype(font_path, font_size)

        text_bbox = draw.textbbox((0, 0), self.user_name, font=font)
        square_diameter = text_bbox[2] - text_bbox[0] + 4  # Размер квадрата
        square_radius = square_diameter // 2

        square_position = ((image_size[0] - square_diameter) // 2, (image_size[1] - square_diameter) // 2)

        draw.rectangle(
            (square_position[0], square_position[1], square_position[0] + square_diameter,
             square_position[1] + square_diameter),
            outline="black",
            width=5,
        )

        text_x = square_position[0] + square_radius - (text_bbox[2] - text_bbox[0]) // 2 + 1
        text_y = square_position[1] + square_radius - (text_bbox[3] - text_bbox[1]) // 2 + 3
        text_position = (text_x, text_y)

        draw.text(text_position, self.user_name, font=font, fill="black")

        image.save(output_image3, quality=99)  # Качество 95%

        print(f"Изображение сохранено как {output_image3}")


    def name_square2(self):
        image_size = (600, 400)
        background_color = (255, 255, 255)

        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)

        font_size = 48
        font = ImageFont.truetype(font_path2, font_size)

        text_bbox = draw.textbbox((0, 0), self.user_name, font=font)
        square_diameter = text_bbox[2] - text_bbox[0] + 4  # Размер квадрата
        square_radius = square_diameter // 2

        square_position = ((image_size[0] - square_diameter) // 2, (image_size[1] - square_diameter) // 2)

        draw.rectangle(
            (square_position[0], square_position[1], square_position[0] + square_diameter,
             square_position[1] + square_diameter),
            outline="black",
            width=5,
        )

        text_x = square_position[0] + square_radius - (text_bbox[2] - text_bbox[0]) // 2 + 1
        text_y = square_position[1] + square_radius - (text_bbox[3] - text_bbox[1]) // 2 - 12
        text_position = (text_x, text_y)

        draw.text(text_position, self.user_name, font=font, fill="black")

        image.save(output_image3, quality=99)

        print(f"Изображение сохранено как {output_image3}")


