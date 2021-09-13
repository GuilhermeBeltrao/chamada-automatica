from methods import *
from datetime import *

    
#   Monday schedule 
while current_weekday() == 0:
    subjects = ["Português", "Filosofia",  "Química", "Fisica", "Arte", "Matemática", "Educação Física"]
    class_schedules = ["07:20:00", "08:05:00", "09:00:00", "09:45:00", "10:40:00", "11:25:00", "12:10:00"]
    start_signing(class_schedules, subjects)

#   Tuesday schedule 
while current_weekday() == 1:
    subjects = ["História", "Inglês",  "Química", "Matemática", "Biologia", "Redação", "Arte"]
    class_schedules = ["07:20:00", "08:05:00", "08:50:00", "09:35:00", "10:40:00", "11:25:00", "12:10:00"]
    start_signing(class_schedules, subjects)

#   Wednesday schedule 
while current_weekday() == 2:
    subjects = ["Português", "Inglês",  "Geografia", "Biologia", "Fisica", "História"]
    class_schedules = ["07:20:00", "08:05:00", "08:50:00", "09:35:00", "10:40:00", "11:25:00"]
    start_signing(class_schedules, subjects)

#   Thursday schedule 
while current_weekday() == 3:
    subjects = ["Sociologia", "Biologia",  "Português", "Química", "Matemática", "Geografia"]
    class_schedules = ["07:20:00", "08:05:00", "08:50:00", "09:35:00", "10:40:00", "11:25:00"]
    start_signing(class_schedules, subjects)
    
#   Friday schedule
while current_weekday() == 4:
    subjects = ["Matemática", "Sociologia",  "Geografia", "Fisica", "História", "Redação", "Português"]
    class_schedules = ["07:10:00", "07:55:00", "08:40:00", "09:45:00", "10:30:00", "11:25:00", "12:00:00"]
    start_signing(class_schedules, subjects)
    