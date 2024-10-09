from robocorp.tasks import task
from RPA.HTTP import HTTP
from RPA.JSON import JSON
from RPA.Tables import Tables

http = HTTP()
json = JSON()
table = Tables()

JSON_TRAFIC_PATH = "output/traffic.json"
CSV_TRAFIC_PATH = "output/traffic.csv"
DATOS_TRAFICO_URL = "https://github.com/robocorp/inhuman-insurance-inc/raw/main/RS_198.json"

@task
def producirDatosDeTrafico():
    print("Producir datos de tráfico")
    http.download(
        url= DATOS_TRAFICO_URL,
        target_file=JSON_TRAFIC_PATH,
        overwrite=True,
    )
    datosDeTrafico = filtrarDatosDeTrafico(cargarDatosComoTabla())
    table.write_table_to_csv(datosDeTrafico, CSV_TRAFIC_PATH)
    
@task
def consumirDatosTrafico():
    print("Consumir datos de tráfico")
    
def cargarDatosComoTabla():
    datosJSON = json.load_json_from_file(JSON_TRAFIC_PATH)
    return table.create_table(datosJSON["value"])

def filtrarDatosDeTrafico(datos):
    table.filter_table_by_column(datos, "NumericValue", ">", 5.0)
    table.filter_table_by_column(datos, "Dim1", "==", "BTSX")
    table.sort_table_by_column(datos, "TimeDim", False)
    return datos