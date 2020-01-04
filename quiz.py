from tkinter import *
import pymysql

class Quiz:
    def __init__(self, cursor, module_name):
        #open the interface and display an introduction message
        #a quiz is an object, that is made up of multiple Question objects
        self.questions = self.database_retrieval(module_name, cursor)




        #root = Tk()
        #quiz = self.interface(root)
        #root.mainloop()


    def interface(self, root):
        frame = Frame(root)
        frame.grid(row=0,column=0)

        self.intro = Label(frame, text='Welcome to Quiz Master 5000! Please select a module below')
        self.intro.grid(row=0,column=0)




        self.button = Button(frame, text='Quit', fg='red', command=frame.quit, height=4, width=20)
        self.button.grid(row=1,column=0)


    def ask_all(self):
        for index, question in enumerate(self.questions):
            print('Question ' + str(index))
            user_answer = input(question.ask() + '\n')
            if question.check(user_answer) == True:
                print('question correct!')
            else:
                print('question incorrect.')


    def database_retrieval(self, module_name, cursor):
        #this is where the program will retrieve all the information from the database
        #when a module is selected, download questions and format correctly

        query = 'select * from ' + module_name
        cursor.execute(query)
        records = cursor.fetchall()
        print('retrieving records')
        print(records)
        questions = []
        for row in records:
            print('debug: processing record' + str(row[0]))
            question = Question(row[1], row[2], row[3])
            questions.append(question)
        return questions

class Question:
    def __init__(self, question, options, answer):
        #Individual Questions as a class
        #question is a string, options is a tuple, answer is a string
        self.question = question
        self.options = options.split('|')
        self.answer = answer

    def check(self, user_answer):
        if user_answer == self.answer:
            return True
        else:
            return False

    def ask(self):
        return self.question




def main():

    #database connection step, can make a module for it
    host = 'addatabase.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
    database = 'main'
    user = 'admin'
    password = '1234567890'
    port = 3306
    connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)
    cursor = connection.cursor()

    '''
    command = 'show tables'

    cursor.execute(command)
    print('Printing all table names: \n', cursor.fetchone())
    '''

    quiz = Quiz(cursor, 'math')
    quiz.ask_all()


    print('program finished debug')









if __name__ == '__main__':
    main()
