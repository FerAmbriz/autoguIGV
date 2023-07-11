# autoguIGV

<p align="center">
  <img src="https://github.com/FerAmbriz/autoguIGV/blob/main/Example.gif" height="auto">
</p>

autoguIGV is a script that automates interaction with IGV to search specific sample sites using the python pyautogui library.
## Dependencies
* IGV
* pyautogui

## Usage
To use it is important to understand the characteristics of the system, such as the size of the screen, the management of virtual desktops and basic knowledge of python, because the autoguIGV script is a roadmap that each user must adapt to the conditions and use of their computer. . In this case, it was developed for a computer with ubuntu 22.04 and bspwm as a window manager in a 1920 x 1080 resolution with a keyboard configured in US English and the configuration of keyboard shortcuts:

* Open a terminal ("win", "enter")
* Switch desktops ("win", "num")
* Send a window to another desktop ("win", "shift", "num")
* Open rofi ("win", "d")

Therefore, if this configuration is not used, you have to change the keyboard shortcuts of the computer system by modifying the file "autoguIGV_bspwm.py" in the corresponding line.
Subsequently, to run the program, the script must be modified to call the corresponding functions for each sample in each site

```
insert_track('/home/fer/Downloads/Bam/UEB_80.tumor.recal.reads.bam')
sites = ['chr17:7,578,083', 'chr17:7,579,621', 'chr17:7,579,647']
search_sites(sites)
remove_track()
```

Finally, once the corresponding modifications have been made, run the script with:
```
python autoguIGV_bspwm.py
```
