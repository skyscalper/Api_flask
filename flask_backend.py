from flask import Flask
from flask_restful import Api, Resource, reqparse
import os


app = Flask(__name__,template_folder = 'templates')
api = Api(app)

'''
-Activate virtual environment
>source ./python3.8.1env/Scripts/activate

TO RUN LOCALLY
>python flask_backend.py

TO DEPLOY ON CLOUD FOUNDRY
>ibmcloud login
>ibmcloud target --cf
>ibmcloud cf push flaskApiService
'''

#########################################
## Definicion de las entradas del json ##
#########################################

scoringJsonParse = reqparse.RequestParser()
scoringJsonParse.add_argument("Id_Transaccion",         type=int,   help = "ID de la transaccion")
scoringJsonParse.add_argument("Consecutivo",            type=int,   help = "Numeracion del score segundo ID")
scoringJsonParse.add_argument("Fecha_Solicitud",        type=str,   help = "Fecha de la solicitud")
scoringJsonParse.add_argument("Tipo_Consulta",          type=str,   help = "El tipo de consulta puede ser 'A', 'B', 'C' o 'D'")
scoringJsonParse.add_argument("Monto_Solicitado",       type=float, help = "Monto del credito solicitado")
scoringJsonParse.add_argument("Plazo",                  type=int,   help = "Plazo en meses")
scoringJsonParse.add_argument("Mensualdiad",            type=float, help = "Mensulidad que debera pagar mes con mes")
scoringJsonParse.add_argument("Enganche",               type=float, help = "Monto del enganche")
scoringJsonParse.add_argument("Edad",                   type=int,   help = "Edad del Cliente")
scoringJsonParse.add_argument("Genero",                 type=str,   help = "Genero de la persona que solicita")
scoringJsonParse.add_argument("Sueldo",                 type=float, help = "Sueldo mensual persivido por el cliente")
scoringJsonParse.add_argument("Direccion_CP_Cliente",   type=int,   help = "Codigo postal del cliente")
scoringJsonParse.add_argument("Tiempo_Residencia_Year", type=int,   help = "Years de residencia en el domicilio actual")
scoringJsonParse.add_argument("Tiempo_Residencia_Month",type=int,   help = "Meses de residencia en el domicilio actual")
scoringJsonParse.add_argument("Trabajo_Tiempo_Year",    type=int,   help = "Years antiguedad en el trabajo actual")
scoringJsonParse.add_argument("Trabajo_Tiempo_Month",   type=int,   help = "Meses antiguedad en el trabajo actual")
scoringJsonParse.add_argument("EstadoCivil",            type=str,   help = "Estado Civil")
scoringJsonParse.add_argument("Num_Depndts_Eco",        type=int,   help = "Numero de dependientes economicos")
scoringJsonParse.add_argument("Distribuidor",           type=int,   help = "Numero de distribuidor")
scoringJsonParse.add_argument("FechaActualizacion",     type=str,   help = "Lista de fechas de modificacion del archivo en una cadena string separada por coma")
scoringJsonParse.add_argument("FechaActualizacion",     type=str,  help = "Lista de fechas de modificacion del archivo en una cadena string separada por coma")
scoringJsonParse.add_argument("NombreOtorgante",        type=str,  help = "Listado de nombres de las instituciones que han otorgado creditos en una cadena string separada por coma")
scoringJsonParse.add_argument("TipoCuenta",             type=str,  help = "Tipos de cuenta para cada institucion bancaria en una cadena string separada por coma")
scoringJsonParse.add_argument("TipoCredito",            type=str,  help = "Tipos de creedito otorgado para cada institucion bancaria en una cadena string separada por coma")
scoringJsonParse.add_argument("FrecuenciaPagos",        type=str,  help = "Frecuencia de pagos para cada credito otorgado en una cadena string separada por coma")
scoringJsonParse.add_argument("FechaAperturaCuenta",    type=str,  help = "Listado de fechas de apertura para cada tipo de cuenta abierta en una cadena string separada por coma")
scoringJsonParse.add_argument("FechaCierreCuenta",      type=str,  help = "Listado de fecha de cierre para cada tipo de cuenta abierta en una cadena string separada por coma")
scoringJsonParse.add_argument("FechaReporte",           type=str,  help = "Listado de fecha de reporte para cada tipo de cuenta abierta en una cadena string separada por coma")
scoringJsonParse.add_argument("SaldoActual",            type=str,  help = "Listado de saldos para cada tipo de cuenta abierta en una cadena string separada por coma")
scoringJsonParse.add_argument("SaldoVencido",           type=str,  help = "Listado para cada tipo de cuenta abierta en una cadena string separada por coma")
scoringJsonParse.add_argument("HistoricoPagos",         type=str,  help = "Listado para cada tipo de cuenta abierta en una cadena string separada por coma")

class ApiJson(Resource):
    def get(self,name):
        return {'name': "Hello World %s" % name} 
    def post(self):
        args = scoringJsonParse.parse_args()
        return args #{'name': "Hello World (post)"}

api.add_resource(ApiJson,"/parsejson")

######################
##  MISC FUNCTIONS  ##
######################

####################
##  MAIN PROGRAM  ##
####################
port = int(os.getenv('PORT', 8000))
    
if __name__ == '__main__':
    #running locally
    #app.run(port=port, debug=True)
    #running on server
    app.run(host='0.0.0.0', port=port, debug=False)
    

