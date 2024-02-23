<div align="right">

### ⚡ RMM ⚡

</div>

# python-flask-skeleton

<div align="right">

[<img src="https://raw.githubusercontent.com/lipis/flag-icons/main/flags/1x1/us.svg" alt="python" width="10" height="10"/> English Readme](docs/README.en.md)

</div>

<table>
  <tr>
    <td>
      <p align="center">
        <a href="https://www.python.org/" target="blank"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="60" alt="Python"></a>
      </p>
    </td>
    <td>
      <p align="center">Python é uma linguagem de programação que permite trabalhar rapidamente e integrar sistemas de forma mais eficaz.</p>
    </td>
  </tr>
</table>

## Descrição

Este é um esqueleto de código que usa Python e Flask.

Auxilia na criação acelerada de aplicações, poc's e estudos da tecnologia.

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


