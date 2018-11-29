#!/bin/bash

sudo curl -s "https://api.github.com/repos/gophish/gophish/releases/latest" | jq -r '.assets[] | select(.name | endswith("linux-64bit.zip" )).browser_download_url' | xargs sudo curl -L -o /opt/gophish.zip --url
unzip -qq /opt/gophish.zip -d /opt/gophish
cd /opt/gophish
jq '.admin_server.listen_url = "0.0.0.0:3333"' config.json >> tmp.json
rm config.json && mv tmp.json config.json
