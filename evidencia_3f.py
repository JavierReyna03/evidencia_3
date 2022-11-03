import sys
import sqlite3
from sqlite3 import Error

while True:
    print("BIENVENIDO A ANDOR")
    print("******************")
    print("¿Que opcion desea realizar")
    print("1) Hacer una reservacion")
    print("2) Reportes de reservaciones")
    print("3) Registrar una sala")
    print("4) Registrar un cliente")
    print("5) Salir")
   
    respuesta = input("Ingrese la opcion deseada: ")
   
    res_int = int(respuesta)
   
    if res_int == 1:
   
        print("Bienvenido al menu de reservaciones")
        print("¿Que opcion desea realizar")
        print("1) Registrar una nueva reservacion")
        print("2) Modificar descripcion de una reservacion")
        print("3) Eliminar una reservacion")
        print("4) Volver al menu principal")
       
        res1 = input("Ingresa la opcion deseada: ")
       
        res_int1 = int(res1)
       
        if res_int1 == 1:
            print("ingresa los datos")
            idres = int(input("Ingresa el Id de la reservacion: "))
            idcli = int(input("Ingresa el Id del Ciente: "))
            idsal = int(input("Ingresa el Id de la sala: "))
            nom = input("Ingresa el nombre del evento: ")
            turn = input("Ingresa el turno del evento: ")
            fech = input("Ingresa la fecha del evento: ")
           
            try:
                with sqlite3.connect("Evidencia_3.db") as conn:
                    mi_cursor = conn.cursor()
                    valores = (idres, idcli, idsal, nom, turn, fech)
                    mi_cursor.execute("INSERT INTO Reservaciones VALUES(?, ?, ?, ?, ?, ?)",  valores)
                    print("REGISTRO AGREGADO EXITOSAMENTE")
                   
            except Error as e:
                print (e)
   
            except:
                print(f"se produjo el siguiente error: {sys.exc_info()[0]}")
   
            finally:
                conn.close()
           
        if res_int1 == 2:
            print("Actualizar datos")
            
            idd_res = int(input("Ingresa el id de la reservacion a modificar: "))
            
            try:
                with sqlite3.connect("Evidencia_3.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT * FROM Reservaciones WHERE ID_Reservacion = {idd_res}")
                    nuevo = input("Ingresa el nuevo nombre del evento: ")
                    update = {'nuevo' : nuevo, 'idd_res' : idd_res}
                    cursor.execute(f"UPDATE Reservaciones SET nombre_evento = :nuevo WHERE ID_Reservacion = :idd_res", update)
                    print("Cambios realizados correctamente")
                    
            except Error as e:
                print (e)
   
            except:
                print(f"se produjo el siguiente error: {sys.exc_info()[0]}")
   
            finally:
                conn.close()
                
        if res_int1 == 3:
            print("Borrar datos")
            borr = int(input("Ingresa el Id de la reservacion a eliminar"))
            
            try:
                with sqlite.connect("Evidencia_3.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"DELETE FROM Reservaciones WHERE ID_Reservacion = {borr}")
                    print("Reservacion eliminada correctamente")
               
            except Error as e:
                print (e)
   
            except:
                print(f"se produjo el siguiente error: {sys.exc_info()[0]}")
   
               
               
               
               
               
               
               
               
               
               
               
                
    elif res_int == 2:
        print("Bienvenido al menu de reportes")
        print("¿Que opcion desea realizar")
        print("1) Mostrar reportes en pantalla")
        print("2) Regresar al menu principal")
        
        reees = input("Ingrese la opcion deseada: ")
        
        reees_int = int(reees)
        
        if reees_int == 1:
            
            conn = sqlite3.connect('Evidencia_3.db')
            c = conn.cursor()
            
            def mostrar_datos():
                c.execute("SELECT * FROM Reservaciones")
                data = c.fetchall ()
                [print(row) for row in data]
            mostrar_datos()
       
    elif res_int == 3:
        print("Bienvenido al registro de salas")
        clv_sala = int(input("Ingresa el id de la sala: "))
        cupo = int(input("Ingresa el cupo de la sala: "))
        
        try:
            with sqlite.connect("Evidencia_3.db") as conn:
                ins = conn.cursor()
                salaval = (clv_sala, cupo)
                ins.execute("INSERT INTO Salas VALUES(?, ?)", salaval)
                print("Sala registrada exitosamente")
                
        except Error as e:
            print (e)
   
        except:
            print(f"se produjo el siguiente error: {sys.exc_info()[0]}")
   
        
       
       
    elif res_int == 4:
        print("Bienvenido al registro de clientes")
        clien = int(input("Ingresa el id del cliente: "))
        nooom = input("Ingresa el nombre del cliente: ")
       
        try:
            
            with sqlite.connect("Evidencia_3.db") as conn:
                salins = conn.cursor()
                inseert = (clien, nooom)
                salins.execute("INSERT INTO Clientes VALUES (?, ?)", inseert)
                print("Cliente agregado correctamente")
               
        except Error as e:
             print (e)
   
        except:
             print(f"se produjo el siguiente error: {sys.exc_info()[0]}")
    elif res_int == 5:
        print("Gracias por su preferencia, los esperamos de nuevo")
        exit()