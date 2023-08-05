## Installation

```bash
pip install zimran-http
```

## Usage

```python
from zimran.http import AsyncHttpClient, HttpClient

# async
async with AsyncHttpClient(service='...') as client:
    response = await client.get('/endpoint')

# sync
client = HttpClient(service='...')
response = client.get('/endpoint')
```
