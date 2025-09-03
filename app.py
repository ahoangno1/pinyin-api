# app.py
from flask import Flask, request, jsonify
from pypinyin import pinyin, Style

app = Flask(__name__)

@app.route('/get_pinyin', methods=['POST'])
def get_pinyin():
    data = request.json
    chinese_text = data.get('text', '')
    pinyin_list = pinyin(chinese_text, style=Style.TONE)
    
    # Kết quả pinyin là một list các list, ví dụ: [['ni'], ['hao']]
    # Bạn nên xử lý để trả về chuỗi pinyin dễ đọc hơn.
    pinyin_str = " ".join([item[0] for item in pinyin_list])

    return jsonify({'pinyin': pinyin_str})

if __name__ == '__main__':
    # Khi chạy trên Render, Gunicorn sẽ xử lý việc chạy app, không cần dòng này
    # app.run(host='0.0.0.0', port=5000)
    pass
