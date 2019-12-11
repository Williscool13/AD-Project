from tkinter import *





class Interface:
    def __init__(self, master):
        #class based implementation of the GUI for the quiz, use Tkinter
        frame = Frame(master)
        frame.pack()

        Label(master, text='test').pack()


class Quiz:
    def __init__(self):
        #open the interface and display an introduction message
        #a quiz is an object, that is made up of multiple Question objects
        root = Tk()
        quiz = Interface(root)

        root.mainloop()



class Question:
    def __init__(self, question, options, answer):
        #Individual Questions as a class
        #question is a string, options is a tuple, answer is a string
        pass




    def database_retrieval():
        #this is where the program will retrieve all the information from the database
        pass



def main():
    game = Quiz()
    print('program finished')









if __name__ == '__main__':
    main()
