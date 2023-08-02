import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pea_detail_pump"
)


def mySQL(model_short):
    df = pd.read_sql(
    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,eff_rl,se_quence FROM factory_table where model_short = "{model_short}" ORDER BY `factory_table`.`se_quence` ASC', con=mydb)
    return df