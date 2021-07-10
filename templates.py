import os
from distutils.dir_util import copy_tree
src = 'C:/Users/crave/PycharmProjects/pythonProject1/my_project/mainapp/'
src2 = 'C:/Users/crave/PycharmProjects/pythonProject1/my_project/authapp/'
dest = 'C:/Users/crave/PycharmProjects/pythonProject1/my_project/templates'

dirName = 'my_project/templates'
try:
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
def templates(src, src2, dest):
    copy_tree(src, dest)
    copy_tree(src2, dest)
templates(src, src2, dest)