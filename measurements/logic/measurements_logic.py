from datetime import datetime
from tkinter import Variable
from ..models import Measurement  

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement= Measurement(
        variable= new_var["variable"],
        value= new_var["value"],
        place = new_var["place"],
        date= datetime.now()
    )
    measurement.save()
    return measurement

def create_measurement(var):
    variable = Variable.objects.get(pk=var["variable"])
    measurement = Measurement(
        variable= variable,
        value = var["value"],
        unit = var["unit"],
        place = var["place"],
        date = datetime.now()
    )
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()
    return measurement
