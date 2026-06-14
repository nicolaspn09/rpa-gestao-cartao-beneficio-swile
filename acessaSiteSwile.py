import re
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import imaplib
import email
from email.header import decode_header
import re
from bs4 import BeautifulSoup
from datetime import datetime

sys.path.append(r'C:\rpa\Python')

from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


def get_swile_auth_code():
    pass # Logica de negocio removida por seguranca corporativa



def acessar_site_swile():
    pass # Logica de negocio removida por seguranca corporativa
