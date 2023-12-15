import os
from threading import Thread

import requests


def thumbnail_images():
    folder_path = "thumb_photos"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 100):
        image_url = f"https://randomuser.me/api/portraits/thumb/men/{i}.jpg"
        image_filename = f"{folder_path}/thumbnails_{i}.jpg"

        try:
            response = requests.get(image_url)
            response.raise_for_status()

            with open(image_filename, "wb") as image_file:
                image_file.write(response.content)
            print(f"{i} rasm saqlandi.")
        except requests.exceptions.RequestException as e:
            print(f"{i} rasmni yuklab bolmadi. Xatolik: {e}")

    print("Barcha rasmlar yuklandi.")


def medium_images():
    folder_path = "medium_photos"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 100):
        image_url = f"https://randomuser.me/api/portraits/med/men/{i}.jpg"
        image_filename = f"{folder_path}/medium_{i}.jpg"

        try:
            response = requests.get(image_url)
            response.raise_for_status()

            with open(image_filename, "wb") as image_file:
                image_file.write(response.content)
            print(f"{i} rasm saqlandi.")
        except requests.exceptions.RequestException as e:
            print(f"{i} rasmni yuklab bolmadi. Xatolik: {e}")

    print("Barcha rasmlar yuklandi.")


def large_images():
    folder_path = "large_photos"
    os.makedirs(folder_path, exist_ok=True)

    for i in range(1, 100):
        image_url = f"https://randomuser.me/api/portraits/men/{i}.jpg"
        image_filename = f"{folder_path}/large_{i}.jpg"

        try:
            response = requests.get(image_url)
            response.raise_for_status()

            with open(image_filename, "wb") as image_file:
                image_file.write(response.content)
            print(f"{i} rasm saqlandi.")
        except requests.exceptions.RequestException as e:
            print(f"{i} rasmni yuklab bolmadi. Xatolik: {e}")

    print("Barcha rasmlar yuklandi.")


if __name__ == '__main__':
    threads = []
    for func in [thumbnail_images, medium_images, large_images]:
        t = Thread(target=func)
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    print("Barcha rasmlar yuklandi.")
