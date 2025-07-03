
from ticket_utils.models import Ticket
from jinja2 import Environment, PackageLoader, select_autoescape



def create_parse_header(header_dict):
    header = [f'{k}:{v}' for k, v in header_dict.items()]
    return f"""
    PARSE_START
    {'\n'.join(header)}
    PARSE_END
    """

def create_ticket_text(header_dict, message):
    return create_parse_header(header_dict) + message


def generate_text(template, **kwargs):
    env = Environment(loader=PackageLoader("ticket_utils"), autoescape=select_autoescape())
    template = env.get_template(f"{ template }.j2")
    return template.render(**kwargs)


def hpc_added_to_group_ticket_text(project_path, user_path, group_name):
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_added_to_group_notification', path=project_path, user_path=user_path, group=group_name, notifications=notifications, footer=footer)
    return t


def hpcvast_project_ticket_text(project_path, quota):
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_storage', path=project_path, quota=quota, notifications=notifications, footer=footer)
    return t


def hpcvast_increase_ticket_text(project_path, quota):
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_storage_update', path=project_path, quota=quota, notifications=notifications, footer=footer)
    return t


def rstore_share_ticket_text(share_name, quota, owner, group, approvers=()):
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    instructions = generate_text('map_smb_drive', share_name=share_name)
    t = generate_text('rstore_share', share_name=share_name, quota=quota, owner=owner, group=group, approvers=', '.join(approvers), 
                      notifications=notifications, footer=footer, instructions=instructions)
    return t


def rstore_increase_ticket_text(project_path, quota):
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('rstore_storage_update', path=project_path, quota=quota, notifications=notifications, footer=footer)
    return t