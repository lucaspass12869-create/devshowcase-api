from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from.database import Base

project_technology = Table('project_technology', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('technology_id', Integer, ForeignKey('technologies.id'))
)

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    projects = relationship("Project", back_populates="owner")

class Technology(Base):
    __tablename__ = "technologies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    link = Column(String)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)
    owner = relationship("Profile", back_populates="projects")
    feedbacks = relationship("Feedback", back_populates="project")

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", back_populates="feedbacks")
