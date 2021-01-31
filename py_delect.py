import mysql.connector #รับโมดูลเข้ามา

my_db = mysql.connector.connect( #คำสั่งเชื่อมต่อฐานข้อมูล
    host="localhost",   #ที่อยู่ฐานข้อมูล
    user="test_py",     #user หือ บัญชีที่จะใช้เชื่อมต่อ
    password="test_py123", #รหัสผ่านของบัญชี
    database="python_sql" #ชื่อฐานข้อมูล
) #

my_cursor = my_db.cursor() # .cursor() ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูลและใช้ในการประมวลผลนั่นเอง

def delete_data(m_id):
    sql_delete = "delete from tb_member where member_id = %s"
    val_delete = (m_id,)
    my_cursor.execute(sql_delete,val_delete)
    my_db.commit()
