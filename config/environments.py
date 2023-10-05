#!/usr/bin/env python

# Configuração do servidor
HOST_ADDRESS = "0.0.0.0"
HOST_PORT = 5000

# Rotas
API_NAMESPACE = '/api'

# Configuração de Logs
LOG_MODULE = 'RMM'

# FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
FORMATTER = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
LOG_PATH = 'tmp/logs/'
LOG_FILE = LOG_PATH +'debug.log'

DATETIME_FORMAT = '%m/%d %H:%M:%S'