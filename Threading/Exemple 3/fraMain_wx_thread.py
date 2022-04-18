# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class fraMain
###########################################################################

class fraMain ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.lblStatus = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.lblStatus.Wrap( -1 )

        bSizer1.Add( self.lblStatus, 0, wx.ALL|wx.EXPAND, 5 )

        self.lblNum = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.lblNum.Wrap( -1 )

        bSizer1.Add( self.lblNum, 0, wx.ALL|wx.EXPAND, 5 )

        self.cmdStart = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.cmdStart, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.cmdStop = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.cmdStop, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.barProgress = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.barProgress.SetValue( 0 )
        bSizer1.Add( self.barProgress, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.cmdStart.Bind( wx.EVT_BUTTON, self.cmdStart_click )
        self.cmdStop.Bind( wx.EVT_BUTTON, self.cmdStop_click )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def cmdStart_click( self, event ):
        event.Skip()

    def cmdStop_click( self, event ):
        event.Skip()


