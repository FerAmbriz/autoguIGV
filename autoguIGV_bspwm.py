import pyautogui
import subprocess
import time
#================================ OPEN IGV =============================#
pyautogui.hotkey('win', 'd')
time.sleep(0.5)
pyautogui.write('igv')
pyautogui.press('enter')
time.sleep(20)
pyautogui.hotkey('win', 'shift', '3')
pyautogui.hotkey('win', '3')

#=============================== Inspect sites ==========================#
#ver donde dar click: pyautogui.position(). Point(x=24, y=68)
def insert_track(bam_file):
    pyautogui.moveTo(24, 68)
    pyautogui.click()
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'l')

    #bam_file = '/home/fer/Downloads/Bam/UEB_80.tumor.recal.reads.bam'
    pyautogui.write(bam_file)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

def search_sites (sites):
    pyautogui.moveTo(714, 68)
    pyautogui.click()
    time.sleep(3)

    #sites = ['chr17:7,578,083', 'chr17:7,579,621', 'chr17:7,579,647']
    for i in sites:
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write(i)
        # Presionar Enter para navegar a la página
        pyautogui.press('enter')
        time.sleep(2)

def remove_track():
    pyautogui.moveTo(88, 294)
    pyautogui.click(button='right')
    pyautogui.press('up')
    pyautogui.press('enter')

    pyautogui.moveTo(88, 294)
    pyautogui.click(button='right')
    pyautogui.press('up')
    pyautogui.press('enter')

insert_track('/home/fer/Downloads/Bam/UEB_80.tumor.recal.reads.bam')
sites = ['chr17:7,578,083', 'chr17:7,579,621', 'chr17:7,579,647']
search_sites(sites)
remove_track()
