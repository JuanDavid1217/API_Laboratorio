from sqlalchemy.orm import Session
from models import models
from schemas import schemas

#### LOGIN FUNCTIONS ####

def create_account(db: Session, user: schemas.NewUser):
  try:
    new_user = models.User(user_name = user.user_name, password= user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def login(db: Session, user: schemas.NewUser):
  exists = db.query(models.User).filter(models.User.user_name == user.user_name).filter(models.User.password == user.password).first()
  return exists

##### SAMPLES FUNCTIONS #####

def save_sample(db: Session, sample: schemas.NewSample):
  try:
    new_sample = models.Sample(description = sample.description)
    db.add(new_sample)
    db.commit()
    db.refresh(new_sample)
    return new_sample
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_sample(db:Session, sample_id: int, sample = schemas.NewSample):
  created_sample = db.query(models.Sample).filter(models.Sample.id == sample_id).first()
  if created_sample is None:
    return None
  try:
    created_sample.description = sample.description
    db.commit()
    db.refresh(created_sample)
    return created_sample
  except Exception as e:
    print(e)
    raise e

def delete_sample(db:Session, sample_id:int):
  try:
    exists = db.query(models.Sample).filter(models.Sample.id == sample_id).first()
    if exists is None:
      return None
    db.delete(exists)
    db.commit()
  except Exception as e:
    print(e)
    raise e

def get_samples(db:Session):
  samples = db.query(models.Sample).all()
  return samples

#### MEASUREMENT UNITS FUNCTIONS ####

def save_unit(db: Session, unit: schemas.NewMeasurementUnit):
  try:
    new_unit = models.MeasurementUnit(description = unit.description)
    db.add(new_unit)
    db.commit()
    db.refresh(new_unit)
    return new_unit
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_unit(db:Session, unit_id: int, unit = schemas.NewMeasurementUnit):
  created_unit = db.query(models.MeasurementUnit).filter(models.MeasurementUnit.id == unit_id).first()
  if created_unit is None:
    return None
  try:
    created_unit.description = unit.description
    db.commit()
    db.refresh(created_unit)
    return created_unit
  except Exception as e:
    print(e)
    raise e

def delete_unit(db:Session, unit_id:int):
  try: 
    exists = db.query(models.MeasurementUnit).filter(models.MeasurementUnit.id == unit_id).first()
    if exists is None:
      return None
    db.delete(exists)
    db.commit()
  except Exception as e:
    print(e)
    raise e

def get_units(db:Session):
  units = db.query(models.MeasurementUnit).all()
  return units

#### USED METHODS FUNCTIONS ####

def save_method(db: Session, method: schemas.NewMethod):
  try:
    new_method = models.Method(description = method.description)
    db.add(new_method)
    db.commit()
    db.refresh(new_method)
    return new_method
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_method(db:Session, method_id: int, method = schemas.NewMethod):
  created_method = db.query(models.Method).filter(models.Method.id == method_id).first()
  if created_method is None:
    return None
  try:
    created_method.description = method.description
    db.commit()
    db.refresh(created_method)
    return created_method
  except Exception as e:
    print(e)
    raise e

def delete_method(db:Session, method_id:int):
  try:
    exists = db.query(models.Method).filter(models.Method.id == method_id).first()
    if exists is None:
      return None
    db.delete(exists)
    db.commit()
  except Exception as e:
    print(e)
    raise e

def get_methods(db:Session):
  methods = db.query(models.Method).all()
  return methods

#### ANALISYS FUNCTIONS ####

def save_analisys(db: Session, analisys: schemas.NewAnalysis):
  try:
    new_analisys = models.Analysis(identifier = analisys.identifier,
                                   price = analisys.price,
                                   data = analisys.data)
    db.add(new_analisys)
    db.commit()
    db.refresh(new_analisys)
    return new_analisys
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_analisys(db:Session, analisys_id: int, analisys = schemas.NewMethod):
  created_analisys = db.query(models.Analysis).filter(models.Analysis.id == analisys_id).first()
  if created_analisys is None:
    return None
  try:
    created_analisys.identifier = analisys.identifier
    created_analisys.price = analisys.price
    created_analisys.data = analisys.data
    db.commit()
    db.refresh(created_analisys)
    return created_analisys
  except Exception as e:
    print(e)
    raise e

def delete_analisys(db:Session, analisys_id:int):
  try:
    exists = db.query(models.analisys).filter(models.Analysis.id == analisys_id).first()
    if exists is None:
      return None
    db.delete(exists)
    db.commit()
  except Exception as e:
    print(e)
    raise e

def get_analisys(db:Session):
  analisys = db.query(models.Analysis).all()
  return analisys

#### GENDER FUNCTIONS ####

def save_gender(db: Session, gender: schemas.NewGender):
  try:
    new_gender = models.Gender(description = gender.description)
    db.add(new_gender)
    db.commit()
    db.refresh(new_gender)
    return new_gender
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_gender(db:Session, gender_id: int, gender = schemas.NewGender):
  created_gender = db.query(models.Gender).filter(models.Gender.id == gender_id).first()
  if created_gender is None:
    return None
  try:
    created_gender.description = gender.description
    db.commit()
    db.refresh(created_gender)
    return created_gender
  except Exception as e:
    print(e)
    raise e

def delete_gender(db:Session, gender_id:int):
  try:
    exists = db.query(models.Gender).filter(models.Gender.id == gender_id).first()
    if exists is None:
      return None
    db.delete(exists)
    db.commit()
  except Exception as e:
    print(e)
    raise e

def get_gender(db:Session):
  genders = db.query(models.Gender).all()
  return genders

#### PATIENT TYPES FUNCTIONS ####

def save_patient_type(db: Session, patient_type: schemas.NewPatientType):
  try:
    new_type = models.PatientType(description = patient_type.description)
    db.add(new_type)
    db.commit()
    db.refresh(new_type)
    return new_type
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_patient_type(db:Session, type_id: int, patient_type = schemas.NewPatientType):
  created_type = db.query(models.PatientType).filter(models.PatientType.id == type_id).first()
  if created_type is None:
    return None
  try:
    created_type.description = patient_type.description
    db.commit()
    db.refresh(created_type)
    return created_type
  except Exception as e:
    print(e)
    raise e

def delete_patient_type(db:Session, type_id:int):
  try:
    exists = db.query(models.PatientType).filter(models.PatientType.id == type_id).first()
    if exists is None:
      return None
    db.delete(exists)
    db.commit()
    return True
  except Exception as e:
    print(e)
    raise e

def get_patient_types(db:Session):
  types = db.query(models.PatientType).all()
  return types

#### REQUEST FUNCTIONS ####
def get_all_requests(db:Session):
  requests = db.query(models.Request).all()
  return requests

def save_request(db:Session, request: schemas.NewPatient):
  try:
    patient_id = request.patient_id
    if patient_id is None:
      new_patient = models.Patient(email = request.email,
                                  phone_number = request.phone_number,
                                  type_id= request.type_id)
      db.add(new_patient)
      db.flush()

      new_animal_human = None

      if request.animal is not None:
        new_animal_human = models.Animal(patient_id = new_patient.id,
                                         name = request.animal.name,
                                         requested_by = request.animal.requested_by,
                                         specie = request.animal.specie)
      else:
        new_animal_human = models.Human(patient_id = new_patient.id,
                                        name = request.human.name,
                                        last_name = request.human.last_name,
                                        maternal_surname = request.human.maternal_surname,
                                        age = request.human.age,
                                        gender_id = request.human.gender_id)
      db.add(new_animal_human)
      db.flush()
      patient_id = new_animal_human.patient_id
      
    details = request.requests.details

    new_request = models.Request(patient_id = patient_id,
                                 date = request.requests.date,
                                 total = request.requests.total,
                                 paid = request.requests.paid)
    db.add(new_request)
    db.flush()

    for detail in details:
      new_detail = models.RequestDetail(request_id = new_request.id,
                                        analysis_id = detail.analisys_id,
                                        price = detail.price,
                                        done= detail.done)
      db.add(new_detail)
      db.flush()
    db.commit()
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def add_detail(db:Session, request_id: int, new_detail: schemas.NewDetail):
  try:
    request = db.query(models.Request).filter(models.Request.id == request_id).first()
    if request is None:
      return None
    detail = models.RequestDetail(request_id = request_id,
                                  analisys_id = new_detail.analisys_id,
                                  price = new_detail.price,
                                  done = new_detail.done)
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return detail
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def delete_detail(db:Session, request_id: int, analysis_id: int):
  try:
    detail = db.query(models.RequestDetail).filter(models.RequestDetail.request_id == request_id).filter(models.RequestDetail.analysis_id == analysis_id).first()
    if detail is None:
      return None
    db.delete(detail)
    db.commit()
    return True
  except Exception as e:
    print(e)
    raise e

def save_results(db: Session, result: schemas.NewResult):
  try:
    new_result = models.Result(detail_id = result.detail_id, result = result.result)
    bd.add(new_result)
    db.flush()
    detail = db.query(models.RequestDetail).filter(models.RequestDetail.id == result.detail_id).first()
    detail.done = 1
    db.commit()
    db.refresh(detail)
    db.refresh(new_result)
    return new_result
  except Exception as e:
    print(e)
    db.rollback()
    raise e

def update_result(db: Session, detail_id: int, new_result: schemas.ResultBase):
  try:
    result = db.query(models.Result).filter(models.Result.detail_id == detail_id).first()
    if result is None:
      return None
    result.result = new_result.result
    db.commit()
    db.refresh(result)
    return result
  except Exception as e:
    print(e)
    raise e

def delete_result(db: Session, detail_id: int):
  try:
    result = db.query(models.Result).filter(models.Result.detail_id == detail_id).first()
    if result is None:
      return None
    db.delete(result)
    db.flush()
    detail = db.query(models.RequestDetail).filter(models.RequestDetail.id == detail_id).first()
    detail.done = 0
    db.commit()
    db.refresh(detail)
    return True
  except Exception as e:
    print(e)
    raise e

def get_patients(db: Session):
  data = db.query(models.Patient).all()
  return data

def update_patient(db:Session, patient_id: int, new_patient: schemas.UpdatePatient):
  try:
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient is None:
      return None
    patient.email = new_patient.email
    patient.phone_number = new_patient.phone_number
    if patient.type_id == 1:
      patientType = patient.animal
      patientType.name = new_patient.animal.name
      patientType.requested_by = new_patient.animal.requested_by
      patientType.specie = new_patient.animal.specie
    else:
      patientType = patient.human
      patientType.name = new_patient.human.name
      patientType.last_name = new_patient.human.last_name
      patientType.maternal_surname = new_patient.human.maternal_surname
      patient_type.age = new_patient.human.age
      patientType.gender_id = new_patient.human.gender_id
    patient.type_id = new_patient.type_id
    db.commit()
    db.refresh(patient)
    return patient
  except Exception as e:
    print(e)
    raise e
