from flask import (render_template, redirect, request, Blueprint)

from theApp.trimmer.utils import insertUrl, findUrl

trimmer = Blueprint('trimmer', __name__, template_folder='templates', static_folder="static")

domain = "phew.link/"

@trimmer.route("/trimit", methods=['POST'])
def trimmerFunction():
    longUrl = request.form.get('url')
    if longUrl:
        ans = insertUrl(longUrl)
        if ans:
            print("We are returning success.html now")
            return render_template('success.html', shortUrl = domain+ans, longUrl = longUrl) # "www.swi.gy/" + ans
        else:
            return render_template('failure.html', longUrl = longUrl)    
    else:
        return render_template('failure.html') 


@trimmer.route("/<shortCode>", methods=['GET'])
def expanderFunction(shortCode):
    print(f"Received {shortCode} for redirecting")
    ans = findUrl(shortCode)
    if ans:
        return redirect(ans, code=302)
    else:
        return render_template('notFound.html')
    # return f"shortCode is {shortCode}"

@trimmer.route("/", methods=['GET'])
def home():
    return render_template('start_form.html')

