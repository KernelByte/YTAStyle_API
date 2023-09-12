from os import getcwd
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
      nombre_archivo : str = PATH_FILES + file.filename
      return nombre_archivo


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