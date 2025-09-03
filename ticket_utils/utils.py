from jinja2 import Environment, PackageLoader, select_autoescape
from ticket_utils.models import Ticket


def create_parse_header(ticket: Ticket) -> str:
    """
    Create the parse header for a ticket. This header allows an email to be parsed into a ticket.
    :param ticket: The Ticket object containing the ticket details.
    :return: A string formatted as a parse header.
    """
    header = [f'{k}:{v}' for k, v in ticket.model_dump().items()]
    return """
PARSE_START
{0}
PARSE_END

    """.format('\n'.join(header))


def generate_text(template, **kwargs):
    """
    Generate text from a Jinja2 template.
    :param template: The name of the template to render.
    :param kwargs: Keyword arguments to pass to the template.
    :return: Rendered text from the template.
    """
    env = Environment(loader=PackageLoader("ticket_utils"),
                      autoescape=select_autoescape())
    template = env.get_template(f"{template}.j2")
    return template.render(**kwargs)


def create_ticket_header(short_description, close_notes, contact, affected_client, 
                         assigned_to, u_business_service=None, watcher=None, 
                         parent_ticket_id=None):
    """
    Create a ticket object with the provided parameters.

    :param short_description: A short description of the ticket.
    :param close_notes: Notes to be added when closing the ticket.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned
    :param u_business_service: The business service related to the ticket
    :param watcher: A list of UTLNs to be added to the watch list.
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A Ticket object."""
    ticket = Ticket(
        u_contact_person=contact,
        caller_id=affected_client,
        short_description=short_description,
        assigned_to=assigned_to,
        close_notes=close_notes)
    if u_business_service:
        ticket.u_business_service = u_business_service
    if parent_ticket_id:
        ticket.parent = parent_ticket_id
    if watcher:
        ticket.watch_list = watcher
    return create_parse_header(ticket)
