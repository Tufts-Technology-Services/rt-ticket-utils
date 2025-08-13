from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Ticket(BaseModel):
    """Represents a ticket in the system."""    
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=True)
    u_incident_type: str = 'Request'
    u_contact_person: str  # requestor's utln
    caller_id: str  # requestor's utln; affected client
    source: str = 'Email'
    category: str = 'Research'
    subcategory: str = 'Research Systems'
    u_business_service: str = 'High Performance Computing (HPC)'
    short_description: str = Field(..., alias='Short_Description')
    assigned_to: str  # script user's utln
    assignment_group: str = 'TTS Research Technology'
    parent: Optional[str] = None  # parent ticket id
    watch_list: Optional[list[str]] = None  # PI utln
    u_action: str = 'Activate/Setup/Install'
    state: str = 'Resolved'
    close_code: str = 'Resolved Remotely'
    close_notes: str


"""
other attributes that can be used in the ticket:
 Location	location
 Room	u_alt_location
 Preferred Phone Number	u_call_back_number
 Major Incident 	u_major_incident 
 Priority	priority
 Due Date	due_date
 First Call Resolution	u_first_call_resolution
 Description	description
 Source	contact_type
 Configuration Item	cmdb_ci
 Sensitive Information	u_pi_checkbox
 Is Duplicate Incident	u_is_duplicate_incident
 Action	u_action
 Resolution Steps	close_notes
 KCS Soution	u_kcs_solution
 Resolution Code	close_code
 Additional Comments	comments
 Work notes	work_notes
 Work notes watch list	u_itil_watch_list
 Do Not Send Client Email	u_do_not_send_client_email
"""
