import wx
from ui_wx_thread import UI
import queue

app = wx.App()

q = queue.Queue()
myUI = UI(q)
myUI.Show()

app.MainLoop()