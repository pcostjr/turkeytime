import mysql.connector
# always keep these so we can do mysql stuff. possibly ask user for login
mydb = mysql.connector.connect(
    host = "localhost",
    user = "<YOUR DB'S USERNAME>",
    passwd = "<YOUR DB'S PASSWORD>",
    #working db
    database = "<YOUR SCHEMA>
)
