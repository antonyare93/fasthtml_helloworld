from fasthtml.common import *

app = FastHTML()

@app.get('/')
def home():
    return H1('Hello world!')


serve()
