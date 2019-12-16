from tkinter import *
import mysql.connector

class Quiz:
    def __init__(self, cursor):
        #open the interface and display an introduction message
        #a quiz is an object, that is made up of multiple Question objects
        self.cursor = cursor
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


    def database_retrieval(self, module, cursor):
        #this is where the program will retrieve all the information from the database
        #when a module is selected, download questions and format correctly

        query = 'select * from questions where module=' + str(module)
        cursor.execute(query)
        records = cursor.fetchall()
        questions = []
        for row in records:
            question = Question(row[0], row[1], row[2])
            questions.append(question)

class Question:
    def __init__(self, question, options, answer):
        #Individual Questions as a class
        #question is a string, options is a tuple, answer is a string



      pass


import pymysql
def main():
    host = 'addatabase.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
    database = 'main'
    user = 'admin'
    password = '1234567890'
    port = 3306

    connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)



    cursor = connection.cursor()
    command = 'show tables'

    cursor.execute(command)
    print('Printing all table names: \n', cursor.fetchone())



    #game = Quiz(cursor)
    print('program finished')









if __name__ == '__main__':
    main()
