import win32com.client as win32

def generate_draft(to, cc_list, subject, template):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)

    mail.To = to
    mail.CC = "; ".join(cc_list)
    mail.Subject = subject
    mail.HTMLBody = template

    mail.display()
