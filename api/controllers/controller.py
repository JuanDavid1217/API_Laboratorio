from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from cruds import crud
from schemas import schemas
from fastapi import APIRouter
from dbconnection import get_db
from typing import List

def global_exception_handler(exc: Exception):
    if isinstance(exc, HTTPException):
        raise exc
    raise HTTPException(status_code=409, detail=str(exc))

router = APIRouter()

@router.post("/account/login", response_model = schemas.User)
def login(new_user: schemas.NewUser, db: Session = Depends(get_db)):
  try:
    user = crud.login(db, new_user)
    if user is None:
      raise HTTPException(status_code = 401, detail = "Usuario o Contraseña Inválidos.") 
    return user
  except Exception as e:
    global_exception_handler(e)

@router.post("/account/create_acount", response_model = schemas.User)
def create_account(new_user: schemas.NewUser, db: Session = Depends(get_db)):
  try:
    user = crud.create_account(db, new_user)
    return user
  except Exception as e:
    global_exception_handler(e)


@router.get("/samples", response_model = List[schemas.Sample])
def get_samples(db: Session = Depends(get_db)):
  return crud.get_samples(db)

@router.post("/samples", response_model = schemas.Sample)
def save_sample(new_sample: schemas.NewSample, db: Session = Depends(get_db)):
  try:
    sample = crud.save_sample(db, new_sample)
    return sample
  except Exception as e:
    global_exception_handler(e)

@router.put("/samples/{sample_id}", response_model = schemas.Sample)
def update_sample(sample_id: int, new_sample: schemas.NewSample, db: Session = Depends(get_db)):
  try:
    sample = crud.update_sample(db, sample_id, sample)
    if sample is None:
      raise HTTPException(status_code = 404, detail = "Muestra no encontrada.")
    return sample
  except Exception as e:
    global_exception_handler(e)

@router.delete("/samples/{sample_id}")
def delete_sample(sample_id: int, db: Session = Depends(get_db)):
  try:
    if crud.delete_sample(db, sample_id) is None:
      raise HTTPException(status_code = 404, detail = "Muestra no encontrada.")
  except Exception as e:
    global_exception_handler(e)


@router.get("/measurement_units", response_model = List[schemas.MeasurementUnit])
def get_units(db: Session = Depends(get_db)):
  return crud.get_units(db)

@router.post("/measurement_units", response_model = schemas.MeasurementUnit)
def save_unit(new_unit: schemas.NewMeasurementUnit, db: Session = Depends(get_db)):
  try:
    unit = crud.save_unit(db, new_unit)
    return unit
  except Exception as e:
    global_exception_handler(e)

@router.put("/measurement_units/{unit_id}", response_model = schemas.MeasurementUnit)
def update_unit(unit_id: int, new_unit: schemas.NewMeasurementUnit, db: Session = Depends(get_db)):
  try:
    unit = crud.update_unit(db, unit_id, new_unit)
    if unit is None:
      raise HTTPException(status_code = 404, detail = "Unidad de medida no encontrada.")
    return unit
  except Exception as e:
    global_exception_handler(e)

@router.delete("/measurement_units/{unit_id}")
def delete_unit(unit_id:int, db: Session = Depends(get_db)):
  try:
    if crud.delete_unit(db, unit_id) is None:
      raise HTTPException(status_code = 404, detail = "Unidad de medida no encontrada.")
  except Exception as e:
    global_exception_handler(e)


@router.get("/methods", response_model = List[schemas.Method])
def get_methods(db: Session = Depends(get_db)):
  return crud.get_methods(db)

@router.post("/mothods", response_model = schemas.Method)
def save_method(new_method: schemas.NewMethod, db: Session = Depends(get_db)):
  try:
    method = crud.save_method(db, new_method)
    return method
  except Exception as e:
    global_exception_handler(e)

@router.put("/methods/{method_id}", response_model = schemas.Method)
def update_method(method_id: int, new_method: schemas.NewMethod, db: Session = Depends(get_db)):
  try:
    method = crud.update_method(db, method_id, new_method)
    if method is None:
      raise HTTPException(status_code = 404, detail = "Método no encontrado.")
    return method
  except Exception as e:
    global_exception_handler(e)

@router.delete("/methods/{method_id}")
def delete_method(method_id:int, db:Session = Depends(get_db)):
  try:
    if crud.delete_method(db, method_id) is None:
      raise HTTPException(status_code = 404, detail = "Método no encontrado.")
  except Exception as e:
    global_exception_handler(e)


@router.get("/analisys", response_model = List[schemas.Analysis])
def get_analisys(db: Session = Depends(get_db)):
  return crud.get_analisys(db)

@router.post("/analisys", response_model = schemas.Analysis)
def save_analisys(new_analisys: schemas.NewAnalysis, db: Session = Depends(get_db)):
  try:
    analisys = crud.save_analisys(db, new_analisys)
    return analisys
  except Exception as e:
    global_exception_handler(e)

@router.put("/analisys/{analisys_id}", response_model = schemas.Analysis)
def update_analisys(analisys_id: int, new_analisys: schemas.NewAnalysis, db: Session = Depends(get_db)):
  try:
    analisys = crud.update_analisys(db, analisys_id, new_analisys)
    if analisys is None:
      raise HTTPException(status_code = 404, detail = "Análisis no encontrado.")
    return analisys
  except Exception as e:
    global_exception_handler(e)

