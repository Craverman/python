import os

dir_path = os.path.join('my_project')
if not os.path.exists(dir_path):
   os.makedirs(dir_path)
os.chdir("my_project")
for el in ['settings', 'mainapp', 'adminapp', 'authapp']:
    if not os.path.exists(el):
        os.mkdir(el)

os.chdir("settings")
for item in  ['prod.py', 'dev.py','__init__.py']:
    f = open (item, "w")
    f.close()
os.chdir("..")

os.chdir("mainapp")
for item in  ['__init__.py', 'models.py', 'views.py']:
    f = open (item, "w")
    f.close()
path = os.path.join("templates", "mainapp")
if not os.path.exists(path):
   os.makedirs(path)
os.chdir("templates")
os.chdir("mainapp")
for item in  ['base.html', 'index.html']:
    f = open (item, "w")
    f.close()

for i in range(3):
    os.chdir("..")

os.chdir("authapp")
for item in  ['__init__.py', 'models.py', 'views.py']:
    f = open (item, "w")
    f.close()
path = os.path.join("templates", "authapp")
if not os.path.exists(path):
   os.makedirs(path)
os.chdir("templates")
os.chdir("authapp")
for item in  ['base.html', 'index.html']:
    f = open (item, "w")
    f.close()