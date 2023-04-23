# ZeroSSL-Certificate-useFlask

### 要驗證的txt檔放在cert資料夾中
```
flask run --host=host --port=port
```

### Certbot test
```
certbot certonly --nginx --email email@example.com --agree-tos -d example.com --dry-run
```
