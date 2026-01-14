from mail_builder import create_template, find_mailID
from outlook import generate_draft
from logger import logger

def main():
    team_name = input("Enter the team name: ").strip()
    incident_id = input("Enter the incident id: ").strip()
    #user_name = input("Enter the sender name: ").strip()

    #create to and cc emails
    try:
        to, cc = find_mailID(team_name)
        cc_list = list()
        cc_list.extend([cc,"pratap.chauhan@dxc.com", "poonam.rane@dxc.com", "Security.admin@bankofbarod.co.in","security.operator@bankofbaroda.co.in"])
    except Exception as e: 
        logger.exception(f"Failed to find team and CC: {e}")
        return False

    #create template
    subject, template = create_template(team_name,incident_id)

    #generate outlook draft
    try:
        generate_draft(to, cc_list, subject, template)
    except Exception as e:
        logger.exception(f"Failed to draft mail: {e}")
        return False

if __name__ == "__main__":
    main()