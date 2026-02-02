import requests
import sqlite3
from datetime import datetime

print("Iniciando programa")

DB_PATH = "../banco/netguardian.db"
BLACKLIST = {
    "https://lists.blocklist.de/lists/ssh.txt" : "Ataque a serviço SSH",
    "https://lists.blocklist.de/lists/mail.txt" : "Ataque a serviço de Email",
    "https://lists.blocklist.de/lists/apache.txt": "Ataque a serviço web (Apache)",
    "https://lists.blocklist.de/lists/imap.txt" : "Ataque a serviço IMAP",
    "https://lists.blocklist.de/lists/ftp.txt" : "Ataque a serviço FTP",
    "https://lists.blocklist.de/lists/sip.txt" : "Ataque a serviço SIP",
    "https://lists.blocklist.de/lists/bots.txt":"Botnet",
    "https://lists.blocklist.de/lists/strongips.txt" : "IP de ataque recorrente",
    "https://lists.blocklist.de/lists/ircbot.txt" : "IRC Bot",
    "https://lists.blocklist.de/lists/bruteforcelogin.txt" : "Brute Force"
}


def processar_amecas():
    print("Iniciando coleta de dados. . .")

    #conecta com DB
    try:
        conexao = sqlite3.connect(DB_PATH)
        print(f"Resposta do banco: OK")
        cursor = conexao.cursor()
    except sqlite3.Error as e:
        print(f"Erro: {e}")

    for url, motivo in BLACKLIST.items():
        print(f"Baixando: {motivo}. . .")

        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                print(f"Resposta HTTP: OK")
                ips = resposta.text.split('\n')
                contador_novos = 0

                for ip in ips:
                    ip = ip.strip()
                    if ip:      
                        try:
                            data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            url_principal = "https://www.blocklist.de/en/export.html"
                            cursor.execute("""
                                INSERT INTO ameacas (ip_address, tipo_ameaca, data_coleta, fonte_dados)
                                VALUES (?, ?, ?, ?)
                            """, (ip, motivo, data_atual, url_principal))
                            contador_novos += 1
                        except sqlite3.IntegrityError:
                            #caso já tenha o ip ou erro no banco
                            continue

                print(f"{contador_novos} novos IPs adicionados por {motivo}.")   
            else:
                print(f"Falha ao acessar {url}")
        except Exception as e:
            print(f"Erro na URL {url}: {e}")
    conexao.commit()
    conexao.close()
    print("Processamento concluído")


if __name__ == "__main__":
    processar_amecas()

