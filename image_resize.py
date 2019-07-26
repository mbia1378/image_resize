"""Importer les fonctions système"""
import sys

"""Importer les fonctions OS"""
import os

"""Importer la librairie Image depuis la bibliothèque PIL"""
from PIL import Image

"""Ce paquet fournit une fonction pour facilement redimensionner les images"""
from resizeimage import resizeimage, imageexceptions

"""Le module shutil offre un certain nombre d'opérations de haut niveau sur les fichiers
 et les collections de fichiers. En particulier, des fonctions sont fournies qui prennent en charge la copie"""
from shutil import copyfile

"""Fonction qui récupère le répertoire et la taille"""
def resize(dir, widthStr):

    """concatener le répertoire au mot resized"""
    resizedDir = dir + 'resized/'

    """Caster width en int puis mettre dans width"""
    width = int(widthStr)

    """si le répertoire de destination n'existe pas le créer"""
    if not os.path.exists(resizedDir):
        os.makedirs(resizedDir)

    for filename in os.listdir(dir):
        if filename.endswith(('.JPG', '.jpg', '.JPEG', '.jpeg', '.PNG', '.png', '.GIF', '.gif')):
            print("Resizing {0}...").format(filename)
            with Image.open(dir + filename) as image:
                try:
                    cover = resizeimage.resize_width(image, width)
                    cover.save(resizedDir + filename, image.format)
                except imageexceptions.ImageSizeError as e:
                    copyfile(dir + filename, resizedDir + filename)
                    print (e.message)


if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Bien vouloir vérifier les paramètres (S'assurer d'avoir ajouté la dernière barre oblique. Ex: python image_resize.py c:\image\exemple")
    else:
        resize(sys.argv[1],sys.argv[2])
