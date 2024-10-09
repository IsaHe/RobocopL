Siguiendo el curso introductorio https://sema4.ai/docs/automation/courses/beginners-course-python
# Introducción

Robot Framework es un marco de automatización de pruebas de código abierto. Se destaca su simplicidad y extensibilidad, lo que lo hace adecuado para una amplia gama de aplicaciones.

### Capacidades Básicas

- **Extensible**: Soporta bibliotecas externas que pueden ser escritas en Python o Java para ampliar su funcionalidad.
- **Generación de Reportes**: Produce reportes y registros detallados que facilitan el análisis de los resultados de las pruebas.

### Usos Comunes

- **Automatización de Procesos**: Puede ser utilizado para automatizar tareas repetitivas en diferentes entornos de software.
- **Pruebas de API**: Facilita la prueba de servicios web y APIs RESTful.

# Cosas a tener en cuenta (borrador)

### Navegador
* Se pueden abrir y realiar acciones en navegador importando browser
* Para acceder a una url: `browser.goto("url")`
* Puedes usar get sobre la browser para guardar la pagina como variable usando `browser.page()`
* Con la pagina como variable se puede usar `page.fill("#idElemento", "textoParaLlenar")` para llenar los campos del formulario
* Puedes enviar el formulario con `page.click("button:text('textoBoton'))` o `page.click("text=textoBoton)`
* Se puede elegir el valor de un dropdown usando `page.select_option("#idDropdown", "valor")`
* Para descargar archivos de una pagina utilizaremos `RPA.HTTP`