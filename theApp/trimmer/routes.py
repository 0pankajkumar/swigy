from flask import (render_template, redirect, request, Blueprint)

from theApp.trimmer.utils import insertUrl, findUrl

trimmer = Blueprint('trimmer', __name__, template_folder='templates')


@trimmer.route("/trimit", methods=['GET'])
def trimmerFunction():
    longUrl = request.args.get('url')
    if longUrl:
        ans = insertUrl(longUrl)
        if ans:
            return "www.swi.gy/" + ans
        else:
            return redirect('http://www.google.com', code=302)    
    else:
        return redirect('http://www.google.com', code=302)


@trimmer.route("/<shortCode>", methods=['GET'])
def expanderFunction(shortCode):
    print(f"Received {shortCode} for redirecting")
    ans = findUrl(shortCode)
    if ans:
        return redirect(f'https://duckduckgo.com/?q={ans}', code=302)
    else:
        return "Does not exist"
    # return f"shortCode is {shortCode}"

@trimmer.route("/", methods=['GET'])
def home():
    return render_template('cover.html')

