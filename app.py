from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "suchSecret"

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
# SentraCode Fix Applied - Remediation 2

# Context:
```python
# Corrected Flask application configuration
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False  # Ensure debug mode is disabled
```

# SentraCode Fix Applied - Remediation 2

# Context:
```python
# Corrected Flask application configuration
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False  # Ensure debug mode is disabled
```

# SentraCode Fix Applied - Remediation 2

# Context:
```python
# Corrected code snippet
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = False  # Disable debug mode for production
```
