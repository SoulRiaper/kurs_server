import serial.tools.list_ports as list_ports
import serial
import time


# define ports list
ports = list_ports.comports()


# # dataRepozitory = data.DataRepozitory()

# # select ctive port
# s = serial.Serial(ports[1].device)# TODO: add a port select 

# string = ""

# # while for featch stm data
# while 1 :
#     if s.in_waiting > 0:
        
#         string = s.read()
        
#         # decode simbols
#         try:
#             # stmData = string.decode('Ascii')
#             print(string)
#             # query = f"INSERT INTO public.voltage (voltage) VALUES ( {stmData[:1]} );"
#             # dataRepozitory.insert_data(query)
#         except Exception as ex:
#             print(ex)
#             pass