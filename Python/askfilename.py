#!/usr/bin/env python3

from tkinter.filedialog import askopenfilename

infile = askopenfilename()
rfile = open(infile, "r")
rfile.read()
rfile.close()
