import pymysql
from config import *
import pandas as pd
import sqlalchemy

# Define a method to create a database connection
def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype, db=None):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, database=db, charset=charset, cursorclass=curtype);
    return sqlCon

# Define a method to create MySQL users
def createUser(cursor, userName, password,
               querynum=0, 
               updatenum=0, 
               connection_num=0):
    try:
        sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))
    
# Connection parameters and access credentials
ipaddress   = ROOT_DB_HOST
usr         = ROOT_DB_USER
passwd      = ROOT_DB_PASSWORD
charset     = "utf8mb4"     
curtype    = pymysql.cursors.DictCursor    

mySQLConnection = getDatabaseConnection(ipaddress, usr, passwd, charset, curtype,None)
mySQLCursor     = mySQLConnection.cursor()

# Delete sbrp_schema if exist
sqlDropSchema = f"DROP DATABASE IF EXISTS {DB_SCHEMA};"
mySQLCursor.execute(sqlDropSchema)

# Create sbrp_schema
with open("database/ddl_sbrp.sql", "r") as file:
    temp_sql_script = file.read()
    temp_sql_script = temp_sql_script.replace("\t"," ")
    temp_sql_script = temp_sql_script.replace("\n"," ")
    temp = ""
    sql_script = []
    for line in temp_sql_script:
        if line == ";":
            sql_script.append(temp)
            temp = ""
        else:
            temp += line

for line in sql_script:
    if line != "":
        mySQLCursor.execute(line)

# Create user
sqlDropUser = f"DROP USER IF EXISTS '{DB_USER}'@'{DB_HOST}';"
mySQLCursor.execute(sqlDropUser)
createUser(mySQLCursor, DB_USER, DB_PASSWORD)

# Grant privileges
sqlUpdatePermissions = f"GRANT SELECT, INSERT ON {DB_SCHEMA}.* TO '{DB_USER}'@'{DB_HOST}';"
mySQLCursor.execute(sqlUpdatePermissions)
mySQLConnection.close()

# Create user database connection
conn = sqlalchemy.create_engine(ROOT_SQLALCHEMY_DATABASE_URI)
# Append data
datalist = ["database/staff.csv", "database/staff_access.csv", "database/staff_skill.csv", "database/role_skill.csv", "database/staff_role_skill.csv", "database/role_listing.csv", "database/application.csv", "database/role_listing_skills.csv"]
tables = ["staff", "staff_access", "staff_skill", "role_skill", "staff_role_skill", "role_listing", "application", "role_listing_skills"]

for i in range(0, len(datalist)):
    data_df = pd.read_csv(datalist[i], encoding='unicode_escape')
    data_df.to_sql(tables[i], conn, if_exists='append', index=False)

print("Database creation and data import completed!")