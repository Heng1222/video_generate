# Copyright (c) 2025 Stephen G. Pope
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from flask import Blueprint, send_from_directory, jsonify
from config import LOCAL_STORAGE_PATH
import os
import logging
from services.authentication import authenticate
from app_utils import queue_task_wrapper

v1_video_download_bp = Blueprint('v1_video_download', __name__)
logger = logging.getLogger(__name__)

@v1_video_download_bp.route('/v1/video/download/<path:filename>', methods=['GET'])
def download_video( filename):
    """Download a processed video file from the local storage directory."""
    logger.info(f"Job : Received download request for file: {filename}")

    try:
        # 防止路徑穿越攻擊
        if ".." in filename or filename.startswith("/"):
            logger.warning(f"Job : Invalid path attempt: {filename}")
            return jsonify({"error": "Invalid file path"}), 400

        full_path = os.path.join(LOCAL_STORAGE_PATH, filename)

        # 檢查檔案是否存在
        if not os.path.exists(full_path):
            logger.error(f"Job : File not found: {filename}")
            return jsonify({"error": f"File not found: {filename}"}), 404

        logger.info(f"Job: Serving file from local storage: {full_path}")
        return send_from_directory(LOCAL_STORAGE_PATH, filename, as_attachment=True)

    except Exception as e:
        logger.error(f"Job: Download failed for file {filename} - {str(e)}")
        return jsonify({"error": f"Download failed: {str(e)}"}), 500
