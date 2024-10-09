from robocorp.tasks import task
from robocorp import browser

@task
def robotExportToPDF():
    """Insertar los datos de ventas por semana y exportar como PDF."""
    browser.configure(
        slowmo=1000,
    )
    abrirIntranet()

def abrirIntranet():
    """Navegar a la intranet de la empresa."""
    browser.goto("https://robotsparebinindustries.com/")