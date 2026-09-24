from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, Text
from sqlalchemy.orm import relationship
from app.database import Base

project_technology = Table(
    "project_technology",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id")),
    Column("technology_id", Integer, ForeignKey("technologies.id"))
)

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    bio = Column(Text)
    github_url = Column(String(255))
    projects = relationship("Project", back_populates="owner", cascade="all, delete")

class Technology(Base):
    __tablename__ = "technologies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    repo_url = Column(String(255), nullable=False)
    profile_id = Column(Integer, ForeignKey("profiles.id"), nullable=False)
    stars = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)
    owner = relationship("Profile", back_populates="projects")
    technologies = relationship("Technology", secondary=project_technology)
    feedbacks = relationship("Feedback", back_populates="project", cascade="all, delete")

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, index=True)
    note = Column(Integer, nullable=False)
    comments = Column(Text, nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    project = relationship("Project", back_populates="feedbacks")
