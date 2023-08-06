## Demo

## Install

```bash
pip install amberdata
```
## for reference

```python
from amberdata import Amberdata

ad_client = Amberdata(x_api_key="ENTER YOUR API KEY HERE")

blockchain_address_logs = ad_client.blockchain_address_logs(
    address="0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", topic="0x58e5d5a525e3b40bc15abaa38b5882678db1ee68befd2f60bafe3a7fd06db9e3"
)

print(blockchain_address_logs)
```
