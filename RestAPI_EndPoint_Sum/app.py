import uvicorn
import logging
from fastapi import FastAPI, Request
import pandas as pd



app = FastAPI(
    title='API for KASEM',
    summary='Compliant with KASEM Interface standard structure',
    version='demo',
    contact={"name": "Predict"}
    )

@app.post('/sum',tags=['Operation'], description='Sum of two syncrhonized scalar time series')
async def sum(request: Request):

    #Parse request body
    content = await request.json()
    data = pd.DataFrame(data = content['scalar']['data'],columns=content['scalar']['headers'])
    logging.info(f'[sum] row count: {len(data)}')    

    #Make the sum
    data['sum_ts'] = (data['e1_ts'] + data['e2_ts']) * content['param']['scale']

    #Format result
    data2 = data[['date','sum_ts']]
    result = {'scalar': {}}
    result['scalar']['headers'] = data2.columns.tolist()
    result['scalar']['data'] = data2.to_numpy().tolist()

    #Return result
    return result



logging.basicConfig(level=logging.INFO)

config = uvicorn.Config(app=app, host="0.0.0.0", port=5000, workers=4, reload=False)
server = uvicorn.Server(config)
server.run()