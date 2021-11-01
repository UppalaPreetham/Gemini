# Gemini

pip install -r config/requirements.txt

command ---- python apiAlerts.py -h
provides the list of optional arguments
Sample output::
(venv) preethamuppala@preethams-mbp cryptoalerter % python apiAlerts.py -h
2021-10-31 18:16:52,313 - AlertingTool - INFO - Parsing the arguments
usage: apiAlerts.py [-h] [-c CURRENCY] [-d DEVIATION] [-t TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -c CURRENCY, --CURRENCY CURRENCY
                        The currency tradiALLmy default value
  -d DEVIATION, --DEVIATION DEVIATION
                        percentage threshold for deviation ch
  -t TYPE, --type TYPE  The type of check to run, or ALL

Runs checks on API
*************************************************************************************

command ---- python apiAlerts.py -t pricedev -c btcusd
price deviation for selected ticker
sample output ::
(venv) preethamuppala@preethams-mbp cryptoalerter % python apiAlerts.py -t pricedev -c btcusd
2021-10-31 18:18:28,917 - AlertingTool - INFO - Parsing the arguments
2021-10-31 18:18:28,918 - AlertingTool - INFO - Running check: pricedev
2021-10-31 18:18:28,919 - AlertingTool - INFO - Using deviation Threshold: 5
2021-10-31 18:18:28,921 - AlertingTool - INFO - Running checks on currency pair: btcusd
2021-10-31 18:18:28,922 - AlertingTool - INFO - Running priceDev check on: btcusd
2021-10-31 18:18:28,923 - AlertingTool - INFO - Getting Price API Data for: btcusd
2021-10-31 18:18:28,963 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.gemini.com:443
2021-10-31 18:18:29,289 - urllib3.connectionpool - DEBUG - https://api.gemini.com:443 "GET /v1/pubticker/btcusd HTTP/1.1" 200 144
2021-10-31 18:18:29,293 - AlertingTool - INFO - Last Price: 61710.53
2021-10-31 18:18:29,298 - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): api.gemini.com:443
2021-10-31 18:18:29,659 - urllib3.connectionpool - DEBUG - https://api.gemini.com:443 "GET /v2/ticker/btcusd HTTP/1.1" 200 385
2021-10-31 18:18:29,663 - AlertingTool - INFO - Standard Deviation: 495.82940051661626
2021-10-31 18:18:29,666 - AlertingTool - INFO - Average: 61060.88500000002
2021-10-31 18:18:29,668 - AlertingTool - INFO - Price diff: 153.815599483366
2021-10-31 18:18:29,669 - AlertingTool - ERROR - ** Price deviation
*************************************************************************************
command ---- python apiAlerts.py -t pricedev
gives price dev for all the tickers

command ---- python apiAlerts.py
run all the three checks for all the tickers
