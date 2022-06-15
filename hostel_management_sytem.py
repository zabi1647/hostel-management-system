import datetime
import pyodbc
try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\New folder\hostel.accdb;'
    conn: object = pyodbc.connect(con_string)
    print("connected to the data base")

except pyodbc.Error as e:
    print("error in connection", e)

again2 = True
while again2:
    status = input("Type:\n 1 for student. \n 2 for manager:\ntype here:  ")
    if status == "1":
        student_status = input("Are you a new student or already live in our hostel\n n for new \n h for hosteler\n b for having any complain\ntype "
                               "here:  ")
        if student_status == "n":
            is_prime = True
            while is_prime:
                list1 = []
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table1')
                for row in cur.fetchall():
                    x = ('room_no = ', row[0])
                    list1.append(row[0])
                print("We have one seater rooms available. \n They have an attached bathroom. It also has a nice cupboard. All rooms are neat and clean.")
                print("The room numbers not available are: ", list1)
                correct_number = True
                while correct_number:
                    room = int(input("We have total 30 rooms.enter the room number: "))
                    check = list1.count(room)
                    if check > 0:
                        print("Room not available enter another room that you want.")
                    elif room > 30:
                        print("We have total 30 rooms in our hostel. you have pick one of them")
                    else:
                        correct_number = False
                monthly_rent = 20000
                print("The rent for the selected room no  ", room, "is ", monthly_rent)
                month = input("Enter the month you joining in: ")
                rent_paid = int(input("Rent paid: \n"))
                remaining = monthly_rent - rent_paid
                name = input("Enter your name: \n")
                father_name = input("Enter your father name: \n")
                phone_number = input("Enter your phone number: \n")
                father_phone_number = input("Enter your father's phone number: \n")
                date1 = datetime.datetime.now()


                cursor = conn.cursor()
                myuser = (
                    (room, name, father_name, phone_number, father_phone_number, month, rent_paid, remaining, date1,),
                )

                cursor.executemany('INSERT into Table1 VALUES(?,?,?,?,?,?,?,?,?)', myuser)
                conn.commit()
                print('data inserted')

                another_student = input("is there an other student. type y or n: ")
                if another_student == "n":
                    is_prime = False
        elif student_status == "h":
            type = input("what do want to do\n s for submitting fee \n c for change your information  \n l for leaving hostel\ntype here: ")
            if type == "s":
                # for submitting fee of a student in hostel

                list2 = []
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table1')

                for row in cur.fetchall():
                    x = ('room_no = ', row[0])
                    list2.append(row[0])
                # checking room number present in our list
                correct_number = True
                while correct_number:
                    print(list2)
                    room_no = int(input("enter your from the above list room number: "))
                    check = list2.count(room_no)
                    if check > 0:
                        correct_number = False
                    elif room_no > 30:
                        print("we have total 30 rooms in our hostel. you have pick one of them")
                    else:
                        print("this room number is free in our hostel please enter correct room no")
                        correct_number = True
                cur = conn.cursor()
                y = cur.execute('SELECT fee_remaining FROM Table1 WHERE room_no = ?', room_no)
                for r in cur.fetchone():
                    print(r)
                conn.commit()
                integer = int(r)
                total = 20000 + integer
                print(f"you last month remaining dues is {r} and total for this month is {total}")
                amount = int(input("enter the amount of fee that you want to submit: "))
                remaing = (total - amount)
                month_n = input("enter the month name: ")
                fee_submit = amount
                rem = remaing
                x = datetime.datetime.now()

                cur = conn.cursor()
                cur.execute('UPDATE Table1 SET month = ? WHERE room_no = ?', (month_n, room_no))
                cur.execute('UPDATE Table1 SET fee_submitted = ? WHERE room_no = ?', (fee_submit, room_no))
                cur.execute('UPDATE Table1 SET fee_remaining = ? WHERE room_no = ?', (rem, room_no))
                cur.execute('UPDATE Table1 SET [date]=? WHERE room_no = ?', (x, room_no))
                conn.commit()
                print("your fee data update in database")

            elif type == "l":

                # student data delete from table1 and save in table3 for our records

                list3 = []
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table1')

                for row in cur.fetchall():
                    x = ('room_no = ', row[0])
                    list3.append(row[0])
                # checking room number present in our list
                correct_number = True
                while correct_number:
                    print(list3)
                    room_no = int(input("enter your from the above list room number: "))
                    check = list3.count(room_no)
                    if check > 0:
                        correct_number = False
                    elif room_no > 30:
                        print("we have total 30 rooms in our hostel. you have pick one of them")
                    else:
                        print("this room number is free in our hostel please enter correct room no")
                        correct_number = True
                cur = conn.cursor()

                y = cur.execute('SELECT * FROM Table1 WHERE room_no = ?', room_no)
                for row in cur.fetchall():
                    print(row)
                row4 = row
                room_no = row4[0]
                name = row4[1]
                father_name = row4[2]
                phone_number = row4[3]
                father_phone_number = row4[4]
                month = row4[5]
                myuser4 = (
                    (room_no, name, father_name, phone_number,  month, father_phone_number),
                )
                print(myuser4)
                cur.executemany('INSERT into Table3 VALUES(?,?,?,?,?,?)', myuser4)
                cur.execute('DELETE FROM Table1 WHERE room_no = ?', room_no)
                conn.commit()

                print("your data has been deleted from the main table1 and save in table3 of our hostel")
                # data for hostel record

            elif type == "c":
                # changing information in database
                change_again = True
                while change_again:
                    list4 = []
                    cur = conn.cursor()
                    cur.execute('SELECT * FROM Table1')

                    for row in cur.fetchall():
                        x = ('room_no = ', row[0])
                        list4.append(row[0])
                    # checking room number present in our list
                    correct_number = True
                    while correct_number:
                        print(list4)
                        room_no = int(input("enter your from the above list room number: "))
                        check = list4.count(room_no)
                        if check > 0:
                            correct_number = False
                        elif room_no > 30:
                            print("we have total 30 rooms in our hostel. you have pick one of them")
                        else:
                            print("this room number is free in our hostel please enter correct room no")
                            correct_number = True
                    print("what do you want to change in your information . type\n n for name\n f or father name\n ph for phone number\n fh for father phone number.\n type here:  ")
                    change = input("what do you want to  change; ")
                    if change == "f":
                        father_name = input("enter the correct name of your father: ")
                        cur = conn.cursor()
                        cur.execute('UPDATE Table1 SET father_name = ? WHERE room_no = ?', (father_name, room_no))
                        cur.commit()
                        print("your father name has been updated from the data base")
                    elif change == "n":
                        correct_name = input("enter your correct name: ")
                        cur = conn.cursor()
                        cur.execute('UPDATE Table1 SET name = ? WHERE room_no = ?', (correct_name, room_no))
                        cur.commit()
                        print("your name has been updated in the data base")
                    elif change == "ph":
                        correct_number = input("enter your correct phone number: ")
                        cur = conn.cursor()
                        cur.execute('UPDATE Table1 SET phone_no = ? WHERE room_no = ?', (correct_number, room_no))
                        cur.commit()
                        print("your phone number has been updated in the data base")
                    elif change == "fh":
                        correct_number = input("enter your correct phone number of your father: ")
                        cur = conn.cursor()
                        cur.execute('UPDATE Table1 SET father_phone_no = ? WHERE room_no = ?', (correct_number, room_no))
                        cur.commit()
                    else:
                        print("enter the correct word")
                    y = input("is there any other information that you want to change: \n type y or n: ")
                    if y == "y":
                        change_again = True
                    else:
                        change_again = False
        elif student_status == "b":
            # complain save in database in table 2
            again_complain = True
            while again_complain:
                list6 = []
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table1')
                for row in cur.fetchall():
                    x = ('room_no = ', row[0])
                    list6.append(row[0])
                # checking room number present in our list
                correct_number = True
                while correct_number:
                    print(list6)
                    room_no = int(input("enter your from the above list room number: "))
                    check = list6.count(room_no)
                    if check > 0:
                        correct_number = False
                    elif room_no > 30:
                        print("we have total 30 rooms in our hostel. you have pick one of them")
                    else:
                        print("this room number is free in our hostel please enter correct room no")
                        correct_number = True
                complain = input("enter your complain here\n")
                name = input("enter your name: ")
                cursor = conn.cursor()
                myuser = (
                    (name, room_no, complain),
                )

                cursor.executemany('INSERT into Table2 VALUES(?,?,?)', myuser)
                conn.commit()
                print('your complain has been noted by our system it will be solved after in short time or in a week')
                complain_yn = input("Is there any other complain:\n Type y or n:")
                if complain_yn == "y":
                    continue
                else:
                    again_complain = False
    elif status == "2":
        h_data = input("what do you want to know type \n m for servents data\n n for student data \n b for calculating fee and total expenditure of hostel.")
        if h_data == "m":
            # servent data
            print("the servents data is")
            cur = conn.cursor()
            cur.execute('SELECT * FROM Table4')
            for row in cur.fetchall():
                print(row)
        elif h_data == "n":
            # student data
            student_type = input("what do you want to see type:\n p for student live in hostel\n k for student leave hostel\n o for showing complain \n type here: ")
            if student_type == "p":
                print("list of the students live in the hostel")
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table1')
                for row in cur.fetchall():
                    print(row)
            elif student_type == "k":
                print("the list of student who leave hostel are")
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table3')
                for row in cur.fetchall():
                    print(row)
            elif student_type == "o":
                print("total complains submitted in our hostel from students is")
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table2')
                for row in cur.fetchall():
                    print(row)
        elif h_data == "b":
            # fee calcuating
            cal = input("what do you want to calculate.type\n d for total fee calculated in hostel\n f for total expenditure of hostel.")
            if cal == "d":
                # student fee submitted in hostel
                list5 = []
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table1')
                for row in cur.fetchall():
                    x = (row[6])
                    list5.append(row[6])
                i = 0
                for s in list5:
                    s = int(s)
                    i = i+s
                print("the total amount of money calculated is", i)
            elif cal == "f":
                # calculation of total amount spend on hostel in a month
                list6 = []
                cur = conn.cursor()
                cur.execute('SELECT * FROM Table4')
                for row in cur.fetchall():
                    x = (row[3])
                    list6.append(row[3])
                i2 = 0
                for s in list6:
                    s = int(s)
                    i2 = i2 + s
                other_uses = 75000
                i2 += other_uses
                print("the total amount of expenses per month is", i2)
    repeat = input("do you want to check or edit data again\n type y or n: ")
    if repeat == "y":
        continue
    else:
        again2 = False
