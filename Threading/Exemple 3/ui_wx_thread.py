from fraMain_wx_thread import fraMain
import wx
import time
from pubsub import pub
from calc_wx_thread import Calc


class UI(fraMain):
    """UI class inherits frMain."""

    def __init__(self, q):
        """Init method."""
        try:
            super().__init__(None)
            self.q = q
            self.myCalc = None
            pub.subscribe(self.update_ui, "UpdateUI")
        except Exception as e:
            print(e)

    def cmdStart_click( self, event ):
        print("Start clicked!")
        self.myCalc = Calc(self.q)
        self.myCalc.start_work()

    def cmdStop_click( self, event ):
        print("Stop clicked!")
        self.myCalc.stop_work()

    def update_ui(self):
        """Update UI widgets from pubsub event."""
        try:
            if not self.q.empty():
                # print("Queue:", self.q.get())
                msg = self.q.get()
                self.lblStatus.SetLabel(str(msg["count"]))
                self.lblNum.SetLabel(str(msg["num"]))
                p = 100 * (1 - (msg["count"] / msg["num"]))
                self.barProgress.SetValue(p)
            
                # for i in range (10000):
                #     x = i ** i
        except Exception as e:
            print(e)