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



def main():
    connection = mysql.connector.connect(host=host,
                                     database=database,
                                     user=user,
                                     password=password)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    else:
        print('connection unsuccessful')
        exit()

    game = Quiz(cursor)
    print('program finished')









if __name__ == '__main__':
    main()
