import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    fhone_nomber: str
    date_of_birth: date
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str



