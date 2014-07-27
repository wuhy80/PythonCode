import wx

""" see images
"""
class InsertFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, 
                    pos = wx.DefaultPosition, 
                    title = "Hello, wxPython"):
        
        wx.Frame.__init__(self, parent, id, title, pos)
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Close", pos=(125, 10),
                                size=(150,50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
    def OnCloseMe(self, event):
        self.Close(True)
        
    def OnCloseWindow(self, event):
        self.Destroy()

class App(wx.App):
    def __init__(self, redirect=False):
        wx.App.__init__(self, redirect)
        
    def OnInit(self):
        image = wx.Image("wxPython.jpg", wx.BITMAP_TYPE_JPEG)
        
        self.frame = InsertFrame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        
        return True
    
if __name__ == "__main__":
    app = App()
    
    app.MainLoop()