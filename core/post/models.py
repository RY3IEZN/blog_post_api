from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Post(Base):
    __tablename__ = "post"

    id = Column(UUID(as_uuid=TabError), primary_key=True, default=uuid.uuid4)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
