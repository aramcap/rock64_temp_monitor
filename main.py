import smtplib
import os
from email.message import EmailMessage
import subprocess
 
temp_warn=60
temp_alarm=70
 
def notify(content):
   sender = 'sender@mail.com'
   sender_pass = ‘pass’
   recipient = 'recept@mail.com'
   msg = EmailMessage()
   msg['Subject'] = 'Alert temp NAS'
   msg['From'] = 'rock64@mail.com'
   msg['To'] = recipient
   msg.set_content("""\
NAS temp is {}
""".format(content))
   session = smtplib.SMTP('mail.com', 587)
   session.starttls()
   session.login(sender, sender_pass)
   session.sendmail(sender, [recipient], msg.as_string())
   session.quit()
 
def get_temp():
   cmd = subprocess.run(["cat", "/sys/class/thermal/thermal_zone1/temp"], stdout=subprocess.PIPE)
   return int(cmd.stdout)/1000
 
def main():
   temp = get_temp()
   if temp > temp_alarm:
       notify("VERY HIGH {}ºC".format(temp))
   elif temp > temp_warn:
       notify("HIGH {}ºC".format(temp))
   #print("{}".format(temp))
 
if __name__ == '__main__':
   main()
