import pytest

def payload(equipment_id = 4, student_id = "ST-AB1234", priotity = 2):
    return{
        equipment_id : int=Field(gt=0)
        student_id : student_idStr
        description : descriptionStr
        priority : int=Field(gt=1,lt=6)
    }