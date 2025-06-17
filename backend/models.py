from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from backend.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    campaigns = relationship("Campaign", back_populates="user")
    sources = relationship("Source", back_populates="user")

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    source_type = Column(Integer)  # Тип источника
    is_active = Column(Boolean, default=True)
    last_scan_date = Column(DateTime, nullable=True)
    scan_start_date = Column(DateTime, nullable=True)
    scan_end_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="sources")

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="campaigns")
    reports = relationship("Report", back_populates="campaign")

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    report_type = Column(String)
    created_at = Column(DateTime)
    data = Column(String)  # JSON данные отчета
    
    campaign = relationship("Campaign", back_populates="reports") 