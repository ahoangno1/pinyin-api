from flask import Flask, request, jsonify
from flask_cors import CORS
from pypinyin import pinyin, Style
#1
app = Flask(__name__)

# Cấu hình CORS một cách tường minh, đây là dòng quan trọng nhất
# Nó cho phép endpoint /get_pinyin nhận yêu cầu từ BẤT KỲ tên miền nào (*)
cors = CORS(app, resources={r"/get_pinyin": {"origins": "*"}})

@app.route('/get_pinyin', methods=['POST', 'OPTIONS']) # Thêm 'OPTIONS' để xử lý preflight
def get_pinyin():
    # Xử lý yêu cầu OPTIONS (preflight)
    if request.method == 'OPTIONS':
        return '', 204 # Trả về phản hồi trống cho preflight

    # Xử lý yêu cầu POST
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text in request body'}), 400
        
    chinese_text = data.get('text', '')
    pinyin_list = pinyin(chinese_text, style=Style.TONE)
    pinyin_str = " ".join([item[0] for item in pinyin_list])

    return jsonify({'pinyin': pinyin_str})

# Không cần if __name__ == '__main__': khi triển khai với Gunicorn
