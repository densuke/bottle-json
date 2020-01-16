from bottle import route, request, response, template, run

@route("/")
def index():
    return template("form.html")

@route("/send", method="POST")
def send():
    if request.headers['Content-Type'] == "application/json":
        return request.json['data']
    else:
        data = request.forms.get("data")
        return data


run(host="0.0.0.0", port=8080)