from src.main.models.labour import Labour
from src.main.models.mistri import Mistri

class PersonFactory:
    @staticmethod
    def create_person(person_type, **kwargs):
        person_type = person_type.lower()

        if person_type == "labour":
            return Labour(
                kwargs.get("first_name"),
                kwargs.get("last_name"),
                kwargs.get("wage"),
                kwargs.get("role"),
            
            )

        elif person_type == "mistri":
            return Mistri(
                kwargs.get("first_name"),
                kwargs.get("last_name"),
                kwargs.get("wage"),
                kwargs.get("role"),
                kwargs.get("skill", [],),
            
            )

        else:
            raise ValueError(f"Invalid person type: {person_type}")