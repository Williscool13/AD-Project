import pymysql
def main():
    #### DO NOT TOUCH
    host = 'ad-database.chexbadcv1tk.ap-southeast-1.rds.amazonaws.com'
    database = 'adproject'
    user = 'admin'
    password = '1234567890'
    port = 3306
    connection = pymysql.connect(host=host, db=database, user=user, passwd=password, port=port)
    cursor = connection.cursor()
    #### DO NOT TOUCH###############################################################################
    
    command = 'select * from quiz'
    cursor.execute(command)
    print('Printing all table names: \n', cursor.fetchall())

    #################################################################################################
    print('program finished')

if __name__ == '__main__':
    main()



#"""create table quiz(quizid int(50) not null auto_increment primary key, question varchar(100), options varchar(200), answer varchar(100))"""

#command = "insert into quiz values(1,'1+1', '3|4|2|9', '2')"
#cursor.execute(command)
#connection.commit()

#command = "insert into quiz values(2,'2+2', '6|4|8|11', '4')"
#cursor.execute(command)
#connection.commit()
   


#command = 'create table scores(scoreid int(50) not null auto_increment primary key, date varchar(50), username varchar(100), module_name varchar(100), score int(2))'
