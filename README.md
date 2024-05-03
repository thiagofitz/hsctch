# hsctch

#Acessar a pasta onde baixou o arquivo

#Executa o comando abaixo:

#python3 /root/reconx-hsctch.py 

#Digite o domínio alvo (exemplo: dominio.com.br): 

testphp.vulnweb.com


_    _  _____  _____ _______ _____ _    _
| |  | |/ ____|/ ____|__   __/ ____| |  | |
| |__| | (___ | |       | | | |    | |__| |
|  __  |\___ \| |       | | | |    |  __  |
| |  | |____) | |____   | | | |____| |  | |
|_|  |_|_____/ \_____|  |_|  \_____|_|  |_|
                                           

Executando: Executando assetfinder
Comando: assetfinder -subs-only testphp.vulnweb.com | anew subdomains.txt
Saída: 
Executando assetfinder concluído com sucesso.
Executando: Executando httprobe
Comando: cat subdomains.txt | httprobe | tee -a host.txt
Saída: http://testphp.vulnweb.com

Executando httprobe concluído com sucesso.
Executando: Executando waybackurls
Comando: cat host.txt | waybackurls | tee -a endpoint.txt
