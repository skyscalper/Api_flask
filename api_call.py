import requests
import json

json_parse = {"Id_Transaccion":120102020,"Consecutivo":4031119164,"Fecha_Solicitud":"28/10/2019",
"Tipo_Consulta":"C",
"Monto_Solicitado":96000,
"Plazo":36,
"Mensualdiad":0,
"Enganche":0,
"Edad":30,
"Marca":"VOLKSWAGEN",
"Genero":"Genero",
"Sueldo":23000,
"Direccion_CP_Cliente":36557,
"Tiempo_Residencia_Year":2,
"Tiempo_Residencia_Month":24,
"Trabajo_Tiempo_Year":5,
"Trabajo_Tiempo_Month":60,
"EstadoCivil":"Union libre",
"Num_Depndts_Eco":1,
"Distribuidor":4031, 
"FechaActualizacion": "01/01/2020,01/02/2020,01/03/2020,01/04/2020,05/05/2020,06/06/2020",
"NombreOtorgante": "BANCOS,FONDOS Y FIDEICOMISOS,FONDOS Y FIDEICOMISOS,BANCOS,TELEFONIA CELULAR,COMUNICACIONES,COMUNICACIONES,GUBERNAMENTALES,COMUNICACIONES",
"TipoCuenta": "R,F,F,F,R,L,L,F,L",
"TipoCredito": "TC,PP,PP,MC,LC,LC,LC,PP,LC",
"FrecuenciaPagos": "M,M,M,M,M,M,M,M,M",
"FechaAperturaCuenta": "1562371200, 1381363200, 1424131200, 1459468800, 1499299200, 1511049600, 1511049600, 1556064000, 1360108800",
"FechaCierreCuenta": "NA, 1412208000, 1457049600, 1535673600,NA,NA,NA,NA,1425081600",
"FechaReporte": "1572480000, 1414713600, 1459382400, 1535673600, 1572480000, 1572566400, 1572480000, 1572480000, 1425081600",
"SaldoActual": "0,0,0,0,876,0,3555,11229,0",
"SaldoVencido": "0,0,0,0,876,0,1512,0,0",
"HistoricoPagos": "V V V V,V V V V V V V V V---- V V,V V-- V V V V V V V V V V V,V---- V V V V V V V-- V,13----131313131313131313131313----------------03,V V-- V V V V V V V V V V V V V V V V V V V V V V,1313131313131313050403020101 V0201 V V V V V V V,V V V V V V V,V V V V V V01 V0101 V"
}


#URL_Base = "http://127.0.0.1:5000/"
URL_Base = "https://flaskapiservice-chatty-hartebeest.mybluemix.net"


response = requests.post(URL_Base+"/parsejson",json_parse)

parsed = response.json()

print(json.dumps(parsed, indent=4, sort_keys=True))


#Curl cmmand to parse json

#curl --header "Content-Type: application/json" --request POST --data '{"Id_Transaccion":120102020,"Consecutivo":4031119164,"Fecha_Solicitud":"28/10/2019","Tipo_Consulta":"C","Monto_Solicitado":96000,"Plazo":36,"Mensualdiad":0,"Enganche":0,"Edad":30,"Marca":"VOLKSWAGEN","Genero":"Genero","Sueldo":23000,"Direccion_CP_Cliente":36557,"Tiempo_Residencia_Year":2,"Tiempo_Residencia_Month":24,"Trabajo_Tiempo_Year":5,"Trabajo_Tiempo_Month":60,"EstadoCivil":"Union libre","Num_Depndts_Eco":1,"Distribuidor":4031}' http://127.0.0.1:5000/parsejson

#IBM Cloud
#curl --header "Content-Type: application/json" --request POST --data '{"Id_Transaccion":120102020,"Consecutivo":4031119164,"Fecha_Solicitud":"28/10/2019","Tipo_Consulta":"C","Monto_Solicitado":96000,"Plazo":36,"Mensualdiad":0,"Enganche":0,"Edad":30,"Marca":"VOLKSWAGEN","Genero":"Genero","Sueldo":23000,"Direccion_CP_Cliente":36557,"Tiempo_Residencia_Year":2,"Tiempo_Residencia_Month":24,"Trabajo_Tiempo_Year":5,"Trabajo_Tiempo_Month":60,"EstadoCivil":"Union libre","Num_Depndts_Eco":1,"Distribuidor":4031, "FechaActualizacion": "01/01/2020,01/02/2020,01/03/2020,01/04/2020,05/05/2020,06/06/2020", "NombreOtorgante": "BANCOS,FONDOS Y FIDEICOMISOS,FONDOS Y FIDEICOMISOS,BANCOS,TELEFONIA CELULAR,COMUNICACIONES,COMUNICACIONES,GUBERNAMENTALES,COMUNICACIONES", "TipoCuenta": "R,F,F,F,R,L,L,F,L","TipoCredito": "TC,PP,PP,MC,LC,LC,LC,PP,LC", "FrecuenciaPagos": "M,M,M,M,M,M,M,M,M", "FechaAperturaCuenta": "1562371200, 1381363200, 1424131200, 1459468800, 1499299200, 1511049600, 1511049600, 1556064000, 1360108800", "FechaCierreCuenta": "NA, 1412208000, 1457049600, 1535673600,NA,NA,NA,NA,1425081600", "FechaReporte": "1572480000, 1414713600, 1459382400, 1535673600, 1572480000, 1572566400, 1572480000, 1572480000, 1425081600", "SaldoActual": "0,0,0,0,876,0,3555,11229,0", "SaldoVencido": "0,0,0,0,876,0,1512,0,0", "HistoricoPagos": "V V V V,V V V V V V V V V---- V V,V V-- V V V V V V V V V V V,V---- V V V V V V V-- V,13----131313131313131313131313----------------03,V V-- V V V V V V V V V V V V V V V V V V V V V V,1313131313131313050403020101 V0201 V V V V V V V,V V V V V V V,V V V V V V01 V0101 V"}' https://flaskapiservice-chatty-hartebeest.mybluemix.net/parsejson
