import smtplib

def main():

sender_email = "pauls.konov@gmail.com"
rec_email = "pauls.konov@gmail.com"
password = input(str("Ievadiet paroli : "))
message = "Emails No Pythona"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

print("Pierakstīšanās veiksmīga")
server.sendmail(sender_email, rec_email, message)
print("Emails ir nosūtīts uz ", rec_email)
if __name__ ==  "__main__"
main()
