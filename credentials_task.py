"""
Credential Storage
Description:
	You are asked to develop a web-application backend
	that stores login credentials (i.e., usernames and
	passwords) for the web application’s users. In this
	task, we would like you to implement a method
	storeCredentials that is called for every user at
	account registration. New login credentials are
	appended to a local SQLite database. Assume that
	the username and password are given as HTTP
	POST parameters to your method. Although we
	are not asking you to implement the verifyCredentials
	method for authenticating users at this time,
	assume that you will also be writing that method,
	so you can choose the storage format within the
	database. We have prepared a SQLite database
	named “database.sqlite3” containing a table “users” and five
	text columns, “column1”, “column2”, “column3”,
	“column4”, “column5”. You can use any or all
	of these columns as needed to store users’ login
	credentials; you do not have to use all columns to
	solve the task.
When is the problem solved?
	The credentials are stored in the database file.
"""

def store_credentials(username, password, database="./database.sqlite3"):
    pass

if __name__ == "__main__":
    store_credentials("email@example.com", "P45sW0rD")
