from PIL import Image, ImageDraw, ImageFont


font_path = "Nautilus.otf"
font_path2 = "Lobster.ttf"

output_image = "output_image.png"
output_image2 = "output_image2.png"
output_image3 = "output_image3.png"


class FontCreation:

    def __init__(self, user_name, font_path, output_image):
        self.user_name = user_name
        self.font_path = font_path
        self.output_image = output_image

    def create_name_engraving(self):
        image_size = (600, 400)
        background_color = (255, 255, 255)

        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)

        font_size = 48
        font = ImageFont.truetype(font_path, font_size)

        text_bbox = draw.textbbox((0, 0), self.user_name, font=font)
        circle_diameter = text_bbox[2] - text_bbox[1] + 2  # Добавляем 2 пикселя слева и справа для отступов
        circle_radius = circle_diameter // 2

        circle_position = ((image_size[0] - circle_diameter) // 2, (image_size[1] - circle_diameter) // 2)

        draw.ellipse(
            (circle_position[0], circle_position[1], circle_position[0] + circle_diameter,
             circle_position[1] + circle_diameter),
            outline="black",
            width=5,
        )

        text_x = circle_position[0] + circle_radius - (text_bbox[2] - text_bbox[0]) // 2 + 2
        text_y = circle_position[1] + circle_radius - (text_bbox[3] - text_bbox[1]) // 2 + 5  # "+" вниз, "-" вверх
        text_position = (text_x, text_y)

        draw.text(text_position, self.user_name, font=font, fill="black")

        image.save(output_image2, quality=99)

        print("Изображение сохранено как output_image.png")

    def create_name_engraving2(self):
        image_size = (600, 400)
        background_color = (255, 255, 255)

        image = Image.new("RGB", image_size, background_color)
        draw = ImageDraw.Draw(image)

        font_size = 48
        font = ImageFont.truetype(font_path, font_size)

        text_bbox = draw.textbbox((0, 0), self.user_name, font=font)
        circle_diameter = text_bbox[2] - text_bbox[0] + 2
        circle_radius = circle_diameter // 2

        circle_position = ((image_size[0] - circle_diameter) // 2, (image_size[1] - circle_diameter) // 2)

        draw.ellipse(
            (circle_position[0], circle_position[1], circle_position[0] + circle_diameter,
             circle_position[1] + circle_diameter),
            outline="black",
            width=5,
        )

        text_x = circle_position[0] + circle_radius - (text_bbox[2] - text_bbox[0]) // 2
        text_y = circle_position[1] + circle_radius - (text_bbox[3] - text_bbox[1]) // 2 + 5
        text_position = (text_x, text_y)

        draw.text(text_position, self.user_name, font=font, fill="black")

        image.save(output_image2, quality=95)

        print("Изображение сохранено как output_image.png")
