# Kling offical API token generator
- 官方API需要透過 access key 和 secret key 生成API token並帶入才能使用API

## 使用方法
1. 編輯 .env 檔案
 - 包含 AK 和 SK 兩個變數，分別為 access key 和 secret key

2. 啟動docker
- 依序執行以下指令

''' bash
# Docker部屬 
docker build -t fastapi-auth .
# 執行容器 port轉接12345:8000
docker run -d -p 12345:8000 --name auth-api fastapi-auth
docker start auth-api
'''

3. API使用
- API位置
'''bash
POST http
http://domain:12345/authentication
'''
- json body
'''bash
{
    "number":3600,
}
'''
- text return
'''bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBYWhEWU05eTl0R3BiWTRScm5LUVJCOUhlNEFrZk04ZSIsImV4cCI6MTc1MzM3Mzc1NSwibmJmIjoxNzUzMzcwMTU1fQ.fYeBddfeo__B4-12aP7FiMEWpfJFGCYkkFG_444dHbk
'''