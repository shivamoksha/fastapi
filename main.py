from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS (Allow all origins, methods, and headers)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

# Sample database (Replace with actual database queries)
marks_database = {[{"name":"0z","marks":9},{"name":"vBUQMzw","marks":31},{"name":"Ht77nX","marks":31},{"name":"sM","marks":92},{"name":"MQDZHebrF","marks":87},{"name":"RP7","marks":60},{"name":"jewMXD","marks":80},{"name":"0WvERs","marks":10},{"name":"rD4","marks":60},{"name":"3tKxdEcIZ","marks":89},{"name":"iLeQl4Wzv","marks":50},{"name":"gn24T2Fv","marks":81},{"name":"7u","marks":32},{"name":"x","marks":25},{"name":"Sc","marks":40},{"name":"Z7kLlPAo","marks":84},{"name":"9s","marks":16},{"name":"J","marks":13},{"name":"PO","marks":33},{"name":"XsKE","marks":11},{"name":"tL09KhD","marks":87},{"name":"Y5ilo857jn","marks":65},{"name":"t","marks":55},{"name":"uonH","marks":70},{"name":"k","marks":48},{"name":"uFCxYQF","marks":39},{"name":"h","marks":70},{"name":"iY","marks":31},{"name":"KvNGWEgHv","marks":73},{"name":"2izR6","marks":41},{"name":"4","marks":79},{"name":"4AAa3awr","marks":75},{"name":"YdwPDYWq","marks":59},{"name":"LxXJ","marks":64},{"name":"LkXINOb","marks":51},{"name":"yQO6","marks":13},{"name":"EK9B","marks":19},{"name":"YUPSziVMfi","marks":51},{"name":"P","marks":9},{"name":"K","marks":17},{"name":"CILF7iSP","marks":51},{"name":"y2MWjy","marks":61},{"name":"vPccsuob","marks":44},{"name":"S","marks":63},{"name":"hzwrPMI1","marks":19},{"name":"uRlsy2Qg2","marks":18},{"name":"KBTn","marks":14},{"name":"U2tRzpQh","marks":50},{"name":"2sG2t","marks":63},{"name":"14ccI0db","marks":44},{"name":"420QbHLW","marks":12},{"name":"JqqX","marks":1},{"name":"aslGpj","marks":71},{"name":"9NPwiP","marks":32},{"name":"nmO","marks":76},{"name":"xtslbtP2","marks":57},{"name":"fB3qV9qN","marks":64},{"name":"2ZQt7","marks":29},{"name":"IKRyqGDosn","marks":18},{"name":"nXAlHo1a","marks":20},{"name":"1","marks":9},{"name":"d","marks":16},{"name":"H8PJ1ya5","marks":20},{"name":"67IM0Wrew","marks":77},{"name":"p2RSp6sqKt","marks":32},{"name":"UAX","marks":84},{"name":"68u1Mw","marks":59},{"name":"UNnWbKtY","marks":1},{"name":"OApL7ypZ","marks":56},{"name":"teojDdv","marks":41},{"name":"u","marks":79},{"name":"Fea1CjBY","marks":8},{"name":"vZ7DxdFD","marks":62},{"name":"zHMnKFqy1L","marks":74},{"name":"N","marks":51},{"name":"kCbY1","marks":18},{"name":"gIMGwbXseY","marks":97},{"name":"yAh1A0D2o","marks":4},{"name":"GV62KypY6","marks":82},{"name":"Gp1EK","marks":84},{"name":"FOY4foTJP","marks":53},{"name":"l","marks":15},{"name":"gQNkFZPyNx","marks":25},{"name":"C8cFEx","marks":25},{"name":"LWF","marks":28},{"name":"0ybdWt","marks":97},{"name":"gijlaL","marks":91},{"name":"IP","marks":95},{"name":"N73","marks":93},{"name":"S7srQfSg","marks":82},{"name":"T5pDPEF","marks":2},{"name":"Cq","marks":50},{"name":"S1zhLMGpv","marks":29},{"name":"cJWoTJ9c","marks":73},{"name":"Kk7hHhXz","marks":42},{"name":"CVunHYtbtM","marks":85},{"name":"a","marks":71},{"name":"wPADeIgV","marks":16},{"name":"0Gb1yNPnA","marks":29},{"name":"6BYvo3bN","marks":96}]
}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # Fetch marks for the requested names
    results = {n: marks_database.get(n, "Not found") for n in name}
    return results

# Run the API using: uvicorn main:app --reload
