from ticket_utils.utils import create_ticket_header, generate_text


def hpc_account_creation_ticket_text(project_path, user_path, 
                                     contact, affected_client, watcher, 
                                     assigned_to, parent_ticket_id=None):
    """
    Create ticket text for HPC account creation.

    :param project_path: The path of the project.
    :param user_path: The path of the user.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned.
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'HPC Account Creation | {user_path}',
        close_notes='Cluster account created!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_account_creation', user_path=user_path, 
                      project_path=project_path, 
                      pi_utln=affected_client, 
                      notifications=notifications, footer=footer)
    return ticket_header + t


def hpc_added_to_group_ticket_text(project_path, user_path, group_name,
                                   contact, affected_client, watcher,
                                   assigned_to, parent_ticket_id=None):
    """
    Create ticket text for adding a user to a project group and adding private directory.

    :param project_path: The path of the project.
    :param user_path: The path of the user.
    :param group_name: The name of the group.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f"Tier 1 HPC Storage: Grant Access to {user_path}",
        close_notes='Added user to group!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_added_to_group_notification', path=project_path, 
                      user_path=user_path, group=group_name, 
                      notifications=notifications, footer=footer)
    return ticket_header + t


def hpcvast_project_ticket_text(project_path: str, quota_gb: str, contact=None, 
                                affected_client=None, watcher=None, assigned_to=None, parent_ticket_id=None):
    """
    Create ticket text for creating a new HPC Vast project.

    :param project_path: The path of the project.
    :param quota_gb: The quota in GB for the project.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'Tier 1 HPC Storage: Creation | {quota_gb} GB | {project_path}',
        close_notes='Project storage created!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_storage', path=project_path, quota_gb=quota_gb, 
                      notifications=notifications, footer=footer)
    return ticket_header + t


def hpcvast_increase_ticket_text(project_path, quota_gb, 
                                 contact=None, affected_client=None, watcher=None, 
                                 assigned_to=None, parent_ticket_id=None):
    """ Create ticket text for increasing the quota of an existing HPC Vast project.

    :param project_path: The path of the project.
    :param quota_gb: The new quota in GB for the project.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned.
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'Tier 1 HPC Storage: Increase | {quota_gb} GB | {project_path}',
        close_notes='Quota increased!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('hpc_storage_update', path=project_path, quota=quota_gb, 
                      notifications=notifications, footer=footer)
    return ticket_header + t


def rstore_share_ticket_text(share_name, quota_gb, group=None, approvers=(), 
                             contact=None, affected_client=None, watcher=None,
                             assigned_to=None, parent_ticket_id=None):

    """
    Create ticket text for creating a new RStore share.

    :param share_name: The name of the share.
    :param quota_gb: The quota in GB for the share.
    :param group: The group to which the share belongs.
    :param approvers: List of approvers for the share.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'Tier 1 RStore Storage: Creation | {quota_gb} GB | {share_name}',
        close_notes='Share created!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    instructions = generate_text('map_smb_drive', share_name=share_name)
    t = generate_text('rstore_share', share_name=share_name, quota=quota_gb, owner=affected_client, 
                      group=group, approvers=', '.join(approvers), 
                      notifications=notifications, footer=footer, instructions=instructions)
    return ticket_header + t


def rstore_increase_ticket_text(share_name, quota_gb, 
                                contact=None, affected_client=None, watcher=None, 
                                assigned_to=None, parent_ticket_id=None):
    """
    Create ticket text for increasing the quota of an existing RStore share.
    :param share_name: The name of the share.
    :param quota_gb: The new quota in GB for the share.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'Tier 1 RStore Storage: Increase | {quota_gb} GB | {share_name}',
        close_notes='Quota increased!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    notifications = generate_text('notifications')
    t = generate_text('rstore_storage_update', path=share_name, quota=quota_gb, 
                      notifications=notifications, footer=footer)
    return ticket_header + t


def course_directory_ticket_text(course_path: str, quota_gb: str, course_group: str, 
                                 admin_group: str, contact=None, affected_client=None, watcher=None, 
                                 assigned_to=None, parent_ticket_id=None):
    """
    Create ticket text for creating a new course directory.

    :param course_path: The path of the course.
    :param quota_gb: The quota in GB for the course.
    :param course_group: The group name for the course.
    :param admin_group: The admin group name for the course.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the affected client.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned.
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'HPC Class Storage: Creation | {quota_gb} GB | {course_path}',
        close_notes='Course storage created!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    t = generate_text('hpc_course_storage', course_dir=course_path, quota_gb=quota_gb, 
                      course_group=course_group, admin_group=admin_group, footer=footer)
    return ticket_header + t


def course_add_ta_ticket_text(course_path: str, contact=None, affected_client=None, watcher=None, 
                              assigned_to=None, parent_ticket_id=None):
    """
    Create ticket text for adding a TA to an existing course.

    :param course_path: The path of the course.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the TA being added.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned.
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'HPC Class Storage: Add TA | {course_path}',
        close_notes='Course TA added!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    t = generate_text('hpc_course_add_ta', course_dir=course_path, course_name=course_path.split('/')[-1], 
                      ta_username=affected_client, footer=footer)
    return ticket_header + t


def course_add_student_ticket_text(course_path: str, contact=None, affected_client=None, watcher=None, 
                              assigned_to=None, parent_ticket_id=None):
    """
    Create ticket text for adding a student to an existing course.

    :param course_path: The path of the course.
    :param contact: The UTLN of the contact person (requestor).
    :param affected_client: The UTLN of the student being added.
    :param watcher: A list of UTLNs to be added to the watch list.
    :param assigned_to: The UTLN of the person to whom the ticket is assigned.
    :param parent_ticket_id: The ID of the parent ticket, if any.
    :return: A string containing the ticket text.
    """
    ticket_header = create_ticket_header(
        short_description=f'HPC Class Storage: Add Student | {course_path}',
        close_notes='Course Student added!',
        affected_client=affected_client, contact=contact, 
        assigned_to=assigned_to, watcher=watcher,
        parent_ticket_id=parent_ticket_id
    )
    footer = generate_text('footer')
    t = generate_text('hpc_course_add_student', course_dir=course_path, course_name=course_path.split('/')[-1], 
                      student_username=affected_client, footer=footer)
    return ticket_header + t
