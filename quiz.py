import tkinter as tk
from tkinter import font as tkfont
import pymysql
from datetime import date
import numpy as np

"""
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
"""

        
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


"""
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
"""

"""
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

"""
GLOBAL_USERNAME = []
GLOBAL_CURSOR = []
GLOBAL_MODULE = [None]


class QuizMasterGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#97c7f1')
        tk.Label(self, text ="Welcome to Quiz Master 5000", padx=10,pady=10,font=('arial',20),fg="blue",bg="#97c7f1").pack()
        tk.Label (self,text = "Please enter your username", font=('arial',15),padx = 20, pady =20,bg="#97c7f1").pack()
        e = tk.Entry(self,bg="#97c7f1")
        def next():
            username = e.get()
            if not username:
                error_message = tk.Label(self, text='Invalid Username',bg="#97c7f1").pack()
                return
            GLOBAL_USERNAME.append(username)
            controller.show_frame("PageOne")
        e.pack()
        tk.Label(self, text="            ",padx=10,pady=10,bg="#97c7f1").pack()

        tk.Button(self, text="Next", command=next,padx=5,pady=5).pack()

        tk.Label(self, text="            ",padx=10,pady=10,bg="#97c7f1").pack()





class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='#97c7f1')
        controller.title('Module Selection')
        #label= tk.Label(self, text ="Hello",padx=10, pady=10).pack(anchor="w")
        label1 = tk.Label(self, text ="Available Modules:", padx=10,pady=10,bg="#97c7f1")
        label1.pack(anchor="w")
        modules = [("DIR", "PageTwo"), ("OSSN", "PageThree"), ("SE", "PageFour"), ("SQPM", "PageFive"), ("TSLEC", "PageSix")]

        v = tk.StringVar(None, "DIR")
        def next():
            module = v.get()
            GLOBAL_MODULE[0] = module
            window = tk.Toplevel()
            QuizQuestions(window, module)
            #frame = Dummy(parent=parent, controller=controller)
            #controller.frames["Dummy"] = frame
            #frame.grid(row=0, column=0, sticky="nsew")

            #controller.show_frame("Dummy")

        for module, page in modules:
            #tk.Button(self, text=module, width=20, height=1, command=lambda: next(module, page)).pack(anchor='center')
            tk.Radiobutton(self, text=module, bg="#97c7f1", padx=20,pady=10,font=('arial',15), variable=v, value=module).pack(anchor='w')


        tk.Button(self, text='select', command=next,padx=10,pady=10).pack()
        tk.Label(self, text="   ",padx=10,pady=10,bg="#97c7f1").pack()

class QuizQuestions:
    def __init__(self, master, module):
        master.title(module)
        self.master = master
        container = tk.Frame(master)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.cursor = GLOBAL_CURSOR[0]
        self.questions = self.database_retrieval(module)
        self.no_of_questions = len(self.questions)
        self.correct = 0



        self.frames = {}

        for index, question_object in enumerate(self.questions):
            page_name = index
            frame = QuizQuestion(container, self, index, question_object)
            self.frames[index] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(0)


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


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


class QuizQuestion(tk.Frame):
    def __init__(self, parent, controller, index, question_object):
        tk.Frame.__init__(self, parent)
        self.configure(background='#97c7f1')
        self.index = index
        self.controller = controller
        self.parent = parent

        self.question = question_object.question
        self.options  = question_object.options
        self.answer   = question_object.answer

        self.Q = tk.Label(self, text=question_object.question, font=('Calibri', 20),bg="#97c7f1",padx=10,pady=10)
        self.A = tk.Button(self, text=question_object.options['A'], width=80, height=2, command=lambda: self.check('A'))
        self.B = tk.Button(self, text=question_object.options['B'], width=80, height=2, command=lambda: self.check('B'))
        self.C = tk.Button(self, text=question_object.options['C'], width=80, height=2, command=lambda: self.check('C'))
        self.D = tk.Button(self, text=question_object.options['D'], width=80, height=2, command=lambda: self.check('D'))

        self.Q.pack()
        self.A.pack()
        self.B.pack()
        self.C.pack()
        self.D.pack()
        tk.Label(self, text="   ",padx=10,pady=10,bg="#97c7f1").pack()


    def check(self, option):
        if self.options[option] == self.answer:
            self.controller.correct += 1
            tk.Button(self, text='Correct!, Click to continue', command=self.next, height=2, width=40).pack()
            tk.Label(self, text="   ",padx=10,pady=10,bg="#97c7f1").pack()
        else:
            tk.Button(self, text='Incorrect!, Click to continue', command=self.next, height=2, width=40).pack()
            tk.Label(self, text="   ",padx=10,pady=10,bg="#97c7f1").pack()
        for value, option in zip(self.options.values(), [self.A, self.B, self.C, self.D]):
            if value == self.answer:
                option.configure(bg='#6EEC77', state='disabled')
            else:
                option.configure(bg='#EC6E6E', state='disabled')

    def next(self):
        if self.index == 9:
            frame = FinalPage(self.parent, self.controller)
            self.controller.frames['FinalPage'] = frame
            frame.grid(row=0, column=0, sticky='nsew')

            self.controller.show_frame('FinalPage')
        else:
            self.controller.show_frame(self.index+1)

