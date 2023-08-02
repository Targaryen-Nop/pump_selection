import mysql.connector
import pandas as pd


# def add_data(value1,value2):
#     # เชื่อมต่อกับฐานข้อมูล MySQL
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="pea_detail_pump"
#     )

#     # สร้างอินสแตนซ์ของคลาส cursor
#     mycursor = mydb.cursor()

#     # สร้างและ execute คำสั่ง SQL เพื่อเพิ่มข้อมูล
#     sql = "INSERT INTO test (name, suname) VALUES (%s, %s)"
#     values = (value1, value2)  
#     mycursor.execute(sql, values)

#     # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
#     mydb.commit()

#     # ตรวจสอบว่าข้อมูลถูกเพิ่มเข้าสู่ฐานข้อมูลหรือไม่
#     print(mycursor.rowcount, "record(s) inserted.")

# # เรียกใช้งานฟังก์ชันสร้างข้อมูล
# df = pd.read_excel('FAC-0255-ORG.xlsx')
# print(df)