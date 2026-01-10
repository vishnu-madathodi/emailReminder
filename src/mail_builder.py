import json

#1.function to find mailIDs
def find_mailID(team_name):
    with open('../data/teams.json','r') as file:
        data = json.load(file)

    for group_name, info in data.items():
        if(group_name.lower() == team_name.lower()):
            team_mail = info['team_mail']
            dl_mail = info['cc']['dl_mail']

    return team_mail, dl_mail
#2.function to modify template
def create_template(team_name, incident_id, user_name = 'Vishnu MR'):
    find_mailID(team_name) #find mailIDs to which the mail has be sent

    with open("../templates/reminderTemplate.html","r") as f:
        template_content = f.read()

    #custom dictionary for values to be replaced
    values = {
        "team_name": team_name, 
        "incident_id": incident_id,
        "user_name": user_name,
    }
    for key, value in values.items():
        template_content = template_content.replace(f"{{{{{key}}}}}", value)

    return template_content