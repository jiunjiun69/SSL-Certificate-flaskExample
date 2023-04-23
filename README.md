# ZeroSSL-Certificate-useFlask

### 要驗證的txt檔放在cert資料夾中
```
flask run --host=host --port=port
```

### Certbot test
```
certbot certonly --nginx --email email@example.com --agree-tos -d example.com --dry-run
```


### SSL Certificate
```
ssl_certificate /usr/local/etc/letsencrypt/live/<domain>/fullchain.pem
ssl_certificate_key /usr/local/etc/letsencrypt/live/<domain>/privkey.pem
```

### Nginx
```
/usr/local/etc/nginx/nginx.conf
```

### Jails root
```
/mnt/<home>/iocage/jails/<app>/root
```

### Jails -> SSL Certificate
```
/mnt/<home>/iocage/jails/<app>/root/usr/local/etc/letsencrypt/live/<domain>
```

### Nginx restart
```
service nginx restart
```
