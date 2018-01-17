from bottle import route, run

@route("/")
def index():
    return "<a href = '/tegund' >Tegund</a><br>" "<a href = '/árgerð' >Árgerð</a><br>" "<a href = '/bílnúmer' >Bílnúmer</a><br>"

@route("/tegund")
def bottle():
    return "foieærhwvejqd"

@route("/árgerð")
def bottle():
    return "<h2>Hello bottle</h2>"

@route("/bílnúmer")
def bottle():
    return "<h2>Hello bottle</h2>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

