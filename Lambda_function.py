import json
import sys
import logging
import mysql.connector
#rds settings
conn = mysql.connector.connect(
host  = "RDS end point",
user = "userName",
passwd = "Password",
database = "DB name is mentioned in the configuration cloumn",
port = portNumber
 )

def lambda_handler(event, context):
    # TODO implement 
    #This function fetches content from MySQL RDS instance
    cur=conn.cursor(buffered=True)
    value1=event['key1']
    value2=event['key2']
    value3=event['key3']
    value4=event['key4']
    value5=event['key5']
    value6=event['key6']
   
    sql="""INSERT INTO LabDetails (Key1,Key2, Key3, Key4,Key5, Key6) VALUES (%s, %s, %s, %s, %s, %s)"""
    val=(value1,value2,value3,value4,value5,value6)
    cur.execute(sql,val)
    conn.commit()
    return {
        'statusCode': 200,
        'body': json.dumps((connection succeeded))
    }
