    
# from flask import Flask, request, json
# from flask_restful import Resource, Api
from flask import Flask, request
from flask_restful import reqparse,Resource, Api
from flask_cors import CORS
import requests
import json
import datetime

""" app = Flask(__name__)
api = Api(app) """

Token = "Bearer ggsCl9jNmxar2MjFx8+Q2quR2+3/atsB4qcufx8ASWkR/PvEROiERKAsR2XEJ5gYyjPcXx9E5hLthS8y3+bMz7WV54B9MtuxGr0Jr/n2GoKqtXJKGIwtA0pBbEcrLOoNYNc8itXmudGL1xjeAOk9LK9/ojLHMRuQEEjHc7yMr1NDmSLMuoHC9e6Ui6GxGSzSiFz1fFT5nKD3morAFN3OwTsmhI/A2l9t0N6RxsUyc7F9NQxxXSLnV5HkjKX0l+/sioh8HIRcYdi1Hz4u+2VyDZK4lhRKqXa/ofXLuqM0EocdOLGCeZt5zPfl4nrj0fMMolq2y9o6ndnBA62H/j9Z5nXGw7ZyzNinJ2rtgvagMepsYPu2oVad4PmFLOTdNBsT/QRjK7rVJGhqECS/WG3ZR2w73SZyqRdKCP1hrwf5bFXZlYUXFJmnsFPHWUC3LDEKd83eawK95kcpSDRmn4MX3faEr9xpyMT7TNsCV0N3VdTGnbZifPndR46lg+VjVkw2zG5RyntApRuT5Tlp1A8/zXmjp39LITloRYm4XaXqrRjQvyvl9jqwsWM1yZ0cql2S79jiGprXVyz2JCX+qMdT2CiWHo7rMaBWXGsjIf6FWociSD/8Z0m9D+7hB52+NvDX8FbFVhqAxhPznPLMWTglfy3MGlLo4mbRYCGMa3AYNirznfjH3Q0YDnnekc+Pxp/8hVu2yG0JlH7T4ecn++Js9AegXEFdvuhdbFPFIoSFyUN4/a5kENcvdDlbR5VX6/E0CRB3YfIlMoQcBPnDgAhN/RF2vYQ0NOYr1OUteSCI5PKJAtWXSdYRytoiAY8loQwFPJ2ACHUuFSXctmFBz9yWfzwFfDzR9Q+b10g6Tm3lQqWyIy3GC0Nl9GZNKuv1+39IeWu6TeOj8s/FsXlCQGbRFbJw+h1rbjAgibhdvZI="
Type = "application/json"
x = datetime.datetime.now()

#print ("Fecha y hora = %s" % x)
# @app.errorhandler(402)
# def page_not_found(error):
#     return 'This page does not exist', 404


app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls
 
# @app.route('/employea', methods=['GET'])
# def get_home():
#     url = 'http://dev.clever-api-benefit.local/subConcepto/getConcepByCategory/68'
#     headers = {
#         'Content-Type':Type,
#         'Authorization':Token}
#     return json.loads(requests.get(url, headers=headers).text)

@app.route('/employea/<pos_str>', methods=['GET'])
def get_notif(pos_str):
    url = 'http://frm-api-qa.clever.palace-resorts.local/notificaciones/elementbytag/'+pos_str
    print(pos_str)
    print(url)
    headers = {
        'Content-Type':Type,
        'Authorization':Token}
    print(requests.get(url, headers=headers).text)
    return json.loads(requests.get(url, headers=headers).text)

# @app.route('/employeb/<post_string>', methods=['POST'])
# def get_notif_group(post_string):
#     url = 'http://dev.clever-api-frm.local/notificaciones/notificacion/' + post_string
#     headers = {
#         'Content-Type':Type,
#         'Authorization':Token}
#     return json.loads(requests.get(url, headers=headers).text)



@app.route('/codigo/api/palaceaRuX/lwQmyIjdVFW0/UEHUWNgpbmc/<post_str>', methods=['POST'])
def post_notificaciones(post_str):
    url = 'http://frm-api-qa.clever.palace-resorts.local/notificaciones/notificacion/'+post_str
    values = request.get_json()
    headers = { 'Content-Type': Type, 'Authorization': Token }
    #return(json.dumps(values))
    return (requests.post(url, data=json.dumps(values), headers=headers).text)



if __name__ == '__main__':
    app.run(debug = True)

# """ if __name__ == '__main__':
#     app.run(debug=True) """