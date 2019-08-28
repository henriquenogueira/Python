import functions
import time
from webdriver import Robo

functions.main()

# abre o dropdown
functions.openMenu()
time.sleep(5)

# Começa capturar e abrir unidade por unidade
functions.reiniciaUnidades()
time.sleep(10)

functions.iniciaBuscas()