from tkinter import *







class Quiz:
    def __init__(self):
        #open the interface and display an introduction message
        #a quiz is an object, that is made up of multiple Question objects
        root = Tk()
        quiz = self.interface(root)

        root.mainloop()


    def interface(self, root):
        frame = Frame(root)
        frame.grid(row=0,column=0)

        self.intro = Label(frame, text='Welcome to Quiz Master 5000! Please select a module below')
        self.intro.grid(row=0,column=0)

        


        self.button = Button(frame, text='Quit', fg='red', command=frame.quit, height=4, width=20)
        self.button.grid(row=1,column=0)


    def database_retrieval():
        #this is where the program will retrieve all the information from the database
        #when a module is selected, download questions and format correctly
        pass


class Question:
    def __init__(self, question, options, answer):
        #Individual Questions as a class
        #question is a string, options is a tuple, answer is a string
        pass






def main():
    game = Quiz()
    print('program finished')









if __name__ == '__main__':
    main()
