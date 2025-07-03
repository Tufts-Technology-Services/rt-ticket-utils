from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List


class Ticket(BaseModel):    
    model_config = ConfigDict(extra='forbid', str_strip_whitespace=True)
    u_incident_type: str = 'Request'
    u_contact_person: str
    caller_id: str
    source: str = 'Email'
    category: str = 'Research'
    subcategory: str = 'Research Systems'
    u_business_service: str = 'High Performance Computing (HPC)'
    short_description: str = Field(..., alias='Short_Description')
    assigned_to: str
    assignment_group: str = 'TTS Research Technology'
    parent: Optional[str] = None
    watch_list: Optional[List[str]] = None
    u_action: str = 'Activate/Setup/Install'
    state: str = 'Resolved'
    close_code: str = 'Resolved Remotely'
    close_notes: str
    message: str
