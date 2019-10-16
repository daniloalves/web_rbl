## Version
* Current: 0.1.0

## Supported Integration
* Graylog 3.x - Data adapters for Lookup Tables (HTTP JSONPath)

## Run Container

* `docker build -t web_rbl:0.1.0 .`
* `docker run --rm -t -p 8000:8000 -e DNSBL_TOKEN=<Access_Key> web_rbl:0.1.0`

## How to generate Access Key
This project use Http:BL https://www.projecthoneypot.org/httpbl_api.php. To consulte this database you need generate a Access Key. Follow this steps:
* Create a account (https://www.projecthoneypot.org/account_login.php)
* Go to Home page.
* Click in API key.
* Follow instructions.

## Available Features
* Consulting recomendation about IP:
    * `http://localhost:8000/ask?ip=103.247.68.227`

## Issues
* Configure exception when don't have DNS return.
* Use LDAP to generate a own PRT (like DNSBL), using a "global" blacklist and a own blacklist.
* Return own LDAP record in API too.
* Write Graylog integration document (How to) (E.q.: https://github.com/Graylog2/graylog-plugin-pipeline-processor/issues/27).