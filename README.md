# SSL-Certificate-useFlask

### 要驗證的txt檔放在cert資料夾中
```
flask run --host=host --port=port
```

### Certbot test
```
certbot certonly --nginx --email email@example.com --agree-tos -d example.com --dry-run
```

or

```
certbot certonly --manual --preferred-challenges http -m email@example.com -d example.com --dry-run
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

### Jails root (FreeBSD) TrueNAS Core（以前為 FreeNAS，基於 FreeBSD）
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

### Kubernetes Pod root (Debian) TrueNAS Scale（基於 Debian） <<FreeBSD Jails -> Kubernetes Pod>>
```
/mnt/<home>/ix-applications/releases/
```
  
### 刷新 Nextcloud 資料
```
先給權限：

chown -R www-data:www-data <path/to/new/files>

然後掃描

cd "path/to/occ/file"
sudo -u www-data php occ files:scan --all
```
  
### docker中的Nextcloud掃描法
https://github.com/nextcloud/all-in-one/discussions/1503#discussioncomment-4362198
  
先`docker ps`找出對應容器
  
```
sudo docker exec --user www-data -it <容器名稱> php occ files:scan --all
```
