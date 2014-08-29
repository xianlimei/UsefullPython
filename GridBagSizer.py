#!/usr/bin/python
#-*- coding: gbk -*-
#-------------------------------------------------------------------------------
# Name:        ģ��1
# Purpose:
#
# Author:      ZWW
#
# Created:     25/12/2013
# Copyright:   (c) ZWW 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
class Example(wx.Frame):
    def __init__(self,parent,title):
        super(Example,self).__init__(parent,title=title,size=(320,130))
        self.InitUI()
        self.Centre()
        self.Show()
    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4,4)

        text = wx.StaticText(panel,label='Rename to')
        sizer.Add(text,pos=(0,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=5)

        tc = wx.TextCtrl(panel)
        sizer.Add(tc,pos=(1,0),span=(1,5),flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=5)

        buttonOK = wx.Button(panel,label='OK',size=(90,28))
        buttonClose = wx.Button(panel,label='Close',size=(90,28))
        sizer.Add(buttonOK,pos=(3,3))
        sizer.Add(buttonClose,pos=(3,4),flag=wx.RIGHT|wx.BOTTOM,border=5)

        sizer.AddGrowableRow(2)
        sizer.AddGrowableCol(1)
        panel.SetSizerAndFit(sizer)
if __name__ == '__main__':
    app = wx.App()
    Example(None,title="FlexGridSizer.py")
    app.MainLoop()