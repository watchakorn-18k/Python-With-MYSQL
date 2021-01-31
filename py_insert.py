import mysql.connector #รับโมดูลเข้ามา

my_db = mysql.connector.connect(
    host="localhost",   #ที่อยู่ฐานข้อมูล
    user="test_py",     #user หือ บัญชีที่จะใช้เชื่อมต่อ
    password="test_py123", #รหัสผ่านของบัญชี
    database="python_sql" #ชื่อฐานข้อมูล
) #เชื่อมต่อกันฐานข้อมูล
my_cursor = my_db.cursor() # .cursor() ทำหน้าที่ในการชี้ลิงค์ตำแหน่งต่างๆไปยังฐานข้อมูลและใช้ในการประมวลผลนั่นเอง

def insert_data(id,fname,lname,age): #สร้างฟังค์ชั่นเพื่อทำการเพิ่มข้อมูลลงไปใน ฐานข้อมูล โดยมี arg อาร์กิวเมนคือ id,fname,lname,age
    sql_insert = "INSERT INTO tb_member (member_id,member_name,member_lastname,member_age)VALUES (%s,%s,%s,%s)"
    #สร้างตัวแปร sql_insert เพื่อเก็บค่าคำสั่งของ sql 
    #INSERT INTO คือระบุการบอก sql ว่า เพิ่มเข้าไปที่ tb_member คือชื่อตารางของฐานข้อมูล
    #(member_id,member_name,member_lastname,member_age) คือการเรียกคอลัมภ์ในตาราง
    #VALUES (%s,%s,%s,%s) คือค่าหรือข้อมูลที่จะเอาลงไปในฐานข้อมูล
    val_insert = (id,fname,lname,age)
    #val_insert ตัวแปรที่เก็บค่าของอาร์กิวเมน id,fname,lname,age
    my_cursor.execute(sql_insert,val_insert) #คือการชี้ตำแหน่งไปดำเนินการไปกระทำตัวแปร sql_insert เพื่อเพิ่มข้อมูลโดยเอาข้อมูลจาก val_insert เข้าไปในฐานข้อมูล
    my_db.commit() #คือคำสั่งยืนยันคำสั่ง
    
insert_data("012","ศรีเทพ","สีสวย",56) #ทดสอบเรียกใช้ฟังค์ชั่น insert_data โดย ("012","ศรีเทพ","สีสวย",56) คือสิ่งที่จะเพิ่มเข้าไปในฐานข้อมูล
