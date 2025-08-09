from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to create intermediate ciphertext
def create_intermediate_ciphertext(encrypted_keyword, trapdoor):
    return encrypted_keyword[:16] + trapdoor[-16:]

# Endpoint to receive data and generate intermediate ciphertext
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    encrypted_keyword = data.get('encrypted_keyword')
    trapdoor = data.get('trapdoor')

    if not encrypted_keyword or not trapdoor:
        return jsonify({"error": "Missing encrypted_keyword or trapdoor"}), 400

    intermediate = create_intermediate_ciphertext(encrypted_keyword, trapdoor)
    return jsonify({"intermediate_ciphertext": intermediate})

# Run the assistant server on port 6000
if __name__ == "__main__":
    app.run(port=6000, debug=True)