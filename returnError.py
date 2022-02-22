# Return Error
# A Library for an Azure Functions App to return an HTTP response containing an error message and HTTP status 500

import json
import azure.functions as func

def returnError (msg=''):
    return func.HttpResponse(json.dumps(dict({"Response" : msg})), status_code=500)


