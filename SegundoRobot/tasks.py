from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Tables import Tables

@task
def pedirRobots():
    """
    Pide un robot
    Guarda el HTML del recivo como un PDF
    Guarda una captira de pantalla del robor pedido
    Mete la captura dentro del PDF del recivo
    Crea un archivo ZIP con todos los PDFs
    """
    browser.configure(
        slowmo=100,
    )
    abrirWeb()
    hacerPedidos(obtenerPedidosCSV())
    
def abrirWeb():
    """Navega a la pagina de pedidos y acepta cokies."""
    browser.goto("https://robotsparebinindustries.com/#/robot-order")
    page = browser.page()
    page.click("text=OK")
    
def obtenerPedidosCSV():
    http = HTTP()
    http.download("https://robotsparebinindustries.com/orders.csv", overwrite=True)
    
    CSV = Tables()
    return CSV.read_table_from_csv("orders.csv")

def hacerPedidos(pedidos):
    for row in pedidos:
        page = browser.page()
        page.select_option("#head", str(row["Head"]))
        page.click(f"#id-body-{row['Body']}")
        page.fill(".form-control", str(row["Legs"]))
        page.fill("#address", row["Address"])
        page.click("#order")
        gestionarError()
        # Todo: Guardar PDF y captura de pantalla
        page.click("#order-another")
        page.click("text=OK")
        
def gestionarError():
    while browser.page().locator(".alert.alert-danger").count() > 0:
        page = browser.page()
        page.click("#order")
