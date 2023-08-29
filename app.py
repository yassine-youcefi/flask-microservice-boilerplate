import os
import json
from api import app
from config import settings

if __name__ == '__main__':

    app.run(debug=settings.DEBUG, host='0.0.0.0',
                    port=5000, threaded=True)
    