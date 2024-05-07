from PIL import Image

def crop_to_16_9(image_path):
    # Rasmni ochish
    img = Image.open(image_path)

    # Asl rasmning kengligi va balandligi
    width, height = img.size

    # Ma'lum bir kenglikdagi 16:9 nisbatni olish
    aspect_ratio = 16 / 9
    new_height = int(width / aspect_ratio)  # Yangi balandlikni hisoblash

    # Agar asl balandlik yangi balandlikdan katta bo'lsa, qirqishni amalga oshirish
    if height > new_height:
        # Markazdan qirqish uchun koordinatalarni olish
        left = 0
        top = (height - new_height) / 2
        right = width
        bottom = top + new_height

        # Rasmni qirqish
        img = img.crop((left, top, right, bottom))

    # Rasmni saqlash
    img.save(image_path)
