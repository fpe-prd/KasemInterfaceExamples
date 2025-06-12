from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/method/', methods=['POST'])    #Endpoint definition
def method():

    #Parse request body
    content = request.json
    data = pd.DataFrame(data = content['scalar']['data'],columns=content['scalar']['headers'])

    #Make the sum
    data['sum_ts'] = (data['e1_ts'] + data['e2_ts']) * content['param']['scale']

    #Format result
    data2 = data[['date','sum_ts']]
    result = {'scalar': {}}
    result['scalar']['headers'] = data2.columns.tolist()
    result['scalar']['data'] = data2.to_numpy().tolist()

    #Return result
    return jsonify(result)

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)