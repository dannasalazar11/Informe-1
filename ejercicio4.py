hora_0 = [int(input("Ingrese la hora: ")), int(input("Ingrese los minutos: ")), int(input("Ingrese los minutos transcurridos: "))]

minutos = hora_0[1]+hora_0[2]
horas   = (hora_0[0] + minutos//60) % 24
minutos = minutos % 60

print("La hora final será ", horas, ":", minutos) 

