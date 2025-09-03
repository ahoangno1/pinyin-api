from flask import Flask, request, jsonify
from flask_cors import CORS
from pypinyin import pinyin, Style

app = Flask(__name__)

# Cấu hình CORS một cách tường minh hơn
# Cho phép tất cả các nguồn gốc với ký tự đại diện '*'
# Hoặc bạn có thể chỉ định cụ thể: cors = CORS(app, resources={r"/get_pinyin": {"origins": "https://www.kanunu8.com"}} )
cors = CORS(app, resources={r"/get_pinyin": {"origins": "*"}})

@app.route('/get_pinyin', methods=['POST'])
def get_pinyin():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text in request body'}), 400
        
    chinese_text = data.get('text', '')
    pinyin_list = pinyin(chinese_text, style=Style.TONE)
    pinyin_str = " ".join([item[0] for item in pinyin_list])

    return jsonify({'pinyin': pinyin_str})

# Bỏ dòng if __name__ == '__main__': pass đi vì nó không cần thiết khi triển khai với Gunicorn
