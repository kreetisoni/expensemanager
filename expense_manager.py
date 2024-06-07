import mysql.connector
import tkinter
import tkinter.messagebox
import tkinter.ttk

sav=mysql.connector.connect(host='localhost', user='root', password='kreeti', database='expenses')
cursor=sav.cursor()

ui=tkinter.Tk()
ui.geometry('800x500')
ui.title("EXPENSE MANAGER")
ui.configure(background="ivory2")

title=tkinter.Label(ui,text="Choose month:", bg='mistyrose2')
title.grid(column=0, row=0)

month=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
cb=tkinter.ttk.Combobox(ui, values=month, width=20)
cb.grid(column=0, row=1)
cb.current(0)

#------------------------------------------------------------------
def button():
    table=cb.get()
    sqll="SHOW TABLES"
    cursor.execute(sqll)
    result=cursor.fetchall()

    result_list=[item[0] for item in result]

    if table in result_list:
        tkinter.messagebox.showinfo("Status", "month exists!")
    else:
        tkinter.messagebox.showinfo("Status", "month does not exist, month created!")
        
        if table=="january":
            cursor.execute("create table January(date int, cash int, name varchar(50));")
        elif table=="february":
            cursor.execute("create table february(date int, cash int, name varchar(50));")
        elif table=="march":
            cursor.execute("create table march(date int, cash int, name varchar(50));")
        elif table=="april":
            cursor.execute("create table april(date int, cash int, name varchar(50));")
        elif table=="may":
            cursor.execute("create table may(date int, cash int, name varchar(50));")
        elif table=="june":
            cursor.execute("create table june(date int, cash int, name varchar(50));")
        elif table=="july":
            cursor.execute("create table july(date int, cash int, name varchar(50));")
        elif table=="august":
            cursor.execute("create table august(date int, cash int, name varchar(50));")
        elif table=="september":
            cursor.execute("create table september(date int, cash int, name varchar(50));")
        elif table=="october":
            cursor.execute("create table october(date int, cash int, name varchar(50));")
        elif table=="november":
            cursor.execute("create table november(date int, cash int, name varchar(50));")
        else:
            cursor.execute("create table december(date int, cash int, name varchar(50));")

sav.commit()


Button=tkinter.Button(ui, text="check", command=button)
Button.grid(column=2, row=1)

#------------------------------------------------------------------------------------------------------------------------------------------------

lbl=tkinter.Label(ui, text='Cash spent(Rs)->', bg='mistyrose2').place(x=10, y=60)
whatval=tkinter.Entry(ui)
whatval.place(x=130, y=60)

lbl2=tkinter.Label(ui, text='Date(DD)->', bg='mistyrose2').place(x=10, y=100)
whatval2=tkinter.Entry(ui)
whatval2.place(x=130, y=100)

lbl3=tkinter.Label(ui,text='Name/Service->', bg='mistyrose2').place(x=10, y=140)
whatval3=tkinter.Entry(ui)
whatval3.place(x=130, y=140)

