# # from flask import Flask, render_template, request
# # from encryption import encrypt_data, hash_keyword

# # app = Flask(__name__)

# # # Simulated storage
# # cloud = {
# #     'encrypted_data': None,
# #     'hashed_keyword': None
# # }

# # @app.route('/', methods=['GET', 'POST'])
# # def home():
# #     if request.method == 'POST':
# #         data = request.form['filedata']
# #         keyword = request.form['keyword']
# #         cloud['encrypted_data'] = encrypt_data(data)
# #         cloud['hashed_keyword'] = hash_keyword(keyword)
# #     return render_template("index.html", result=cloud)

# # if __name__ == "__main__":
# #     app.run(debug=True)
from flask import Flask, render_template, request
import requests
from encryption import encrypt_data, hash_keyword  # your own logic

app = Flask(__name__)

# Simulated storage
cloud = {
    'encrypted_data': None,
    'hashed_keyword': None
}

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    ict = None
    error = None
    verification_result = None

    if request.method == 'POST':
        if 'filedata' in request.form and 'keyword' in request.form:
            # Data Owner section
            data = request.form['filedata']
            keyword = request.form['keyword']
            cloud['encrypted_data'] = encrypt_data(data)
            cloud['hashed_keyword'] = hash_keyword(keyword)
            result = cloud

        elif 'encrypted_keyword' in request.form and 'trapdoor' in request.form and 'ict' not in request.form:
            # Assistant Server section
            encrypted_keyword = request.form.get('encrypted_keyword')
            trapdoor = request.form.get('trapdoor')
            try:
                response = requests.post("http://127.0.0.1:6000/generate", json={
                    "encrypted_keyword": encrypted_keyword,
                    "trapdoor": trapdoor
                })
                if response.status_code == 200:
                    ict = response.json().get('intermediate_ciphertext')
                else:
                    error = "Failed to generate ICT. Check your inputs or server."
            except Exception as e:
                error = f"Error connecting to Assistant Server: {str(e)}"

        elif 'ict' in request.form and 'encrypted_keyword' in request.form and 'trapdoor' in request.form:
            # Test Server section
            ict = request.form.get('ict')
            encrypted_keyword = request.form.get('encrypted_keyword')
            trapdoor = request.form.get('trapdoor')

            expected = encrypted_keyword[:16] + trapdoor[-16:]
            if ict == expected:
                verification_result = "✅ Match confirmed — Intermediate Ciphertext is correct."
            else:
                verification_result = "❌ Mismatch — Intermediate Ciphertext is incorrect."

    return render_template("index.html", result=cloud, ict=ict, error=error, verification_result=verification_result)

if __name__ == "__main__":
    app.run(debug=True)
