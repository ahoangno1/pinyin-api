from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Import the CORS object
from pypinyin import pinyin, Style

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for the entire app

@app.route('/get_pinyin', methods=['POST'])
def get_pinyin():
    data = request.json
    chinese_text = data.get('text', '')
    pinyin_list = pinyin(chinese_text, style=Style.TONE)

    pinyin_str = " ".join([item[0] for item in pinyin_list])

    return jsonify({'pinyin': pinyin_str})

if __name__ == '__main__':
    pass
