'''mport tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = filedialog.askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print(filename)'''
import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
dlg = wx.FileDialog(frame, "Choose a file", wildcard="*.*", style=wx.FD_OPEN)
if dlg.ShowModal() == wx.ID_OK:
    filename = dlg.GetPath()
    print(f"You selected: {filename}")
dlg.Destroy()
