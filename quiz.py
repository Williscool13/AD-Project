from tkinter import *
import pymysql
from datetime import date
import numpy as np


class Quiz:
    def __init__(self, cursor, module_name, username):
        #Initializes quiz attributes
        self.correct_answers = 0
        #questions contains ALL questions in a list. This list contains multiple question objects
        self.cursor = cursor
        self.questions = self.database_retrieval(module_name)
        self.no_of_questions = len(self.questions)
        self.correct = []
        self.username = username
        self.module_name = module_name

    def ask_all(self):
        #ask all questions in terminal
        #@AUNG - in the final version, this will be done in the GUI, so this module will be removed in a future release
        for index, question in enumerate(self.questions):
            print('=' * 50)
            print('Question ' + str(index + 1))
            print(question.ask())
            user_answer = input().upper()
            while user_answer not in ['A','B','C','D']:
                user_answer = input('Please input A,B,C, or D: ').upper()
            if question.check(user_answer) == True:
                self.correct_answers += 1
                print('Answer  Correct!\nYou Gain 1/1 Points')
                self.correct.append(question)
            else:
                print('Answer Incorrect.\nYou Gain 0/1 Points')
            print('CORRECT ANSWER IS:', question.get_answer())


    def database_retrieval(self, module_name):
        # retrieves questions from database
        # output is a list of Question objects
        query = 'select * from ' + module_name
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        print('==DEBUG==','Retrieving Records', records, '==/DEBUG==', sep='\n')
        questions = []
        for row in records:
            print('==DEBUG==','Processing Record ' + str(row[0]), '==DEBUG==')
            question = Question(row[1], row[2], row[3])
            questions.append(question)
        return questions

    def final_print(self):
        print('=' * 100)
        print('You got {} out of {} questions correct!'.format(self.correct_answers, self.no_of_questions))
        print('Total Points: {}/{}'.format(self.correct_answers, self.no_of_questions))
        if not self.correct:
            print("You didn't get answer any questions correctly, boohoo")
        else:
            print('You answered the following questions correctly:')
            print('=' * 20)
            for question in self.correct:
                question.to_string()
                print('-' * 20)


    
    def update_database(self):
        print('DEBUG: begin update database')
        today = date.today()
        self.cursor.execute("insert into scores values('','{}','{}','{}','{}')".format(today, self.username, self.module_name, self.correct_answers))
        print('DEBUG: end update database')

    def last_three(self):
        self.cursor.execute("select * from scores where username='{}' and module_name='{}'".format(self.username, self.module_name))
        scores = self.cursor.fetchall()
        top_three = big_three(scores, 3)
        top_three = insertion_sort(top_three)
        for row in top_three:
            print('Date: {} - Username: {} - Score: {}'.format(row[1], row[2], row[4]))



def big_three(arr, N):
    if len(arr) <= N:
        return arr
    else:
        scores = [[0,'','','', 0], [0,'','','', 0], [0,'','','', 0]]
        idx_min = np.argmin([x[4] for x in scores])
        for i in arr:
            if i[4] >= scores[idx_min][4]:
                scores[idx_min] = i
                idx_min = np.argmin([x[4] for x in scores])

    return scores

def insertion_sort(arr): 
    final_list = [list(x) for x in arr]

    for i in range(1, len(arr)):
        key = final_list[i]

        j = i - 1
        while j >= 0 and key[4] < arr[j][4]:
            final_list[j + 1] = final_list[j]
            j -= 1
        final_list[j + 1] = key

    return reversed(final_list)
        
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
        #options are in a dictionary
        temp = [x.strip() for x in options.split('|')]
        self.options = dict(zip(['A','B','C','D'], temp))
        #answer is a string
        self.answer = answer
        
    def check(self, user_answer):
        #check if user answer matches real answer
        #output boolean
        if self.options[user_answer] == self.answer:
            return True
        else:
            return False


    def ask(self):
        question = self.question + '\n'
        sep = '-' * 50
        options = '\nOptions:\n' + '\n'.join(['{}: {}'.format(key, value) for key, value in list(self.options.items())])
        return question + sep + options
    #self.question + '\n' + self.list_options()

    def list_options(self):
        return ', '.join(self.options)

    def get_answer(self):
        return self.answer

    def to_string(self):
        print('Question:', self.question)
        print('Options:\n' + '\n'.join(['{}: {}'.format(key, value) for key, value in list(self.options.items())]))
        print('Answer:', self.answer)
        

def quiz_selection(module_dict):
    print('Available Modules:')
    for key, module in module_dict.items():
        print('{}: {}'.format(key, module))
    user_choice = input('Please select a module: ').upper().strip()
    while user_choice not in module_dict.keys():
        user_choice = input('Please select from: ' + ', '.join(list(module_dict.keys())))

    return module_dict[user_choice]


def continue_playing():
    a = input('Would you like to retake the quiz? (Y/N): ').lower()
    while a not in ['y','n']:
        a = input('Please input (Y) or (N): ')
    if a == 'y':
        return True
    else:
        return False

def main():

    #database connection step, can make a module for it
    host = 'ad-database.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
    database = 'adproject'
    user = 'admin'
    password = '1234567890'
    port = 3306
    connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)
    cursor = connection.cursor()

    print('Welcome to Quiz Master 5000')
    print('=' * 30)
    username = input('What is your username? ').lower()
    module_dict = {'A':'DIR', 'B':'OSSN', 'C':'SE', 'D':'SQPM', 'E':'TSLEC'}
    module = quiz_selection(module_dict)
    
    play = True
    while play:
        quiz = Quiz(cursor, module, username)
        quiz.ask_all()
        quiz.final_print()
        quiz.update_database()
        #play the highscore only for that specific module
        quiz.last_three()

        play = continue_playing()
        
    print('==DEBUG== Program Finished ==DEBUG==')

    connection.commit()







if __name__ == '__main__':
    main()
