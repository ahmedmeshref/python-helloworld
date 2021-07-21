from flask import Flask, jsonify
import logging

app = Flask(__name__)


@app.get("/")
def hello():
    logger.info('home route requested successfully')

    return 'hello'


@app.get("/status")
def health():
    response = jsonify({"result": "OK - healthy"})
    logger.info('status route requested successfully')

    return response


@app.get('/metrics')
def metrics():
    response = jsonify({"data": {"UserCount": 140, "UserCountActive": 23}})
    logger.info('metrics route requested successfully')

    return response

if __name__ == "__main__":
    # create logger
    logger = logging.getLogger(__name__)
    # set the level of logging for the logger
    logger.setLevel(logging.INFO)
    # setup formatter 
    formatter = logging.Formatter('%(asctime)-15s: %(name)s: %(message)s')
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    app.run(debug=True, host='0.0.0.0')
