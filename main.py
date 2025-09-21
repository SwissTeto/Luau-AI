from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    reply = "You said: " + user_input
    return jsonify({'text': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
  
