# 使用輕量版 python 作為基底映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製需求與程式碼
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY .env .
# 啟動 FastAPI Server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# docker run
# docker run -d -p 12345:8000 --name auth-api fastapi-auth