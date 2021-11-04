#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
    installation-prerequis.py
    Script to install a GLPI server with a maria DB database and apache2 server
    Author :    Didier Lemaitre
    Version :   0.1
    Date :      2021-11-01
    Tested with Python 3.7 running on a Ubuntu 20.04 

"""

#Import of required modules

import logging
import subprocess
import os

"""
    Paquets to be installed : 
        apache2
        php
        mariadb-server
        curl 
        python3
        module python validators
        module python mariadb
        pip

    Configuration de base :
        mysql_secure_installation

"""

#constants Définitions

LOG_FILE = "./installation.log"

# Log File Configuration 

try:
    logging.basicConfig(filename=LOG_FILE, format="%(asctime)s : %(levelname)s:%(message)s", 
        level=logging.DEBUG)
    logging.info("Début de l'installation des pré-requis")
except Exception as e:
    print("Erreur lors de la création du fichier de journalisation")
    raise e

# system update and paquet Installation

try:
    logging.info("system update and paquet Installation...")
    os.system("apt update ; apt upgrade")
    os.system("apt install apache2 php mariadb-server curl python3 python3-pip libmariadbclient-dev pip")
    os.system("pip install --upgrade setuptools")
    os.system("pip install validators")
    os.system("pip install mariadb")
    os.system("mysql_secure_installation")
    logging.info("system update and paquet installations succeeded !")
    exit(0)
except Exception as e:
    print("paquets installation failed !")
    logging.error("paquets installation failed !")
    logging.error(e)
    raise e
