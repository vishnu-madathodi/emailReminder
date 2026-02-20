import pythoncom
import win32com.client as win32

def generate_draft(to, cc_list, subject, template):
    pythoncom.CoInitialize()
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)

    mail.To = to
    mail.CC = "; ".join(cc_list)
    mail.Subject = subject
    mail.HTMLBody = template

    mail.Display()


#full issues now. not even the mail is opening and I have removed logic for esc key close as that is not working. 
#the exe is getting no where. 
#check isue with crashing - wrong name