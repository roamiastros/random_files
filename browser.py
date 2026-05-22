from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# 1. Set up options to disable proxy
options = Options()
options.add_argument("--no-proxy-server") 
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

edge_driver_path = r'driver\msedgedriver.exe'

service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://www.google.com")
