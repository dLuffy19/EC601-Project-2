# EC601-Project-2
## Authentication
For my consumer key, consumer secret, access token key, access token secret and bearer token, I export them as environment variables as follows:
```
export 'CONSUMER_KEY'='<my_consumer_key>'
```
And then I use `os` package to access them:
```python
import os
consumer_key = os.environ.get("CONSUMER_KEY")
```
## request.py
This is a test program to access Twitter API and send a request.
