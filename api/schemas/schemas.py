from pydantic import BaseModel
from typing import Union, Optional

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

class TokenBase(BaseModel):
  token: str
  user_id: int

class ChangePassword(BaseModel):
  user_id: int
  password: str

class AnalysisBase(BaseModel):
  identifier: str
  data: str

class NewAnalysis(AnalysisBase):
  price: float

class Analysis(NewAnalysis):
  id: int

  class Config:
    from_attributes = True

class AnalysisByDetail(AnalysisBase):
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


class NewAnimal(BaseModel):
  name: str
  requested_by: str
  specie: str

class Animal(NewAnimal):
  patient_id: int
  
  class Config:
    from_attributes = True


class HumanBase(BaseModel):
  name: str
  last_name: str
  maternal_surname: str | None = None
  age: int

class NewHuman(HumanBase):
  gender_id:int

class Human(HumanBase):
  patient_id: int
  gender: Gender

  class Config:
    from_attributes = True

class ResultBase(BaseModel):
  result: str

class NewResult(ResultBase):
  detail_id: int

class Result(NewResult):
  id: int

  class Config:
    from_attributes = True

class ResultByDetail(ResultBase):
  id: int

  class Config:
    from_attributes = True

class DetailBase(BaseModel):
  price: float
  done: int = 0

class NewDetail(DetailBase):
  analysis_id:int

class Detail(DetailBase):
  id: int
  request_id: int
  analysis: AnalysisByDetail
  result: ResultByDetail | None

  class Config:
    from_attributes = True

class RequestBase(BaseModel):
  date: str
  total: float
  paid: int = 0

class NewRequest(RequestBase):
  details: list[NewDetail] = []

class Request(RequestBase):
  id: int
  details: list[Detail] = []

  class Config:
    from_attributes = True

class Request2(RequestBase):
  id: int
  patient_id: int
  details: list[Detail] = []

  class Config:
    from_attributes = True

class PatientBase(BaseModel):
  email: str | None = None
  phone_number: str | None = None

class UpdatePatient(PatientBase):
  type_id: int | None = None
  animal: NewAnimal | None = None
  human: NewHuman | None = None

class NewPatient(UpdatePatient):
  patient_id: int | None = None
  requests: NewRequest

class Patient2(PatientBase):
  id: int
  patient_type: PatientType
  animal: Animal | None
  human: Human | None

  class Config:
    from_attributes = True

class Patient(PatientBase):
  requests: list[Request] = []

  class Config:
    from_attributes = True
