from flask import Flask, redirect, request,render_template
app = Flask(__name__)
sites = {}
@app.route("/upload", methods=["POST", "GET"])
def details():

    print(request.method)
    if request.method == "POST":
        urlname = request.form.get("urlname")
        url = request.form.get("url")
      
        sites[urlname] = url
        return sites
    else:
        return render_template("index.html")
@app.route("/<link>")
def links(link):
    if(link!="upload"):
        return redirect(sites[link])

if __name__ == '__main__':
    app.run(debug=True)