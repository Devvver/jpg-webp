from PIL import Image
import os

def extract_filenames_and_sizes_from_file(file_path):
    with open(file_path, "r") as file:
        lines = file.read().splitlines()

    filenames_and_sizes = []

    for line in lines:
        filename = os.path.basename(line)
        size_str = filename.split("_")[-1].split(".")[0]
        width, height = map(int, size_str.split("x"))
        filenames_and_sizes.append((filename, width, height))

    return filenames_and_sizes

def generate_resized_webp_image(filename, width, height):
    try:
        # Открываем изображение
        img = Image.open("file.webp")

        # Масштабируем изображение
        img_resized = img.resize((width, height))

        # Сохраняем измененное изображение в формате webp
        img_resized.save(filename, "WEBP")
        print(f"Изображение {filename} успешно создано.")

    except Exception as e:
        print(f"Ошибка при обработке файла {filename}: {e}")

if __name__ == "__main__":
    # Чтение списка имен файлов и их размеров из файла
    filenames_and_sizes = extract_filenames_and_sizes_from_file("link2.txt")

    # Обработка каждого имени файла и его размеров
    for filename, width, height in filenames_and_sizes:
        generate_resized_webp_image(filename, width, height)
