import os
import subprocess
import sqlite3

# 🚨 Vulnerability: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "12345"

def insecure_exec(user_input):
    # 🚨 Vulnerability: Command Injection
    os.system("echo " + user_input)

def sql_injection(user_input):
    # 🚨 Vulnerability: SQL Injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)  # No input sanitization
    result = cursor.fetchall()
    print(result)

def unsafe_subprocess(user_input):
    # 🚨 Vulnerability: Subprocess Injection
    subprocess.call("ls " + user_input, shell=True)

def insecure_file_handling():
    # 🚨 Vulnerability: Insecure File Permissions
    with open("sensitive_data.txt", "w") as f:
        f.write("Secret API Key: ABC123")

if __name__ == "__main__":
    user_input = input("Enter something: ")
    insecure_exec(user_input)
    sql_injection(user_input)
    unsafe_subprocess(user_input)
    insecure_file_handling()

