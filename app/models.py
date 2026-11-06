from sqlalchemy  import Integer, String
from sqlalchemy.orm import Base, Mapped, mapped_column

class ticket_db(Base):
    __tablename__ = "Maintenence_Log"
    id : Mapped[int]=mapped_column(primary_key=True, index= True)
    eqipment_id : Mapped[int]=mapped_column(Integer,nullable=False)
    student_id : Mapped[str]=mapped_column(String(10), unique=True,nullable=False)
    description : Mapped[str]=mapped_column(String(100))
    priority : Mapped[int]=mapped_column(Integer,nullable=False)
    status: Mapped[str]=mapped_column(nullable=False,default="OPEN")

