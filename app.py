'''
Rubik cube microservice

This is the entry point for a microservice that enumerates the face rotations
needed to transform the input cube to a solved state.
'''
import os
import json
from flask import Flask, request, render_template, jsonify
from rubik.view.solve import solve
from rubik.view.rotate import rotate
app = Flask(__name__, template_folder='templates', static_folder='assets')

#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /
#  It returns a welcome string
#
@app.route('/')
def default():
    '''Return welcome information'''
    return render_template('MainPage.html')

#-----------------------------------
#  The following code is invoked with the path portion of the URL matches
#         /about
#  It returns the author identifier
#
@app.route('/about')
def about():
    '''Return author information'''
    return str(_getAuthor())

#-----------------------------------
#  The following code is invoked when the path portion of the URL matches
#         /rubik/solve
#
#  The cube is passed as a URL query:
#        /rubik/solve?cube=<value>
#
@app.route('/rubik/solve')
def solveServer():
    '''Return face rotation solution set'''
    try:
        userParms = _parseParms(request.args)
        print(userParms)
        result = solve(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)
#-----------------------------------
#  The following code is invoked when the path portion of the URL matches
#         /rubik/rotate
#
#  The cube and the face rotation(s) are passed as a URL query:
#        /rubik/rotate?cube=<value>&rotation=<value>
#
@app.route('/rubik/rotate')
def rotateServer():
    '''Return rotated cube'''
    try:
        userParms = _parseParms(request.args)
        result = rotate(userParms)
        print("Response -->", str(result))
        return str(result)
    except Exception as anyException:
        return str(anyException)


#-----------------------------------
#  The following code is invoked when the user submits a cube string in the form
#         /
#  It returns a welcome string
#
@app.route('/processInput', methods=['POST'])
def processInput():
    '''Return welcome information'''
    data = request.get_json()
    userInput = data.get('cube')
    processed_result = solve(data)
    return jsonify(result=processed_result)
#-----------------------------------
#  URL parsing support code
def _parseParms(queryString):
    '''Convert URL query string items into dictionary form'''
    userParms = {}
    for key in queryString:
        userParms[key] = str(queryString.get(key,''))
    return userParms

#-----------------------------------
#  SBOM support code
#
def _getAuthor(sbomDirectory = ''):
    '''Return author information from SBOM'''
    with open(os.path.join(sbomDirectory,"sbom.json"), encoding="utf-8") as sbomFile:
        parsedSbom = json.load(sbomFile)
    sbomComponents = parsedSbom["components"]
    author = "unknown"
    for component in sbomComponents:
        if 'rubik' in component.get('name'):
            author = component.get('author', author)
            continue
    return {'author': author}
 
#-----------------------------------
if __name__ == "__main__":
    port = os.getenv('PORT', '8080')
    app.run(debug=False, host = '0.0.0.0', port = int(port))
