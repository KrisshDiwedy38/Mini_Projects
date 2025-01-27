#File Organizer Create a script that organizes files in a specified directory by moving them into subfolders based on their file extensions. For example, all .jpg files should be moved to a ‘Photos’ folder, .txt files to a ‘Documents’ folder, etc.

import os
import sys
import shutil
class Photos:
   def move_to_photos(images_path, dir_path):
      for image in images_path:

         shutil.move(image,dir_path)
      return "Images added to dir Photos successfully!"

   def create_photos(target):
      #Checking is Photos exists or not, creating a new dir "photos" if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "photos":
               photos_path = os.path.join(target, directory) #Creating path for photos dir
               return photos_path 
      photos_path = os.path.join(target,"photos")
      os.mkdir(photos_path) #Creating photos and returning it's path
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
   def move_to_documents(documents_path, dir_path):
      for files in documents_path:

         shutil.move(files,dir_path)
      return "files added to dir documents successfully!"

   def create_documents(target):
      #Checking is 'documents' exists or not, creating a new dir 'documents' if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "documents":
               documents_path = os.path.join(target, directory) #Creating path for 'documents' dir
               return documents_path 
      documents_path = os.path.join(target,"documents")
      os.mkdir(documents_path) #Creating documents and returning it's path
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
   def move_to_docx(docx_path, dir_path):
         for files in docx_path:

            shutil.move(files,dir_path)
         return "files added to dir docx successfully!"

   def create_docx(target):
      #Checking if 'docx' exists or not, creating a new dir 'docx' if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "docx":
               docx_path = os.path.join(target, directory) #Creating path for 'docx' dir
               return docx_path 
      docx_path = os.path.join(target,"docx")
      os.mkdir(docx_path) #Creating docx and returning it's path
      return docx_path


   def find_docx(target):
      docx_path = []
      #Finding files in target directory
      for root, dirs, files in os.walk(target):
         for file in files:
            if file.endswith(".docx"):
               #Making a list of  paths
               path = os.path.join(target,file)
               docx_path.append(path)
         break
      return docx_path

class PowerPoint:
   def move_to_ppt(ppt_path, dir_path):
         for ppt in ppt_path:

            shutil.move(ppt,dir_path)
         return "Ppt added to dir PowerPoint successfully!"

   def create_ppt(target):
      #Checking if 'powerpoint' exists or not, creating a new dir 'powerpoint' if does not exist
      for root, dirs, files in os.walk(target):
         for directory in dirs:
            if directory.lower() == "powerpoint":
               ppt_path = os.path.join(target, directory) #Creating path for 'powerpoint' dir
               return ppt_path 
      ppt_path = os.path.join(target,"powerpoint")
      os.mkdir(ppt_path) #Creating powerpoint and returning it's path
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
      #Creating dir "photos"
      photos_dir_path = Photos.create_photos(target_dir)
      #Moving images to photos
      print(Photos.move_to_photos(image_paths, photos_dir_path))
   else:
      print("No images in the directory")
   
   #Checking if directory has text files and finding their paths
   documents_paths = TextFile.find_documents(target_dir)
   if documents_paths:
      #Creating dir "documents"
      documents_dir_path = TextFile.create_documents(target_dir)
      #Moving text files to documents
      print(TextFile.move_to_documents(documents_paths, documents_dir_path))
   else:
      print("No text files in the directory")

   #Checking if directory has word docx and finding their paths
   docx_paths = WordDocx.find_docx(target_dir)
   if docx_paths:
      #Creating dir "photos"
      docx_dir_path = WordDocx.create_docx(target_dir)
      #Moving images to photos
      print(WordDocx.move_to_docx(docx_paths, docx_dir_path))
   else:
      print("No Word Docx in the directory")

   #Checking if directory has power points and finding their paths
   ppt_paths = PowerPoint.find_ppt(target_dir)
   if ppt_paths:
      #Creating dir "powerpoint"
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