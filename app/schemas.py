from typing import Annotated

from pydantic import BaseModel, ConfigDict,EmailStr,Field,StringConstraints

student_idStr=Annotated[str,StringConstraints(pattern=R"^ST-AB\d{4}$")]
descriptionStr=Annotated[str,StringConstraints(min_length=5,max_length=100)]

class ticketCreate(BaseModel):
    equipment_id : int=Field(gt=0)
    student_id : student_idStr
    description : descriptionStr
    priority : int=Field(gt=1,lt=6)


class ticketRead(BaseModel):
    model_config= ConfigDict(from_attributes=True)
    id;int
    equipment_id:int
    student_id: student_idStr
    description : descriptionStr
    priority:int