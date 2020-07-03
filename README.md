# AssettoCorsaAutoExtract
Download your favourite mods to your mod folder. The python script will then automatically extract the contents to your Assetto Corsa Content Folder.


1. Download .zip file and extract the contents to your choosen folder OR Clone the Repo

2. Open CMD and naviagte to the folder that you just extracted. ```cd Foldername```

3. Use the command ```pip install -r requirements.txt``` to install all dependencies.

4. Navigate to "C:\Users\USER\AppData\Local\ACPythonScript". In there will be 2 text files, acpath.txt. Change the contents of it to your Assetto Corsa path. ```DEFAULT = "C:\Program Files(x86)\steamapps\common\assettocorsa\content"```

5. There will also be a text file called modpath.txt. This is where you will put your path to your downloaded Mods. Make sure you don't put any other compressed files in here.

6. Run the script by type ```python3 main.py``` into CMD.

7. If you require the ```main.py``` to run at startup then run the file ```runatstartup.py```. This NEEDS to be run as Admin.
  You can do this by running CMD as Admin and navigating to the Python file and running it ```python runatstartup.py```
