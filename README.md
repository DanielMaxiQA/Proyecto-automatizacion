
# Automatizacion Chronos
<p align="center">
        <a href="https://www.python.org/">
            <img src="https://img.shields.io/badge/Language-Python%203.12-green.svg" alt="Python">
        </a>
        <a href="https://playwright.dev/">
            <img src="https://img.shields.io/badge/Framework-Playwright-red.svg" alt="Playwright">
        </a>
        <a href="https://pipenv.pypa.io/en/latest/">
            <img src="https://img.shields.io/badge/Virtual%20Environment-PipEnv-yellow.svg" alt="PipEnv">
        </a>
         <a href="https://allurereport.org/docs/">
            <img src="https://img.shields.io/badge/Report-Allure-blue.svg" alt="Allure">
        </a>
</p>

Proyecto desarrollado en Python con Playwright Async para la automatizacion de flujos en la aplicación Chronos


## Instalación y Configuración

1. Descargar el proyecto de GitHub
```bash
  git clone https://github.com/DanielMaxiQA/maxi-chronos-automation.git
```
2. Ingresar a la raiz del proyecto
```bash
  cd maxi-chronos-automation
```
3. Configurar entornor virtual e instalar dependencias
```bash
  pipenv install
```
```bash
  pipenv shell
```
Este comando instala los Browser que necesita playwright
```bash
 pipenv run playwright install
```

## Ejecución de las pruebas
Para ejecutar las pruebas se puede hacer de diferentes maneras, dependiendo de como se necesita que se ejecuten.

- Opción 1: Si se necesita ejecutar todas las pruebas en paralelo al mismo tiempo y que no se genere reportes, dependiendo de la capacidad de la maquina se usa el siguiente comando:
```bash
 pytest -n auto
```
- Opción 2: Si se necesita ejecutar todas las pruebas en paralelo al mismo tiempo y que se genere reportes, dependiendo de la capacidad de la maquina se usa el siguiente comando:
```bash
pytest -n auto --alluredir=reports/allure-results
```
- Opción 3: Si se necesita ejecutar algun caso de prueba en especifico, se debe usar el siguiente comando:
```bash
pytest tests/{Nombre del archivo de pruebas}/ --alluredir=reports/allure-results
```

## Abrir los reportes
Despues de que se ejecuten las pruebas con alguno de los comandos que generan reportes, se ejecuta el siguiente comando para que se cargue el reporte en formato HTML.
```bash
allure serve reports/allure-results 
```

## Opción Record and Play
Si queremos grabar un flujo o un caso de pruebas o simplemente queremos usar los localizadores que playwright mapea automaticamente al grabar un caso de prueba, usamos el siguiente comando:
```bash
playwright codegen demo.playwright.dev/todomvc
```


## Authors
Proyecto implementado por:

**Héctor Vergara** /
**Ignacio García** /
**Daniel Ureña**
