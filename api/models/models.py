from sqlalchemy import Column, ForeignKey, Integer, String, Table, Float, Text, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sample(Base): #Crud already
  __tablename__ = "samples"
  id = Column(Integer, primary_key = True, autoincrement = True)
  description = Column(String(255), nullable = False, unique = True)

class MeasurementUnit(Base): #Crud already
  __tablename__ = "measurement_units"
  id = Column(Integer, primary_key = True, autoincrement = True)
  description = Column(String(255), nullable = False, unique = True)

class User(Base): #Only login
  __tablename__ = "users"
  id = Column(Integer, primary_key = True, autoincrement = True)
  user_name = Column(String(255), nullable = False, unique = True)
  password = Column(String(255), nullable = False)

class Analysis(Base): #Crud already
  __tablename__ = "analysis"
  id = Column(Integer, primary_key = True, autoincrement = True)
  identifier = Column(String(255), nullable = False, unique = True)
  price = Column(Float, nullable = False)
  data = Column(Text, nullable = False)

  details = relationship("RequestDetail", back_populates="analysis")

class Method(Base): #Crud already
  __tablename__ = "methods"
  id = Column(Integer, primary_key = True, autoincrement = True)
  description = Column(String(255), nullable = False, unique = True)

class Gender(Base): #Crud already
  __tablename__ = "genders"
  id = Column(Integer, primary_key = True, autoincrement = True)
  description = Column(String(255), nullable = False, unique = True)

  humans = relationship("Human", back_populates = "gender")

class PatientType(Base): #Crud already
  __tablename__ = "patient_types"
  id = Column(Integer, primary_key = True, autoincrement = True)
  description = Column(String(255), nullable = False, unique = True)
  
  patients = relationship("Patient", back_populates="patient_type")

class Patient(Base):
  __tablename__ = "patients"
  id = Column(Integer, primary_key = True, autoincrement = True)
  email = Column(String(255), nullable = False)
  phone_number = Column(String(255), nullable = False)
  type_id = Column(Integer, ForeignKey("patient_types.id"), nullable = False)
  
  patient_type = relationship("PatientType", back_populates="patients")
  animal = relationship("Animal", back_populates="patient", uselist=False)
  human = relationship("Human", back_populates = "patient", uselist=False)
  requests = relationship("Request", back_populates = "patient")

class Animal(Base):
  __tablename__ = "animals"
  patient_id = Column(Integer, ForeignKey("patients.id"), primary_key = True)
  name = Column(String(255), nullable = False)
  requested_by = Column(String(255), nullable = False)
  specie = Column(String(255), nullable = False)

  patient = relationship("Patient", back_populates="animal")

class Human(Base):
  __tablename__ = "humans"
  patient_id = Column(Integer, ForeignKey("patients.id"), primary_key = True)
  name = Column(String(255), nullable = False)
  last_name = Column(String(255), nullable = False)
  maternal_surname = Column(String(255), nullable = True)
  age = Column(Integer, nullable = False)
  gender_id = Column(Integer, ForeignKey("genders.id"), nullable = False)

  patient = relationship("Patient", back_populates = "human")
  gender = relationship("Gender", back_populates = "humans")

class Request(Base):
  __tablename__ = "requests"
  id = Column(Integer, primary_key = True, autoincrement = True)
  patient_id = Column(Integer, ForeignKey("patients.id"), nullable = False)
  date = Column(String(255), nullable = False)
  total = Column(Float, nullable = False)
  paid = Column(Integer, nullable = False)

  __table_args__ = (
    CheckConstraint('paid IN (0, 1)', name='check_paid'),
  )

  patient = relationship("Patient", back_populates="requests")
  details = relationship("RequestDetail", back_populates="request", cascade="all, delete")

class RequestDetail(Base):
  __tablename__ = "request_details"
  id = Column(Integer, primary_key = True, autoincrement = True)
  request_id = Column(Integer, ForeignKey("requests.id", ondelete="CASCADE"), nullable = False)
  analisys_id = Column(Integer, ForeignKey("analysis.id"), nullable = False)
  price = Column(Float, nullable = False)
  done = Column(Integer, nullable = False)

  __table_args__ = (
    CheckConstraint('done IN (0, 1)', name='check_done'),
    UniqueConstraint('request_id', 'analisys_id', name='unique_analysis_by_request')
  )

  request = relationship("Request", back_populates="details")
  analysis = relationship("Analysis", back_populates="details")
  result = relationship("Result", back_populates="detail", cascade="all, delete")

class Result(Base):
  __tablename__ = "results"
  id = Column(Integer, primary_key = True, autoincrement = True)
  detail_id = Column(Integer, ForeignKey("request_details.id", ondelete="CASCADE"), nullable = False, unique = True)
  result = Column(Text, nullable = False)

  detail = relationship("RequestDetail", back_populates="result")

  
