# Launch: yokofukada.com on `lambent-static`

Decided (2026-11-16): the website moves to the droplet; email stays at Fasthosts. Fasthosts charges £37.45 a year for an SSL certificate, while Let's Encrypt on the droplet is free and already routine. The Fasthosts hosting package stays, because it carries the `yoko@yokofukada.com` mailbox.

Who: Jack runs the server commands on `lambent-static`; Stephen edits DNS at Fasthosts and publishes.

## Facts (checked 2026-11-16)

| | Now | After |
|---|---|---|
| `yokofukada.com` A | 88.208.252.228 (Fasthosts), TTL 3600 | 134.122.97.96 (`lambent-static`) |
| `www.yokofukada.com` A | 88.208.252.228 | 134.122.97.96 |
| AAAA | none | none |
| MX | `10 mailserver.livemail.co.uk.` | unchanged |
| `mail` A | 213.171.216.40 | unchanged |
| `webmail` A | 213.171.216.229 | unchanged |
| TXT (SPF) | `v=spf1 mx a include:_spf.livemail.co.uk ~all` | unchanged (see note) |
| CAA | none (any CA may issue) | unchanged |
| Nameservers | `ns1–3.livedns.co.uk` (Fasthosts) | unchanged |

SPF note: the `a` mechanism authorises whatever the A record points at to send mail. After the move that is the droplet, which sends no mail for this domain, so it's harmless. Fasthosts' mail servers stay authorised through `mx` and the `include`.

## 1. Prepare (any time before the DNS change)

1. **Lower the TTL** of the two A records (`@`, `www`) from 3600 to 300 at Fasthosts, at least an hour before step 3, so the switch (and any rollback) takes effect quickly. Stephen.
2. **Site folder** on the droplet. Jack:

   ```sh
   sudo mkdir /var/www/yokofukada.com
   sudo chown stephen: /var/www/yokofukada.com    # same owner as wireframes/yokofukada/
   sudo restorecon -Rv /var/www/yokofukada.com     # SELinux is enforcing
   ```

3. **Publish** to it: `lib/publish production` (dry run), then `lib/publish --go production`. Stephen.
4. **Nginx site**, HTTP only for now, following the pattern of the other sites' confs (IPv6 `listen` lines, log paths). Jack, e.g. `/etc/nginx/conf.d/yokofukada.com.conf`:

   ```nginx
   server {
       listen 80;
       server_name yokofukada.com www.yokofukada.com;
       root /var/www/yokofukada.com;
       index index.html;

       # Old addresses
       location = /jewellery.php { return 301 /jewellery.html; }
       location = /jw.php        { return 301 /jewellery.html; }
       location ^~ /ifproject/   { return 301 /; }

       location / { try_files $uri $uri/ =404; }
   }
   ```

   Then `sudo nginx -t && sudo systemctl reload nginx`.
5. **Test before DNS**, from the Mac:

   ```sh
   curl -sI --resolve yokofukada.com:80:134.122.97.96 http://yokofukada.com/
   curl -sI --resolve yokofukada.com:80:134.122.97.96 http://yokofukada.com/jewellery.php   # 301
   curl -s  --resolve yokofukada.com:80:134.122.97.96 http://yokofukada.com/version.txt
   ```

## 2. Switch DNS

6. At Fasthosts, change the A records for `@` and `www` to `134.122.97.96`. Touch nothing else. Stephen.
7. Check that the authoritative servers have it, then public resolvers:

   ```sh
   dig +short yokofukada.com @ns1.livedns.co.uk
   dig +short www.yokofukada.com @ns1.livedns.co.uk
   dig +short yokofukada.com @1.1.1.1
   ```

   Let's Encrypt asks the authoritative servers, so certbot can run as soon as `ns1–3` answer with the new address. Visitors follow as the old TTL runs out.

## 3. HTTPS

8. Jack:

   ```sh
   sudo certbot --nginx -d yokofukada.com -d www.yokofukada.com --redirect
   ```

   Then make sure `/etc/letsencrypt/renewal/yokofukada.com.conf` says `installer = nginx`, so that Nginx reloads after renewal (the root crontab already runs `certbot renew`).
9. **Canonical name**: the apex. In the HTTPS server block, send `www` to it:

   ```nginx
   if ($host = www.yokofukada.com) { return 301 https://yokofukada.com$request_uri; }
   ```

   `sudo nginx -t && sudo systemctl reload nginx`.

Between steps 6 and 8, `https://yokofukada.com` reaches the droplet's default certificate and shows a browser warning. The old site had no HTTPS, so no existing links use it. Keep the gap short: do steps 6–8 in one sitting.

## 4. Check

10. From the Mac: `http://` → `https://`; `www` → apex; every page and image 200; `/jewellery.php` → `/jewellery.html`; `version.txt` shows the published commit; a certificate for both names. Screenshots at desktop and phone width.
11. Send a test email to and from `yoko@yokofukada.com` (it should be unaffected).
12. Push the `published-YYYY-MM-DD` tag that `lib/publish` made.
13. Put the TTLs back to 3600 after a few days.
14. Watch the Nginx 404 log for a couple of weeks for old addresses we missed.

## Rollback

Point the two A records back to 88.208.252.228. The old site on Fasthosts is untouched (and saved in `prev/ftp/htdocs/`). With TTL 300, the rollback takes effect within minutes.

## Afterwards

- Leave the old web content on Fasthosts as it is: nothing reaches it by name, and it serves as a fallback.
- Staging (`wireframes/yokofukada/`) stays, for previewing future changes.
