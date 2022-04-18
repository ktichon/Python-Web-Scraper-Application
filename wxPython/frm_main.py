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
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 744,436 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.lblFirstName = wx.StaticText( self, wx.ID_ANY, u"First Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFirstName.Wrap( -1 )

		bSizer1.Add( self.lblFirstName, 0, wx.ALL, 5 )

		self.txtFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		self.txtFirstName.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.txtFirstName.SetToolTip( u"Enter the first name" )

		bSizer1.Add( self.txtFirstName, 0, wx.ALL, 5 )

		self.lblLastName = wx.StaticText( self, wx.ID_ANY, u"Last Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLastName.Wrap( -1 )

		bSizer1.Add( self.lblLastName, 0, wx.ALL, 5 )

		self.txtLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		self.txtLastName.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.txtLastName.SetToolTip( u"Enter a last name" )

		bSizer1.Add( self.txtLastName, 0, wx.ALL, 5 )

		self.cmdSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.cmdSave, 0, wx.ALL, 5 )

		self.lblResult = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE )
		self.lblResult.Wrap( -1 )

		self.lblResult.SetBackgroundColour( wx.Colour( 234, 238, 11 ) )
		self.lblResult.SetToolTip( u"The mangled text..." )

		bSizer1.Add( self.lblResult, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.cmdSave.Bind( wx.EVT_BUTTON, self.cmdSave_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cmdSave_click( self, event ):
		event.Skip()
