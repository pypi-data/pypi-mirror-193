# pyxJetAPI, but not async

## Authors
- [@xJetLabs](https://github.com/xJetLabs) (forked from)
- [@nik-1x](https://github.com/nik-1x)
- [@Sovenok-Hacker](https://github.com/Sovenok-Hacker)
 
## Usage/Examples  
```python
from xjetsync import pyxJet
api = pyxJet(
    api_key="API_KEY",
    private_key="PRIVATE_KEY", 
    mainnet=False
)
```

```python
# Account methods
api.me() # get API Application information.
api.balance() # get balance
api.submit_deposit() # check for deposit
api.withdraw(ton_address, currency, amount) # check for deposit
```

```python
# Cheques methods
api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque
api.cheque_status(cheque_id) # get cheque status
api.cheque_list() # get cheques on account
api.cheque_cancel(cheque_id) # delete cheque
```

```python
# Invoice methods
api.invoice_create(currency, amount, description, max_payments) # create invoice
api.invoice_status(invoice_status) # get invoice status
api.invoice_list() # get invoices on account
```

## License
[GNUv3](https://github.com/Sovenok-Hacker/syncxJetConnect/blob/master/LICENSE)  
