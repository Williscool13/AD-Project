with open('preprocessed quiz.txt', 'r') as f:
    data = f.read().split('\n')


#no_of_modules = input('how many modules:')

if len(data) % 61 != 0:
    print('incorrect length')
    print(len(data))
else:
    no_of_modules = len(data) / 61
all_modules = []
all_questions= []
all_options = []
all_answers = []

for i in range(int(no_of_modules)):
    module_name = data[0 + 61 * i]
    questions = data[1 + 61 * i:61 * (i + 1):6]
    options1 = data[2 + 61 * i:61 * (i + 1):6]
    options2 = data[3 + 61 * i:61 * (i + 1):6]
    options3 = data[4 + 61 * i:61 * (i + 1):6]
    options4 = data[5 + 61 * i:61 * (i + 1):6]
    answer = data[6 + 61 * i:61 * (i + 1):6]

    options1 = [x.title() for x in options1]
    options2 = [x.title() for x in options2]
    options3 = [x.title() for x in options3]
    options4 = [x.title() for x in options4]
    
    all_modules.append(module_name)
    all_questions.append(list([x.title() for x in questions]))
    all_options.append(list(zip(options1,options2,options3,options4)))
    all_answers.append([x[8:].title() for x in answer])

for i in range(int(no_of_modules)):
    print('=' * 30 + '\n' + 'MODULE ' + str(i) + '\n' + '=' * 30)
    print(all_modules[i])
    print(all_questions[i])
    print(all_options[i])
    print(all_answers[i])

import pymysql
host = 'ad-database.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
database = 'adproject'
user = 'admin'
password = '1234567890'
port = 3306
connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)
cursor = connection.cursor()

for i in range(int(no_of_modules)):
    cursor.execute("create table {}({} int(64) not null auto_increment primary key, question varchar(256), options varchar(512), answer varchar(128))".format(all_modules[i], all_modules[i] + '_id'))
    for j in range(len(all_questions[i])):
        cursor.execute("insert into {} values('', '{}', '{}', '{}')".format(all_modules[i], all_questions[i][j], '|'.join(all_options[i][j]), all_answers[i][j]))
    
                       




    



