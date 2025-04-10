
from flask import Flask
import os
import datetime
import pytz
import subprocess
import getpass

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Your Full Name"  # replace with your actual name
    username = getpass.getuser()
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get top output (first 10 lines for brevity)
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -n 10", shell=True).decode()
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    return f"""
    <h1>HTOP INFO</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
