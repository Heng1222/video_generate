import os
from flask import Blueprint, send_from_directory, jsonify
from config import LOCAL_STORAGE_PATH

download_api = Blueprint('download_api', __name__, url_prefix='/v1/file')

@download_api.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """
    允許使用者下載本地儲存在 LOCAL_STORAGE_PATH 中的檔案。
    僅限此資料夾內的檔案（防止路徑穿越漏洞）。
    """
    try:
        # 防止路徑穿越攻擊
        if ".." in filename or filename.startswith("/"):
            return jsonify({'error': 'Invalid file path'}), 400

        file_path = os.path.join(LOCAL_STORAGE_PATH, filename)

        # 檢查檔案是否存在
        if not os.path.exists(file_path):
            return jsonify({'error': f'File not found: {filename}'}), 404

        # 回傳檔案，使用 Flask 原生 send_from_directory，適合大檔案
        return send_from_directory(LOCAL_STORAGE_PATH, filename, as_attachment=True)
    except Exception as e:
        print(f"File download failed: {str(e)}")
        return jsonify({'error': f'Failed to download file: {str(e)}'}), 500
