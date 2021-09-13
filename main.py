from methods import *
from datetime import *

    
#   Monday schedule -- TODO
while current_weekday() == 0:
    subjects = ["Português", "Filosofia",  "Química", "Fisica", "Arte", "Matemática", "Educação Física"]
    classes_time = ["07:20:00", "08:05:00", "09:00:00", "09:45:00", "10:40:00", "11:25:00", "12:10:00"]
    start_signing(classes_time, subjects)

#   Tuesday schedule -- TODO
while current_weekday() == 1:
    subjects = ["História", "Inglês",  "Química", "Matemática", "Biologia", "Redação", "Arte"]
    classes_time = ["07:20:00", "08:05:00", "08:50:00", "09:35:00", "10:40:00", "11:25:00", "12:10:00"]

#   Wednesday schedule -- DONE
while current_weekday() == 2:
    subjects = ["Português", "Inglês",  "Geografia", "Biologia", "Fisica", "História"]
    classes_time = ["07:20:00", "08:05:00", "08:50:00", "09:35:00", "10:40:00", "11:25:00"]

#   Thursday schedule -- TODO
while current_weekday() == 3:
    pass
    
#   Friday schedule -- TODO
while current_weekday() == 4:
    pass
    