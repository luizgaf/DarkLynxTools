#!/bin/bash

url="http://rh.businesscorp.com.br/?page="
wordlist="/usr/share/wordlists/dirb/small.txt"

echo "[*] Testando URLs em: $url"

for word in $(cat "$wordlist"); do
    full_url="$url$word"
    
    # Pega HTTP STATUS + TAMANHO da resposta
    response=$(curl -A "Mozilla" -s -o /dev/null -w "%{http_code} %{size_download}" "$full_url")
    code=$(echo "$response" | awk '{print $1}')
    size=$(echo "$response" | awk '{print $2}')

    # Filtra: Só mostra se for HTTP 200 E tamanho > 1700 bytes
    if [ "$code" == "200" ] && [ "$size" -gt 4700 ]; then
        echo "[+] $full_url /// status: $code / size: $size bytes"
    fi
done
