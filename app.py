from flask import Flask, send_file, render_template, Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, you bad bad"

# @app.route("/.well-known/pki-validation/<path:filename>",methods=['GET', 'POST'])
# def txt(filename):
    # path ='./cert/'+ filename
    # return send_file(path, as_attachment=True)

# @app.route("/gg.html")
# def google_site_verf():
    # return render_template("gg.html")
  
# @app.route("/log")
# def log():
    # with open("cert/檔名.txt", "r") as f:
        # content = f.read()
    # return Response(content, mimetype='text/plain')

# @app.route("/.well-known/pki-validation/<path:filename>",methods=['GET', 'POST'])
@app.route("/.well-known/acme-challenge/<path:filename>",methods=['GET', 'POST'])
def txt(filename):
    path ='./cert/'+ filename
    with open(path, "r") as f:
        content = f.read()
    return Response(content, mimetype='text/plain')

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
