import os
import tkinter as tk

# INIT TK
root = tk.Tk()
root.title('Among Us Mod Manager')
root.geometry('1000x600+50+50')
root.resizable(False, False)
# root.iconbitmap('./assets/pythontutorial.ico')
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)
root.rowconfigure(0, weight=1)

# ENV
mods_path = '/home/corran/.steam/debian-installation/steamapps/common/Among Us TOU/BepInEx/plugins/'
game_executable = ''

# INIT VARIABLES
enabledvariable = tk.StringVar()
disabledvariable = tk.StringVar()

# INIT FUNCTIONS
def getModsList(status):
    files = [f for f in os.listdir(mods_path) if os.path.isfile(os.path.join(mods_path, f))]
    files.sort()
    mods = []

    if status == 'enabled':
        for i in files:
            if i.split('.')[-1] == 'dll':
                mods.append(i)
    elif status == 'disabled':
        for i in files:
            if i.split('.')[-1] == 'disabled':
                mods.append(i)

    return mods

def getFormattedModsList(status):
    files = [f for f in os.listdir(mods_path) if os.path.isfile(os.path.join(mods_path, f))]
    files.sort()
    mods = []

    if status == 'enabled':
        for i in files:
            if i.split('.')[-1] == 'dll':
                mods.append(i.replace('.dll', ''))
    elif status == 'disabled':
        for i in files:
            if i.split('.')[-1] == 'disabled':
                mods.append(i.replace('.disabled', '').replace('.dll', ''))

    return mods

def refreshMods():
    global enabledvariable
    global disabledvariable
    enabledvariable.set(getFormattedModsList('enabled'))
    disabledvariable.set(getFormattedModsList('disabled'))
    print('refreshed mods')
refreshMods()

def enableMod():
    mod = disabledlist.curselection()
    if mod:
        mod_name = getModsList('disabled')[mod[0]]
        old_path = os.path.join(mods_path, mod_name)
        new_path = os.path.join(mods_path, mod_name.replace('.disabled', ''))
        os.rename(old_path, new_path)
        print(f'Enabled {mod_name}')
    else:
        print('No Disabled Mod Selected')
    refreshMods()


def disableMod():
    mod = enabledlist.curselection()
    if mod:
        mod_name = getModsList('enabled')[mod[0]]
        old_path = os.path.join(mods_path, mod_name)
        new_path = os.path.join(mods_path, mod_name+'.disabled')
        os.rename(old_path, new_path)
        print(f'Disabled {mod_name}')
    else:
        print('No Enabled Mod Selected')
    refreshMods()

# TK Enabled Mods
enabledframe = tk.Frame(root, width=400, height=600)
enabledframe.grid(column=0, row=0, padx=0, pady=0, sticky=tk.NS)
enabledlabel = tk.Label(enabledframe, text='Enabled Mods')
enabledlabel.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)
enabledlist = tk.Listbox(enabledframe, listvariable=enabledvariable, height=6)
enabledlist.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.TOP)

# Middle Controls
controlsframe = tk.Frame(root, width=200)
controlsframe.grid(column=1, row=0, padx=0, pady=0, sticky=tk.NS)
controlsenable = tk.Button(controlsframe, text='Enable <', command=enableMod)
controlsenable.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)
controlsdisable = tk.Button(controlsframe, text='> Disable', command=disableMod)
controlsdisable.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)
controlsrefresh = tk.Button(controlsframe, text='Refresh', command=refreshMods)
controlsrefresh.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)

# TK Disabled Mods
disabledframe = tk.Frame(root, width=400)
disabledframe.grid(column=2, row=0, padx=0, pady=0, sticky=tk.NS)
disabledlabel = tk.Label(disabledframe, text='Disabled Mods')
disabledlabel.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)
disabledlist = tk.Listbox(disabledframe, listvariable=disabledvariable, height=6)
disabledlist.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.TOP)

root.mainloop()