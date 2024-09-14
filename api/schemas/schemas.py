from pydantic import BaseModel
from typing import Union

class NewSample(BaseModel):
  description:str

class Sample(NewSample):
  id: int

  class Config:
    from_attributes = True


class NewMeasurementUnit(BaseModel):
  description: str

class MeasurementUnit(NewMeasurementUnit):
  id: int

  class Config:
    from_attributes = True


class UserBase(BaseModel):
  user_name: str

class NewUser(UserBase):
  password: str

class User(UserBase):
  id: int

  class Config:
    from_attributes = True


class NewAnalysis(BaseModel):
  identifier: str
  price: float
  data: str

class Analysis(NewAnalysis):
  id: int

  class Config:
    from_attributes = True


class NewMethod(BaseModel):
  description: str

class Method(NewMethod):
  id: int

  class Config:
    from_attributes = True


class NewGender(BaseModel):
  description: str

class Gender(NewGender):
  id: int

  class Config:
    from_attributes = True


class NewPatientType(BaseModel):
  description: str

class PatientType(NewPatientType):
  id: int

  class Config:
    from_attributes = True


class PatientBase(BaseModel):
  email: str
  phone_number: str

class NewPatient(PatientBase):
  type_id: int

class Patient(PatientBase):
  patient_type: PatientType

  class Config:
    from_attributes = True


class AnimalBase(BaseModel):
  name: str
  requested_by: str
  specie: str

class NewAnimal(AnimalBase):
  patient: NewPatient

class Animal(AnimalBase):
  patient_id: int
  patient: Patient

  class Config:
    from_attributes = True


class HumanBase(BaseModel):
  name: str
  last_name: str
  maternal_surname: str | None = None
  age: int

class NewHuman(HumanBase):
  patient: NewPatient
  gender_id:int

class Human(HumanBase):
  patient_id: int
  patient: Patient
  gender: Gender

  class Config:
    from_attributes = True


class DetailBase(BaseModel):
  price: float
  done: int = 0

class NewDetail(DetailBase):
  analysis_id:int

class Detail(DetailBase):
  id: int
  analysis: Analysis

  class Config:
    from_attributes = True

class RequestBase(BaseModel):
  date: str
  total: float
  paid: int = 0

class NewRequest(RequestBase):
  patient: Union[NewAnimal, NewHuman]
  details: list[NewDetail] = []

class NewRequestByPreviousPatient(RequestBase):
  patient_id: int
  details: list[NewDetail] = []

class Request(RequestBase):
  id: int
  patient: Patient
  details: list[Detail] = []

  class Config:
    from_attributes = True


class ResultBase(BaseModel):
  result: str

class NewResult(ResultBase):
  detail_id: int

class Result(RequestBase):
  detailt: Detail

  class Config:
    from_attributes = True
