import subprocess
from datetime import datetime
import pytz
from django.http import HttpResponse

def htop_view(request):
    username = os.getlogin()
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1 | head -n 10')

    html_content = f"""
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>Name: Your Full Name</h1>
        <h2>Username: {username}</h2>
        <h2>Server Time in IST: {ist_time}</h2>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(html_content)