class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#97c7f1')
        self.controller = controller
        self.update_database()
        r = 'You got ' + str(self.controller.correct) + ' out of 10 questions correct!'
        tk.Label(self, text=r,font=('arial',20),bg="#97c7f1",padx=10,pady=10).pack(anchor='center')
        tk.Label(self, text="            ",padx=10,pady=10,bg="#97c7f1").pack()

        tk.Button(self, text='Check Answers',padx=10,pady=10, command=self.run_through).pack()
        tk.Label(self, text="            ",padx=5,pady=5,bg="#97c7f1").pack()      
        tk.Button(self, text='High Scores', command=self.high_score,padx=10,pady=10).pack()
        tk.Label(self, text="            ",padx=5,pady=5,bg="#97c7f1").pack()
        #high score update and show


        tk.Button(self, text='Close Quiz', command=self.controller.master.destroy,padx=10,pady=10).pack()
        tk.Label(self, text="            ",padx=5,pady=5,bg="#97c7f1").pack()
    def run_through(self):
        self.controller.show_frame(0)



    def update_database(self):
        print('DEBUG: begin update database')
        today = date.today()
        GLOBAL_CURSOR[0].execute("insert into scores values('','{}','{}','{}','{}')".format(today, GLOBAL_USERNAME[0], GLOBAL_MODULE[0], self.controller.correct))
        print('DEBUG: end update database')


    def high_score(self):
        master = tk.Tk()
        master.title('High Score')
        master.configure(background='#97c7f1')
        GLOBAL_CURSOR[0].execute("select * from scores where username='{}' and module_name='{}'".format(GLOBAL_USERNAME[0], GLOBAL_MODULE[0]))
        scores = GLOBAL_CURSOR[0].fetchall()
        top_three = big_three(scores, 3)
        top_three = insertion_sort(top_three)
        for row in top_three:
            s = 'Date: {} - Username: {} - Score: {}'.format(row[1], row[2], row[4])
            tk.Label(master, text=s,bg="#97c7f1",padx=10,pady=10,font=(10)).pack()
        tk.Label(master, text="            ",padx=5,pady=5,bg="#97c7f1").pack()
        tk.Button(master, text='Close', padx=7,pady=7,command=master.destroy).pack()
        tk.Label(master, text="            ",padx=5,pady=5,bg="#97c7f1").pack()

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


import time
import warnings

def main():
    warnings.filterwarnings("ignore")
    #database connection step, can make a module for it
    host = 'ad-database.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
    database = 'adproject'
    user = 'admin'
    password = '1234567890'
    port = 3306
    connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)
    cursor = connection.cursor()

    GLOBAL_CURSOR.append(cursor)

    app = QuizMasterGUI()
    app.mainloop()

    """
    print('Welcome to Quiz Master 5000')
    print('=' * 30)
    username = input('What is your username? ').lower()
    module_dict = {'A':'DIR', 'B':'OSSN', 'C':'SE', 'D':'SQPM', 'E':'TSLEC'}
    module = quiz_selection(module_dict)
    """
    """
    play = True
    while play:
        quiz = Quiz(cursor, module, username)
        quiz.ask_all()
        quiz.final_print()
        quiz.update_database()
        #play the highscore only for that specific module
        quiz.last_three()

        play = continue_playing()
    """
    print('==DEBUG== Program Finished ==DEBUG==')

    connection.commit()






if __name__ == '__main__':
    main()
