#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import arpisearch

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        
        self.entry.bind("<Return>", self.OnPressEnter)
        
        button = Tkinter.Button(self,text=u"Search", command=self.OnButtonClick)
        button.grid(column=1,row=0)
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
    	var = arpisearch.main(self.entryVariable.get())
    	print var
    	for x in range(len(var)):
    		self.labelVariable = Tkinter.StringVar() 
        	label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="black", bg="white")
    		label.grid(column=0,row=x + 1,columnspan=2,sticky='EW')
#    		self.labelVariable.set(var.index(x - 1))

	def OnPressEnter(self,event):
		for x in range(1, len(arpisearch.main(self.entryVariable.get()))):
			self.labelVariable2 = Tkinter.StringVar()
			label = Tkinter.Label(self,  textvariable=self.labelVariable2, anchor="w", fg="black", bg="white")
			
			label.grid(column=0,row=x,columnspan=2,sticky='EW')
		
       	#self.labelVariable.set(arpisearch.main(self.entryVariable.get()))

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('News Interface')
    app.mainloop()