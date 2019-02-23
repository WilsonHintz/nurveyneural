import numpy
from flask import Flask
from flask import request, jsonify
from keras.models import model_from_json

app = Flask(__name__)
loaded_model = None


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    print(content['x'])

    dataset = numpy.fromstring(content['x'], sep=",")
    dataset2 = numpy.vstack([dataset, dataset])
    global loaded_model
    salida = loaded_model.predict(dataset2[:, 0:24])

    print("")
    print("salida")
    i, j = numpy.unravel_index(salida.argmax(), salida.shape)
    print("categoria")
    categoriaNSE(j)
    print(categoriaNSE(j))
    data = {'Categoria': categoriaNSE(j)}

    #return 'Categoria ' + categoriaNSE(j)
    return jsonify(data), 200


def categoriaNSE(nivel):
    return {
        0: "E",
        1: "E",
        2: "D2",
        3: "D1",
        4: "C3",
        5: "C2",
        6: "C1",
        7: "AB"
    }.get(nivel, "error")

def loadModel():
    json_file = open('./models/modelNoBin.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    global loaded_model
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("./models/modelNoBin.h5")

    print("Loaded model from disk")


if __name__ == "__main__":
    # start the web server
    print("* Starting web service...")
    loadModel()
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=False)
