## pawapi

API wrapper for [PythonAnywhere](https://pythonanywhere.com/)

## Install

```bash
pip install pypawapi
```

## Usage

[API documentation](https://help.pythonanywhere.com/pages/API)

```python
import pawapi

TOKEN = "YOUR_TOKEN"
USER = "YOUR_USERNAME"

api = pawapi.Pawapi(USER, TOKEN)
print(api.cpu.info())
```

## LICENSE
[MIT](./LICENSE)
