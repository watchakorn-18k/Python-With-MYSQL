import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="test_py",
    password="test_py123",
    database="python_sql"
)
my_cursor = my_db.cursor()

def insert_data(id,fname,lname,age):
    sql_insert = "INSERT INTO tb_member (member_id,member_name,member_lastname,member_age)VALUES (%s,%s,%s,%s)"
    val_insert = (id,fname,lname,age)
    my_cursor.execute(sql_insert,val_insert)
    my_db.commit()

def select_data():
    sql_select = "select * from tb_member"
    my_cursor.execute(sql_select)
    my_data = my_cursor.fetchall()
    for i in my_data:
        print(i)

def delete_data(m_id):
    sql_delete = "delete from tb_member where member_id = %s"
    val_delete = (m_id,)
    my_cursor.execute(sql_delete,val_delete)
    my_db.commit()

print("ข้อมูลสมาชิก")
select_data()
m_id = input('กรอกรหัสสมาชิกที่ต้องการลบ : ')
delete_data(m_id)
select_data()

mb_id = input('กรุณากรอกรหัสสมาชิก : ')
mb_name = input('กรุณากรอกชื่อสมาชิก : ')
mb_lastname = input('กรุณากรอกนามสกุลสมาชิก : ')
mb_age = input('กรุณากรอกข้อมูลอายุสมาชิก : ')

insert_data(mb_id,mb_name,mb_lastname,mb_age)


