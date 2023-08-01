import os
from instabot import Bot
username = "theluckygoud"
password = "passward"

Bot.login(username=username, password=password)
# Replace 'path_to_your_image.jpg' with the actual path to your image file
image_path = "black_sunglass.jpg"
caption = ". #yourhashtags"
Bot.upload_photo(image_path, caption=caption)
