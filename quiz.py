from tkinter import *
import pymysql

class Quiz:
    def __init__(self, cursor, module_name):
        #Initializes quiz attributes
        self.correct_answers = 0

        #questions contains ALL questions in a list. This list contains multiple question objects
        self.questions = self.database_retrieval(module_name, cursor)

        self.no_of_questions = len(self.questions)

    def ask_all(self):
        #ask all questions in terminal
        #@AUNG - in the final version, this will be done in the GUI, so this module will be removed in a future release
        for index, question in enumerate(self.questions):
            print('Question ' + str(index))
            user_answer = input(question.ask() + '\n')
            if question.check(user_answer) == True:
                self.correct_answers += 1
                print('question correct!')
            else:
                print('question incorrect.')


    def database_retrieval(self, module_name, cursor):
        # retrieves questions from database
        # output is a list of Question objects
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

    def final_tally(self):
        print('You got {} out of {} questions correct!'.format(self.correct_answers, self.no_of_questions))


    #unused modules
    """
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
    """


class Question(object):
    def __init__(self, question, options, answer):
        #Individual questions, made up of 3 parts: question, options answer
        #question is a string
        self.question = question
        #options are in a list
        self.options = options.split('|')
        #answer is a string
        self.answer = answer

    def check(self, user_answer):
        #check if user answer matches real answer
        #output boolean
        if user_answer == self.answer:
            return True
        else:
            return False


    def ask(self):
        return self.question + '\n' + self.list_options()

    def list_options(self):
        return 'The options are: ' + ', '.join(self.options)


def main():

    #database connection step, can make a module for it
    host = 'addatabase.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
    database = 'main'
    user = 'admin'
    password = '1234567890'
    port = 3306
    connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)
    cursor = connection.cursor()

    quiz = Quiz(cursor, 'math')
    quiz.ask_all()
    quiz.final_tally()

    print('program finished debug')









if __name__ == '__main__':
    main()
