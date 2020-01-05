# this gui program havent finished coding and is still implementing in proccess, need to update frames, choosable options and correct/incorrect answers and update questions. I will update accordingly as the time goes.
import tkinter as tk

root = tk.Tk()

root.title("Quiz Master 5000")

v = tk.IntVar()

def OSSN():
    tk.Label(root,
              text="What is OSSN?",
              justify = tk.LEFT,
              padx=20).pack()
    tk.Radiobutton(root,
                   text="Open Source Security Network",
                   padx = 20,
                   variable=v,
                   value=3).pack(anchor=tk.W)
    tk.Radiobutton(root,
                   text="Open Source Security Network2",
                   padx = 20,
                   variable=v,
                   value=4).pack(anchor=tk.W)
    tk.Radiobutton(root,
                   text="Open Source Security Network3",
                   padx = 20,
                   variable=v,
                   value=5).pack(anchor=tk.W)
    tk.Radiobutton(root,
                   text="Operating Systems & Security Networks",
                   padx = 20,
                   variable=v,
                   value=6).pack(anchor=tk.W)
                
    tk.Label(root,
             text="What do you learn mainly in OSSN?",
             justify = tk.LEFT,
             padx=20).pack()
    tk.Radiobutton(root,
                   text="OSSN1",
                   padx = 20,
                   variable=v,
                   value=7).pack(anchor=tk.W)
    tk.Radiobutton(root,
                   text="OSSN2",
                   padx = 20,
                   variable=v,
                   value=8).pack(anchor=tk.W)
    tk.Radiobutton(root,
                   text="OSSN3",
                   padx = 20,
                   variable=v,
                   value=9).pack(anchor=tk.W)
    tk.Radiobutton(root,
                   text="OSSN4",
                   padx = 20,
                   variable=v,
                   value=10).pack(anchor=tk.W)
    

def PADS():
    tk.Label(root,
              text="What is PADS?",
              justify = tk.LEFT,
              padx=20).pack()
    tk.Radiobutton(root,
                   text="PADS",
                   padx = 20,
                   variable=v,
                   value=3).pack(anchor=tk.W)

    tk.Label(root,
             text="What do you learn mainly in PADS?",
             justify = tk.LEFT,
             padx=20).pack()


tk.Label(root, 
        text="""CS Modules for MCQ:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(root, 
              text="OSSN",
              padx = 20, 
              variable=v, 
              value=1, command = OSSN).pack(anchor=tk.W)
tk.Radiobutton(root, 
              text="PADS",
              padx = 20, 
              variable=v, 
              value=2, command = PADS).pack(anchor=tk.W)


#OSSN()
#root.mainloop()