def insert():
    x=int(whatval2.get())
    y=int(whatval.get())
    z=str(whatval3.get())
    b=cb.get()
    if b=='january':
        cursor.execute('INSERT INTO january(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='february':
        cursor.execute('INSERT INTO feburary(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='march':
        cursor.execute('INSERT INTO march(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='april':
        cursor.execute('INSERT INTO april(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='may':
        cursor.execute('INSERT INTO may(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='june':
        cursor.execute('INSERT INTO june(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='july':
        cursor.execute('INSERT INTO july(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='august':
        cursor.execute('INSERT INTO august(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='september':
        cursor.execute('INSERT INTO september(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='october':
        cursor.execute('INSERT INTO october(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    elif b=='november':
        cursor.execute('INSERT INTO november(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    else:
        cursor.execute('INSERT INTO december(date, cash, name)VALUES(%s, %s, %s)', (x, y, z))
    sav.commit()
    tkinter.messagebox.showinfo('yay!', "DATA ADDED SUCCESSFULLY")

        
addvalue=tkinter.Button(ui, text='Add new value', command=insert)
addvalue.place(x=100, y=220)


def fetchall():
    if cb.get()=="january":
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('january')
        cursor.execute('SELECT*from january')
        i=1
        for january in cursor:
            for j in range(len(january)):
                e=tkinter.Entry(res, width=20, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, january[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='february':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('february')
        cursor.execute('SELECT*from february')
        i=0
        for february in cursor:
            for j in range(len(february)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, february[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='march':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('march')
        cursor.execute('SELECT*from march')
        i=0
        for march in cursor:
            for j in range(len(march)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, march[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='april':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('april')
        cursor.execute('SELECT*from ')
        i=0
        for april in cursor:
            for j in range(len(april)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, april[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='may':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('may')
        cursor.execute('SELECT*from may')
        i=0
        for may in cursor:
            for j in range(len(may)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, may[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='june':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('june')
        cursor.execute('SELECT*from june')
        i=0
        for june in cursor:
            for j in range(len(june)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, june[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='july':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('july')
        cursor.execute('SELECT*from july')
        i=0
        for july in cursor:
            for j in range(len(july)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, july[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='august':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('august')
        cursor.execute('SELECT*from august')
        i=0
        for august in cursor:
            for j in range(len(august)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, august[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='september':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('september')
        cursor.execute('SELECT*from september')
        i=0
        for september in cursor:
            for j in range(len(september)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, september[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='october':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('october')
        cursor.execute('SELECT*from october')
        i=0
        for october in cursor:
            for j in range(len(october)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, october[j])
            i=i+1
        res.mainloop()
    elif cb.get()=='november':
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('november')
        cursor.execute('SELECT*from november')
        i=0
        for november in cursor:
            for j in range(len(november)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, november[j])
            i=i+1
        res.mainloop()
    else:
        res=tkinter.Tk()
        res.geometry('300x300')
        res.title('december')
        cursor.execute('SELECT*from december')
        i=0
        for december in cursor:
            for j in range(len(december)):
                e=tkinter.Entry(res, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(tkinter.END, december[j])
            i=i+1
        res.mainloop()
    sav.commit()

getval=tkinter.Button(ui, text='fetch value', command=fetchall)
getval.place(x=200, y=220)

def add():
    if cb.get()=='january':
        cursor.execute('SELECT sum(cash) FROM january')
    elif cb.get()=='february':
        cursor.execute('SELECT sum(cash) FROM february')
    elif cb.get()=='march':
        cursor.execute('SELECT sum(cash) FROM march')
    elif cb.get()=='april':
        cursor.execute('SELECT sum(cash) FROM april')
    elif cb.get()=='may':
        cursor.execute('SELECT sum(cash) FROM may')
    elif cb.get()=='june':
        cursor.execute('SELECT sum(cash) FROM june')
    elif cb.get()=='july':
        cursor.execute('SELECT sum(cash) FROM july')
    elif cb.get()=='august':
        cursor.execute('SELECT sum(cash) FROM august')
    elif cb.get()=='september':
        cursor.execute('SELECT sum(cash) FROM september')
    elif cb.get()=='october':
        cursor.execute('SELECT sum(cash) FROM october')
    elif cb.get()=='november':
        cursor.execute('SELECT sum(cash) FROM november')
    else:
        cursor.execute('SELECT sum(cash) FROM december')
    total=cursor.fetchall()
    tkinter.messagebox.showinfo("MONEY SPENT THIS MONTH", total)
    sav.commit()

sumval=tkinter.Button(ui, text='Total cash', command=add)
sumval.place(x=300, y=220)

def umm():
    answer=tkinter.messagebox.askquestion('', "Do you really want to delete all data of this month?")
    if answer=='yes':
        def deleteMonth():
            if cb.get()=='january':
                cursor.execute('DROP table january;')
            elif cb.get()=='february':
                cursor.execute('DROP table february;')
            elif cb.get()=='march':
                cursor.execute('DROP table march;')
            elif cb.get()=='april':
                cursor.execute('DROP table april;')
            elif cb.get()=='may':
                cursor.execute('DROP table may;')
            elif cb.get()=='june':
                cursor.execute('DROP table june;')
            elif cb.get()=='july':
                cursor.execute('DROP table july;')
            elif cb.get()=='august':
                cursor.execute('DROP table august;')
            elif cb.get()=='september':
                cursor.execute('DROP table september;')
            elif cb.get()=='october':
                cursor.execute('DROP table october;')
            elif cb.get()=='november':
                cursor.execute('DROP table november;')
            else:
                cursor.execute('DROP table december;')
        sav.commit()
        deleteMonth()
        tkinter.messagebox.showinfo('yay!', "DATA DELETED")
    elif answer=='no':
        print('ok')
    else:
        print("jeez, fine!")
        
deleteMonth=tkinter.Button(ui, text='Delete MONTH',bg='black', fg='red', command=umm)
deleteMonth.place(x=400, y=220)

#---------------------------------------------------

title2=tkinter.Label(ui, text="[HOW TO USE? check for month->add new value/fetch value/get total]", bg='white')
title2.grid(column=3, row=1)


ui.mainloop()
sav.close()



        
