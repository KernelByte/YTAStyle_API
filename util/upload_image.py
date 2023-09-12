from os import getcwd
import os
from PIL import Image
from fastapi import  UploadFile, File, BackgroundTasks

PATH_FILES = getcwd() + "/image/"

async def upload_file(background_task : BackgroundTasks, file:UploadFile = File(...)): 
      #SAVE FILE ORIGINAL
      with open(PATH_FILES + file.filename, "wb") as myfile:
         content = await file.read()
         myfile.write(content)
         myfile.close()
      
      background_task.add_task(resize_image,filename=file.filename)

      # Genera un nombre de archivo único para la imagen
      image_extension = file.filename.split(".")[-1]
      image_name = f"{file.filename}_image.{image_extension}"
      image_path = os.path.join(PATH_FILES, image_name)

      
      return image_path


def resize_image(filename: str):
   sizes = [
      {
            "width": 640,
            "heigth": 480
      }
   ]

   for size in sizes:
      size_define = size["width"], size["heigth"]
      image = Image.open(PATH_FILES + filename, mode="r")
      image.thumbnail(size_define)
      image.save(PATH_FILES + str(size["heigth"])+"_"+filename)