import json
from flask import Flask, Response
import os
import random

API_PORT = int(os.environ.get('API_PORT', 5000))

app = Flask(__name__)

@app.route("/inference/<string:token>")
def generate_inference(token):
    """Generate inference for given token."""
    if not token or token not in ["R"]:
        error_msg = "Token is required" if not token else "Token not supported"
        return Response(json.dumps({"error": error_msg}), status=400, mimetype='application/json')

    try:
        random_value = random.uniform(70, 80)
        inference = round(random_value, 2)
        return Response(str(inference), status=200)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=API_PORT)
