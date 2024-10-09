from robocorp.tasks import task
from robocorp import browser

from RPA.HTTP import HTTP
from RPA.Excel.Files import Files

@task
def robotExportToPDF():
    """Insertar los datos de ventas por semana y exportar como PDF."""
    browser.configure(
        slowmo=100,
    )
    abrirIntranet()
    logIn()
    descargarExcel()
    rellenarConDatosExel()
    recolectarResultados()

def abrirIntranet():
    """Navegar a la intranet de la empresa."""
    browser.goto("https://robotsparebinindustries.com/")
    
def logIn():
    """Iniciar sesión en la intranet."""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")
    
def enviarFormularioVentas(nombre: str, apellido: str, resultado: str, objetivo: str):
    """Rellenar y enviar formulario de ventas."""
    page = browser.page()
    
    page.fill("#firstname", nombre)
    page.fill("#lastname", apellido)
    page.fill("#salesresult", str(resultado))
    page.select_option("#salestarget", str(objetivo))
    page.click("text=Submit")
    
def descargarExcel():
    """Descargar un archivo excel dada una URL."""
    http = HTTP()
    http.download("https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)
    
def rellenarConDatosExel():
    """Rellenar formulario con datos de un archivo Excel."""
    excel = Files()
    excel.open_workbook("SalesData.xlsx")
    data = excel.read_worksheet_as_table(header=True)
    
    for row in data:
        enviarFormularioVentas(row["First Name"], row["Last Name"], row["Sales"], row["Sales Target"])
        
    excel.close_workbook()
    
def recolectarResultados():
    """Hacer una captura de pantalla de la pagina."""
    page = browser.page()
    page.screenshot(path="output/resultadosVentas.png")