import os
import sys

if __name__ == "__main__":
   args = sys.argv
   target = args[1]
   photos_path = os.path.join(target,"photos") 
   print(photos_path)