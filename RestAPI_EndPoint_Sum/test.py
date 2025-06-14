import requests as rq

url = 'http://localhost:2000/method'

body = { 'param': {
            'scale': 25
            },
            'scalar': { 
                'headers': ['date', 'el_ts', 'e2_ts'],
                'data': [
                    [ 1420066800.0, 1.2507524347169103, 842.59695878373316],
                    [ 1420066801.0, 17.684785517717145, 503.28803528253366],
                    [ 1420066802.0, 48.464766632981956, 921.17810851017862],
                    [ 1420066803.0, 11.014022077905956, 935.60744493063885]
                ]
            }
        }

result = rq.post(url, json = body)

print(result.json())

'''
{ 'scalar': {'
    headers': ['date', 'sum_ts']},
    'data': [
        [1420066800.0, 21096.19278046125],
        [1420066801.0, 13024.320520006271],
        [1420066802.0, 24241.071878579016],
        [1420066803.0, 23665.536675213618]
    ]
}
'''