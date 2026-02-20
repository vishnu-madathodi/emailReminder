import json
from path_helper import resource_path


#1.function to find mailIDs
def find_mailID(team_name):
    with open(resource_path('data/teams.json'),'r') as file:
        data = json.load(file)

    for group_name, info in data.items():
        if group_name.lower() == team_name.lower():
            team_mail = info['team_mail']
            dl_mail = info['cc']['dl_mail']
            return team_mail, dl_mail

    raise ValueError("No such team found!")


#2.function to modify template
def create_template(team_name, incident_id, user_name='Vishnu MR'):

    subject = "P2 incident: " + incident_id

    with open(resource_path("templates/reminderTemplate.html"),"r", encoding="utf-8") as f:
        template_content = f.read()

    values = {
        "team_name": team_name,
        "incident_id": incident_id,
        "user_name": user_name,
    }

    for key, value in values.items():
        template_content = template_content.replace(f"{{{{{key}}}}}", value)

    return subject, template_content