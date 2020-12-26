import flask 
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Must Watch TV Shows - API Data
tvShows = [
    {
        'id': 0,
        'title': 'All American',
        'runtime': 45,
    },

    {
        'id': 1,
        'title': 'NCIS: Los Angeles',
        'runtime': 45,
    },

    {
        'id': 2,
        'title': 'The Rookie',
        'runtime': 43,
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>API server for awesome information</h1><p>Welcome to my Flask hosted API attempt</p><p>Due to limitation of my hosting provider, it has to be a static website; and therefore just limited to get all</p><p>Try api.akisan.ml/api/v1/shows/all</p>"

# API Calls

@app.route('/api/v1/shows/all', methods=['GET'])
def api_get_all():
    return jsonify(tvShows)

@app.route('/api/v1/shows', methods=['GET'])
def api_id():
    # Use ID if provided or display an error for user 
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Find Show if ID is valid and export as Json
    for show in tvShows:
        if show['id'] == id:
            return jsonify(show)
    
    return "Error: ID is not Valid!"

# @app.route('/api/v1/shows', methods=['GET'])
# def api_runtime():
#     # Use runtime if provided or display an error for user
#     if 'runtime' in request.args:
#         time = int(request.args['runtime'])
#     else:
#         return "Error: No runtime field provided. Please specify an runtime."


#     results = []

#     # Find Shows with runtime and export as Json
#     for show in tvShows:
#         if show['runtime'] == time:
#             results.append(show)
            
#     if (len(results) != 0):
#         return jsonify(results)
#     else:
#         return "Error: No Show with runtime!"

if __name__ == '__main__':
    app.run()