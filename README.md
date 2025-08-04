# 自動化AI影片生成 環境
- n8n(自動化流程) 本地部屬
- baserow(資料庫) 本地部屬
- no-code-architects-toolkit(影片剪輯API) 本地部屬
- LLM、video model使用API連線，於n8n中設定
- (optional) Kling official API 需要JWT加密產生API token，kling_authentication 本地部屬內部API產生

## 引用開源專案

以下為本專案引用之其他開源專案資訊，並遵循其授權條款。本專案依據 GPL-2.0 發佈。

---

### 1. [No-Code Architects Toolkit](https://github.com/stephengpope/no-code-architects-toolkit)

- 📁 路徑：`no-code-architects-toolkit/`
- 📜 詳見：`no-code-architects-toolkit/LICENSE`

---

### 2. [Baserow](https://gitlab.com/baserow/baserow.git)

- 📁 路徑：`baserow/`
- 📜 詳見：`baserow/LICENSE`

---

### 3. [ai-automation-n8n](https://github.com/qwedsazxc78/ai-automation-n8n.git)

- 📁 路徑：`n8n/`
- 📜 詳見：`n8n/LICENSE`


## 安裝方法
``` bash
git clone https://github.com/Heng1222/video_generate.git
cd video_generate
```
### 1. n8n建置
 - 使用 `n8n/public/docker-compose.yml`部署
 - ngork 建立外部連線
 - docker networks設定，啟動專案需要先部屬n8n再部屬其他
 - 修改`env.example`變數並改名為`.env`
 ``` bash
 cd n8n/public
 docker compose up -d
 ```
### 2. baserow建置
 - 使用`baserow/docker-compose.all-in-one.yml`部署
 - 因為有docker networks設定，須先完成n8n部署
 - 修改`env.example`變數並改名為`.env`
``` bash
 cd ./baserow
 docker compose up -f ./docker-compose.all-in-one.yml -d
 ```

### 3. NCA 建置
 - 使用`no-code-architects-toolkit/docker-compose.yml`部署
 - 因為有docker networks設定，須先完成n8n部署
 - 修改`env.example`變數並改名為`.env`
``` bash
 cd ./no-code-architects-toolkit
 docker compose up -d
 ```
### 4. Kling_auth 建置
 - 若有使用official Kling API才需要建置此API
 - 使用`kling_authentication/Dockerfile`部屬 
 - 因為有docker networks設定，須先完成n8n部署
 - 修改`env.example`變數並改名為`.env`
 ``` bash
 cd ./kling_authentication
 docker up -d
 ```

## port號使用
| 名稱       | 外部 port | 內部 port | 備註         |
|------------|-----------|-----------|--------------|
| PostgreSQL | 5432      | 5432      | X    |
| n8n        | 5678      | 5678      | X |
| Baserow    | 8080      | 80        | X |
| Baserow    | 4431      | 443        | X |
| Ngrok      | 4040      | 4040      | X      |
| NCA      | 5050      | 8080      | X      |
| Kling API token      | 12345      | 8000      | X      |

TODO:
- [ ] fb ig 同步上傳
- [ ] 工作流備份

