from robocorp.tasks import task
from robocorp import browser

@task
def robotExportToPDF():
    """Insertar los datos de ventas por semana y exportar como PDF."""
    browser.configure(
        slowmo=2000,
    )
    abrirIntranet()
    logIn()
    enviarFormularioVentas()

def abrirIntranet():
    """Navegar a la intranet de la empresa."""
    browser.goto("https://robotsparebinindustries.com/")
    
def logIn():
    """Iniciar sesión en la intranet."""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")
    
def enviarFormularioVentas():
    """Rellenar y enviar formulario de ventas."""
    page = browser.page()
    
    page.fill("#firstname", "John")
    page.fill("#lastname", "Doe")
    page.fill("#salesresult", "100")
    page.select_option("#salestarget", "10000")
    page.click("text=Submit")