from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from model.base import Base



class Admin(Base):

    __tablename__ = "admin"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    senha = Column(String(100))
    email = Column(String(150), unique=True)

    def to_dict(self):
        return {
            "id": str(self.id),
            "senha": self.senha,
            "usemail": self.email
        }