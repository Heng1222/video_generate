# 自動化AI影片生成 環境
- n8n(自動化流程) 本地部屬
- baserow(資料庫) 本地部屬
- no-code-architects-toolkit(影片剪輯API) 本地部屬
- LLM、video model使用API連線，於n8n中設定
- (optional) Kling official API 需要JWT加密產生API token，kling_authentication 本地部屬內部API產生

## n8n
 - 使用 n8n/local-ai/public/docker-compose.yml部署
 - ngork建立外部連線
 - docker networks設定，啟動專案需要先部屬n8n再部屬其他
## baserow
 - 使用baserow/docker-compose.all-in-one.yml部署
 - 因為有docker networks設定，須先完成n8n部署

## NCA
 - 使用no-code-architects-toolkit/docker-compose.yml部署
 - 因為有docker networks設定，須先完成n8n部署

# port號使用
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
- [ ] .env.example
- [ ] fb ig 同步上傳
- [ ] 工作流備份
- [ ] ffmpeg剪輯
- [ ] PiAPI 切換
