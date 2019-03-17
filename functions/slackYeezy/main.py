# Copyright 2019 Evan Gray
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import requests
from flask import request
from flask import jsonify

def handleRequest(request):
    resp = {'status': 'OK'}
    json = request.json

    logging.warn('Got request: %s' % request.json)

    if json is not None:
        if json.get('type') in ['url_verification']:
            resp = {'challenge': json.get('challenge')}
    else:
        quote = requests.get('https://api.kanye.rest').json()
   
        resp = {'response_type': 'in_channel', 
                'text': 'I miss the old kanye.',
                'username': 'KanyeBot',
                'attachments': [{'text': quote.get('quote')}]}

    return jsonify(resp)

if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)

    @app.route('/kanye', methods=['POST', 'GET', 'OPTIONS'])
    def req():
        _request = request
        return handleRequest(_request)
    app.run(host='0.0.0.0')
