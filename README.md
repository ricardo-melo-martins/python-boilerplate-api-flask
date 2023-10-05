<p align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="python" width="60" height="60"/>
</p>

# RMM | Python Esqueleto padrão com Flask

<p align="right">
[![English](:flag_en)](README.en.md)
</p>

## Requisitos

 [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
 [![Pip 2.x](https://img.shields.io/badge/pip-2.x-blue.svg)](https://www.python.org/downloads/release/python-360/)
 [![Flask 2.x](https://img.shields.io/badge/Flask-2.x-blue.svg)](https://www.python.org/downloads/release/python-360/)
 [![Bash 2.x](https://img.shields.io/badge/Bash-2.x-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Instalação

```bash
$ pip3 install -r ./requirements.txt
```

or with shell

```bash
$ ./bin/install
```

## Iniciando

```bash
$ Flask --app server run --debug
```

or with shell

```bash
$ ./bin/start
```

or with debug

```bash
$ ./bin/start_dev
```

## Cache

### Application

Arquivos de caches da aplicação são gravados no diretório

```
/tmp/caches
```
mas também há arquivos do python `__pycache__, .pyc e .pyo` gravados em meio ao projeto.


Se for preciso apagar os caches criados pela aplicação, existe um comando

```bash
$ ./bin/clear_cache
```


## Logs

### Application

Arquivos de logs são gravados no diretório
```
/tmp/logs
```

Para apagar arquivos de logs

```bash
$ ./bin/clear_logs
```


## Licença

[![License](https://img.shields.io/badge/license-MIT-green?style=plastic)](LICENSE.md)



Criado e mantido com diversão e :heart: por [![Github](https://img.shields.io/badge/-ricardo%20melo%20martins-000?style=plastic&logo=github)](https://github.com/ricardo-melo-martins)


