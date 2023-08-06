# tahoma
This is a very easy API for controlling Somfy Tahoma's devices written in Python3, thanks to the pyoverkiz API.
You just need a three-word input to control a device.



![Somfy](https://www.voletsdusud.com/wp-content/uploads/2018/04/logo-tahoma.jpg)





# Install the main apckage :



Install tahoma :
```python
sudo python3 -m pip install -U
```



# Create a PATH to tahoma :




To be able to run tahoma directly in the terminal, without going to the source package, you should add the tahoma's folder to the PATH :

On Linux, it can be permanently done by executing : `sudo gedit ~/.bashrc` and adding, at the end of the document, this line :

`export PATH=$PATH:/place/of/the/folder/tahoma`



If you want to temporarily test it before, you can just execute this command in the terminal : 

`export PATH=$PATH:/place/of/the/folder/tahoma` 

It will be restored on the next reboot.



By doing this, instead of taping `python3 '/place/of/the/folder/tahoma/tahoma open shuter kitchen'`,

 you will be able to directly tape in the terminal : `tahoma open shuter kitchen`.



The best way is to download the full package and extract it in a foler like $HOME/Tahoma, then create a PATH to this folder and 

voila !

The programme just need two files for working : `tahoma` and `get_devices_url.py`


Then execute tahoma just like this : `tahoma arm alarm garden open shuter kitchen confort heater dining off plug office` and that's all !



# Configure :



It's very easy to configure, there are just two commands to execute once for all

All is explain in tahoma --help and tahoma --info


1. Specify your Somfy-connect login's info and choose the Somfy server :


- `python3 tahoma --config`


2. Configure the API and get the list of your personal Somfy's devices:


- `python3 tahoma --getlist`


3. And now, you are ready to use tahoma :


# Usage : `python3 place\of\Tahoma\foler\tahoma [ACTION] [CATEGORY] [NAME]` (if you don't create a PATH)


For instance : `python3 home/user/Tahoma/tahoma open shutter kitchen activer alarme terrasse`



## Get possible ACTIONS for each CATEGORIES : 


- `python3 tahoma --list-actions`

or

- `python3 tahoma --list-actions-french`
 
 
 
## Get available CATEGORIES :


- `python3 tahoma --list-categories`

or 

- `python3 tahoma --list-categories-french`



## Get the NAMES you have given to your personal devices in the Somfy's App :


- `python3 tahoma --list-names`

or

- `python3 tahoma --list-names-french`



And Enjoy ! 








For :


Somfy Connectivity Kit
Somfy Connexoon IO
Somfy Connexoon RTS
Somfy TaHoma
Somfy TaHoma Beecon
Somfy TaHoma Switch
Thermor Cozytouch
And more...

Supported devices :
Alarm
Shutter
Plug
Heater
and more if you ask me on github : 



















[@pzim-devdata GitHub Pages](https://github.com/pzim-devdata/tahoma/issues)

------------------------------------------------------------------

- [Licence](https://github.com/pzim-devdata/DATA-developer/raw/master/LICENSE)
MIT License Copyright (c) 2023 pzim-devdata

------------------------------------------------------------------

Created by @pzim-devdata - feel free to contact me!
