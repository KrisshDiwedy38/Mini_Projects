#File Organizer Create a script that organizes files in a specified directory by moving them into subfolders based on their file extensions. For example, all .jpg files should be moved to a ‘Photos’ folder, .txt files to a ‘Documents’ folder, etc.

import os
import sys
import shutil
class Photos:
   # Moving image to dir "Photos"
   def move_to_photos(images_path, dir_path):
      for image in images_path:

         shutil.move(image,dir_path)
      return "Images added to dir Images successfully!"

   def create_photos(target):
      #Checking if Photos exists or not, creating a new dir "Images" if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "Images":
               photos_path = os.path.join(target, directory) #Creating path for Images dir
               return photos_path 
      photos_path = os.path.join(target,"Images")
      os.mkdir(photos_path) #Creating Images and returning it's path
      return photos_path


   def find_photos(target):
      photos_path = []
      #Finding images in target directory
      for root, dirs, files in os.walk(target):
         for file in files:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
               #Making a list of image paths
               path = os.path.join(target,file)
               photos_path.append(path)
         break
      return photos_path

class TextFile:
   # Moving files to dir "Documents"
   def move_to_documents(documents_path, dir_path):
      for files in documents_path:

         shutil.move(files,dir_path)
      return "files added to dir Documents successfully!"

   def create_documents(target):
      #Checking if 'Documents' exists or not, creating a new dir 'Documents' if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "Documents":
               documents_path = os.path.join(target, directory) #Creating path for 'Documents' dir
               return documents_path 
      documents_path = os.path.join(target,"Documents")
      os.mkdir(documents_path) #Creating Documents and returning it's path
      return documents_path
   
   def find_documents(target):
      documents_path = []
      #Finding files in target directory
      for root, dirs, files in os.walk(target):
         for file in files:
            if file.endswith(".txt"):
               #Making a list of  paths
               path = os.path.join(target,file)
               documents_path.append(path)
         break
      return documents_path

class WordDocx:
   # Moving files to dir "Docx"
   def move_to_docx(docx_path, dir_path):
         for files in docx_path:

            shutil.move(files,dir_path)
         return "files added to dir docx successfully!"

   def create_docx(target):
      #Checking if 'Docx' exists or not, creating a new dir 'Docx' if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "Docx":
               docx_path = os.path.join(target, directory) #Creating path for 'Docx' dir
               return docx_path 
      docx_path = os.path.join(target,"Docx")
      os.mkdir(docx_path) #Creating Docx and returning it's path
      return docx_path


   def find_docx(target):
      docx_path = []
      #Finding files in target directory
      for root, dirs, files in os.walk(target):
         for file in files:
            if file.endswith(".docx") or file.endswith(".doc"):
               #Making a list of  paths
               path = os.path.join(target,file)
               docx_path.append(path)
         break
      return docx_path

class PowerPoint:
   # Moving files to dir "PowerPoint"
   def move_to_ppt(ppt_path, dir_path):
         for ppt in ppt_path:

            shutil.move(ppt,dir_path)
         return "Ppt added to dir PowerPoint successfully!"

   def create_ppt(target):
      #Checking if 'Powerpoint' exists or not, creating a new dir 'Powerpoint' if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "powerpoint":
               ppt_path = os.path.join(target, directory) #Creating path for 'Powerpoint' dir
               return ppt_path 
      ppt_path = os.path.join(target,"powerpoint")
      os.mkdir(ppt_path) #Creating Powerpoint and returning it's path
      return ppt_path


   def find_ppt(target):
      ppt_path = []
      #Finding ppt in target directory
      for root, dirs, files in os.walk(target):
         for file in files:
            if file.endswith(".pptx") or file.endswith(".ppt"):
               #Making a list of  paths
               path = os.path.join(target,file)
               ppt_path.append(path)
         break
      return ppt_path


def main(target_dir):
   #Checking if directory has images and finding their paths
   image_paths = Photos.find_photos(target_dir)
   if image_paths:
      #Creating dir "Images"
      photos_dir_path = Photos.create_photos(target_dir)
      #Moving images to Images
      print(Photos.move_to_photos(image_paths, photos_dir_path))
   else:
      print("No images in the directory")
   
   #Checking if directory has text files and finding their paths
   documents_paths = TextFile.find_documents(target_dir)
   if documents_paths:
      #Creating dir "Documents"
      documents_dir_path = TextFile.create_documents(target_dir)
      #Moving text files to Documents
      print(TextFile.move_to_documents(documents_paths, documents_dir_path))
   else:
      print("No text files in the directory")

   #Checking if directory has word docx and finding their paths
   docx_paths = WordDocx.find_docx(target_dir)
   if docx_paths:
      #Creating dir "Docx"
      docx_dir_path = WordDocx.create_docx(target_dir)
      #Moving images to Docx
      print(WordDocx.move_to_docx(docx_paths, docx_dir_path))
   else:
      print("No Word Docx in the directory")

   #Checking if directory has power points and finding their paths
   ppt_paths = PowerPoint.find_ppt(target_dir)
   if ppt_paths:
      #Creating dir "Powerpoint"
      ppt_dir_path = PowerPoint.create_ppt(target_dir)
      #Moving ppt to PowerPoint
      print(PowerPoint.move_to_ppt(ppt_paths, ppt_dir_path))
   else:
      print("No power points in the directory")




if __name__ == "__main__":
   args = sys.argv
   if len(args) != 2:
      raise Exception("You must pass the path of target directory - only!")
   target = args[1]
   main(target)