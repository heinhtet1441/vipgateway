VIPGATEWAY Payment QR — PythonAnywhere Setup Guide
===================================================

STEP 1: Upload files to PythonAnywhere
---------------------------------------
Go to: https://www.pythonanywhere.com/user/Harris2181997/files/

Create folder: /home/Harris2181997/vipgateway/
Create folder: /home/Harris2181997/vipgateway/templates/

Upload these files:
  app.py           → /home/Harris2181997/vipgateway/app.py
  templates/index.html → /home/Harris2181997/vipgateway/templates/index.html


STEP 2: Install requests library
----------------------------------
Go to: Consoles → Bash

Run:
  pip3 install --user requests flask


STEP 3: Create a Web App
--------------------------
Go to: Web tab → Add a new web app
  - Choose: Flask
  - Python version: Python 3.10
  - Path: /home/Harris2181997/vipgateway/app.py


STEP 4: Set source directory
------------------------------
In Web tab → Source code:
  /home/Harris2181997/vipgateway


STEP 5: Reload and open
-------------------------
Click "Reload" button in Web tab

Your app will be live at:
  https://Harris2181997.pythonanywhere.com/


STEP 6: Use the app
--------------------
1. Open https://Harris2181997.pythonanywhere.com/
2. Enter your API token: m2pay_live_35bc04de1800fc38eddf18d991171b6b0036328f9443299b606ab093d4f4449ed
3. Click "Load Channels"
4. Select KBZPay or WavePay channel
5. Fill in amount, phone, notes
6. Click "Generate QR"

