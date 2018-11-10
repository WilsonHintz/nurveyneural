# import the necessary packages
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from keras.models import model_from_json
from threading import Thread
from flask import request
from PIL import Image
import numpy as np
import base64
import flask
import redis
import uuid
import time
import json
import sys
import io

# initialize constants used to control image spatial dimensions and
# data type
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "float32"

# initialize constants used for server queuing
VECTOR_QUEUE = "vector_queue"
BATCH_SIZE = 32
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25

# initialize our Flask application, Redis server, and Keras model
app = flask.Flask(__name__)
db = redis.StrictRedis(host="localhost", port=6379, db=0)
model = None


def base64_encode_image(a):
    # base64 encode the input NumPy array
    return base64.b64encode(a).decode("utf-8")


def base64_decode_image(a, dtype, shape):
    # if this is Python 3, we need the extra step of encoding the
    # serialized NumPy string as a byte object
    if sys.version_info.major == 3:
        a = bytes(a, encoding="utf-8") 

    # convert the string to a NumPy array using the supplied data
    # type and target shape
    a = np.frombuffer(base64.decodestring(a), dtype=dtype)
    a = a.reshape(shape)

    # return the decoded image
    return a


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


def classify_process():
    # load the pre-trained Keras model (here we are using a model
    #  pre-trained on ImageNet and provided by Keras, but you can
    #  substitute in your own networks just as easily)
    print("* Loading model...")
    model = ResNet50(weights="imagenet")
    print("* Model loaded")

    # modelos nurvey ==========
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    nurvey_model = model_from_json(loaded_model_json)
    # load weights into new model
    nurvey_model.load_weights("model.h5")
    print("Loaded model from disk")

    # continually poll for new images to classify
    while True:
        # attempt to grab a batch of images from the database, then
        # initialize the image IDs and batch of images themselves
        queue = db.lrange(VECTOR_QUEUE, 0, BATCH_SIZE - 1)
        vectorsIDs = []
        batch = None

        # loop over the queue loading new data
        for q in queue:
            # deserialize the object and obtain the input image
            q = json.loads(q.decode("utf-8"))

            # check to see if the batch list is None
            if batch is None:
                batch = q

            # otherwise, stack the data
            else:
                batch = np.vstack([batch, q])

            # update the list of image IDs
            vectorsIDs.append(q["id"])

        # check to see if we need to process the batch
        if len(vectorsIDs) > 0:
            # classify the batch
            #print("* Batch size: {}".format(batch.shape))
            predsNurvey = nurvey_model.predict(batch)
            preds = model.predict(batch)
            results = imagenet_utils.decode_predictions(preds)
            print(predsNurvey)

            # loop over the image IDs and their corresponding set of
            # results from our model
            for (imageID, resultSet) in zip(vectorsIDs, results):
                # initialize the list of output predictions
                output = []

                # loop over the results and add them to the list of
                # output predictions
                for (imagenetID, label, prob) in resultSet:
                    r = {"label": label, "probability": float(prob)}
                    output.append(r)

                # store the output predictions in the database, using
                # the image ID as the key so we can fetch the results
                db.set(imageID, json.dumps(output))

            # remove the set of images from our queue
            db.ltrim(VECTOR_QUEUE, len(vectorsIDs), -1)

        # sleep for a small amount
        time.sleep(SERVER_SLEEP)


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}
    print(request.is_json)
    content = request.get_json()
    print(content)

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        #return 'JSON posted'
        # generate an ID for the classification then add the
        # classification ID + image to the queue
        k = str(uuid.uuid4())
        d = {"id": k, "vector": content}
        db.rpush(VECTOR_QUEUE, json.dumps(d))

        # keep looping until our model server returns the output
        # predictions
        while True:
            # attempt to grab the output predictions
            output = db.get(k)

            # check to see if our model has classified the input
            # image
            if output is not None:
                # add the output predictions to our data
                # dictionary so we can return it to the client
                output = output.decode("utf-8")
                data["predictions"] = json.loads(output)

                # delete the result from the database and break
                # from the polling loop
                db.delete(k)
                break

            # sleep for a small amount to give the model a chance
            # to classify the input image
            time.sleep(CLIENT_SLEEP)

        # indicate that the request was a success
        data["success"] = True

        # return the data dictionary as a JSON response
        return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    # load the function used to classify input images in a *separate*
    # thread than the one used for main classification
    print("* Starting model service...")
    t = Thread(target=classify_process, args=())
    t.daemon = True
    t.start()

    # start the web server
    print("* Starting web service...")
    app.run(host='0.0.0.0', debug = False)