@router.delete("/analisys/{analisys_id}")
def delete_analisys(analisys_id: int, db: Session = Depends(get_db)):
  try:
    if crud.delete_analisys(db, analisys_id) is None:
      raise HTTPException(status_code = 404, detail = "Análisis no encontrado.")
  except Exception as e:
    global_exception_handler(e)


@router.get("/genders", response_model = List[schemas.Gender])
def get_gender(db: Session = Depends(get_db)):
  return crud.get_gender(db)

@router.post("/genders", response_model = schemas.Gender)
def save_gender(new_gender: schemas.NewGender, db: Session = Depends(get_db)):
  try:
    gender = crud.save_gender(db, new_gender)
    return gender
  except Exception as e:
    global_exception_handler(e)

@router.put("/genders/{gender_id}", response_model = schemas.Gender)
def update_gender(gender_id: int, new_gender: schemas.NewGender, db: Session = Depends(get_db)):
  try:
    gender = crud.update_gender(db, gender_id, new_gender)
    if gender is None:
      raise HTTPException(status_code=404, detail = "Genero no encontrado.")
    return gender
  except Exception as e:
    global_exception_handler(e)

@router.delete("/genders/{gender_id}")
def delete_gender(gender_id: int, db: Session = Depends(get_db)):
  try:
    if crud.delete_gender(db, gender_id) is None:
      raise HTTPException(status_code=404, detail = "Genero no encontrado.")
  except Exception as e:
    global_exception_handler(e)


@router.get("/patient_types", response_model = List[schemas.PatientType])
def get_patient_types(db: Session = Depends(get_db)):
  return crud.get_patient_types(db)

@router.post("/patient_types", response_model = schemas.PatientType)
def save_patient_type(new_type: schemas.NewPatientType, db: Session = Depends(get_db)):
  try:
    patient_type = crud.save_patient_type(db, new_type)
    return patient_type
  except Exception as e:
    global_exception_handler(e)

@router.put("/patient_types/{type_id}", response_model = schemas.PatientType)
def update_patient_type(type_id: int, new_type: schemas.NewPatientType, db: Session = Depends(get_db)):
  try:
    patient_type = crud.update_patient_type(db, type_id, new_type)
    if patient_type is None:
      raise HTTPException(status_code=404, detail = "Tipo de paciente no encontrado.")
    return patient_type
  except Exception as e:
    global_exception_handler(e)

@router.delete("/patient_types/{type_id}")
def delete_patient_type(type_id: int, db: Session = Depends(get_db)):
  try:
    if crud.delete_patient_type(db, type_id) is None:
      raise HTTPException(status_code=404, detail = "Tipo de paciente no encontrado.")
  except Exception as e:
    global_exception_handler(e)


@router.get("/requests", response_model = List[schemas.Request2])
def get_all_requests(db: Session = Depends(get_db)):
  return crud.get_all_requests(db)

@router.post("/requests", response_model = schemas.Patient)
def save_request(new_request: schemas.NewPatient, db: Session = Depends(get_db)):
  try:
    request = crud.save_request(db, new_request)
    return request
  except Exception as e:
    global_exception_handler(e)

@router.post("/requests/details", response_model = schemas.Detail)
def add_detail(request_id: int, new_detail: schemas.NewDetail, db: Session = Depends(get_db)):
  try:
    detail = crud.add_detail(db, request_id, new_detail)
    if detail is None:
      raise HTTPException(status_code=404, detail= 'Solicitud de Análisis no encontrada.')
    return detail
  except Exception as e:
    global_exception_handler(e)

@router.delete("/requests/details/{request_id}/{analysis_id}")
def delete_detail(request_id: int, analysis_id: int, db: Session = Depends(get_db)):
  try:
    if crud.delete_detail(db, request_id, analysis_id) is None:
      raise HTTPException(status_code=404, detail='El análisis no se encuuentra registrado en la solicitud.')
  except Exception as e:
    global_exception_handler(e)

@router.post("/results", response_model = schemas.Result)
def save_results(new_result: schemas.NewResult, db: Session = Depends(get_db)):
  try:
    result = crud.save_results(db, new_result)
    return result
  except Exception as e:
    global_exception_handler(e)

@router.put("/results/{detail_id}", response_model = schemas.Result)
def update_result(detail_id: int, result: schemas.NewResult, db: Session = Depends(get_db)):
  try:
    result_updated = crud.update_result(db, detail_id, result)
    if result_updated is None:
      raise HTTPException(status_code = 404, detail = 'Resultado no encontrado.')
    return result_updated
  except Exception as e:
    global_exception_handler(e)

@router.delete("/results/{detail_id}")
def delete_result(detail_id: int, db: Session = Depends(get_db)):
  try:
    if crud.delete_result(db, detail_id) is None:
      raise HTTPException(status_code = 404, detail = 'Resultado no encontrado.')
  except Exception as e:
    global_exception_handler(e)

@router.get("/patients", response_model=list[schemas.Patient2])
def get_patients(db:Session = Depends(get_db)):
  return crud.get_patients(db)

@router.put("/patients", response_model = schemas.Patient2)
def update_patient(patient_id: int, new_patient: schemas.UpdatePatient, db: Session=Depends(get_db)):
  try:
    patient = crud.update_patient(db, patient_id, new_patient)
    if patient is None:
      raise HTTPException(status_code=404, detail='Paciente no encontrado.')
    return patient
  except Exception as e:
    global_exception_handler(e)