# NetGuardian 🛡️

Um sistema inteligente de detecção e análise de ameaças na rede usando Python e banco de dados SQLite.

## 📋 Descrição

NetGuardian é uma ferramenta de inteligência de ameaças que coleta, armazena e analisa dados sobre IPs maliciosos de múltiplas fontes. O sistema integra dados de listas de bloqueio públicas, permitindo consultas rápidas e visualização de padrões de ameaças em um dashboard interativo.

## 🎯 Objetivo

Fornecer uma plataforma centralizada para:
- Coletar dados de ameaças de múltiplas fontes
- Armazenar informações em banco de dados otimizado
- Consultar IPs suspeitos em tempo real
- Visualizar padrões de ameaças através de dashboards
- Facilitar análise de segurança de rede

## 🏗️ Arquitetura

O projeto é composto por três componentes principais:

### 1. **coletor.py** - Coleta de Dados
- Baixa listas de IPs maliciosos de múltiplas fontes
- Processa e valida os dados coletados
- Armazena as informações no banco de dados SQLite
- Evita duplicatas usando tratamento de exceções

### 2. **consulta.py** - Sistema de Consultas
- Interface interativa em linha de comando
- Permite buscar IPs por endereço
- Permite buscar por tipo de ameaça
- Exibe informações detalhadas sobre registros encontrados

### 3. **dashboard.py** - Visualização
- Gera visualizações gráficas das ameaças
- Exibe proporções de tipos de ameaça
- Utiliza matplotlib e seaborn para gráficos profissionais

### 4. **banco/netguardian.db** - Banco de Dados
- Banco SQLite otimizado com índices
- Armazena histórico de ameaças
- Permite consultas rápidas mesmo com milhões de registros

## ⚙️ Funcionalidades

### Coleta de Dados
- ✅ Download de múltiplas listas de bloqueio
- ✅ Categorização de ameaças por tipo
- ✅ Timestamp de coleta automático
- ✅ Rastreamento da fonte de dados
- ✅ Validação e tratamento de erros

### Tipos de Ameaças Monitoradas
- 🔴 Ataque a serviço SSH
- 📧 Ataque a serviço de Email
- 🌐 Ataque a serviço web (Apache)
- 📬 Ataque a serviço IMAP
- 📁 Ataque a serviço FTP
- 📞 Ataque a serviço SIP
- 🤖 Botnet
- 🔄 IP de ataque recorrente
- 💬 IRC Bot
- 🔐 Brute Force

### Sistema de Consultas
- ✅ Busca por IP específico
- ✅ Busca por tipo de ameaça
- ✅ Filtro por padrão de ameaça
- ✅ Exibição de histórico temporal
- ✅ Interface amigável de menu

### Visualização
- ✅ Gráficos em pizza (proporção de ameaças)
- ✅ Análise de top 5 ameaças
- ✅ Contagem total de registros
- ✅ Temas visuais profissionais

## 🛠️ Requisitos

- **Python 3.x**
- **sqlite3** - Banco de dados (incluído no Python)
- **requests** - Para download de listas
- **pandas** - Manipulação de dados
- **matplotlib** - Visualização de gráficos
- **seaborn** - Temas e estilos de gráficos

### Instalação de dependências

```bash
pip install requests pandas matplotlib seaborn
```

## 🚀 Como usar

### 1. Estrutura de Diretórios

```
netguardian/
├── src/
│   ├── coletor.py          # Script de coleta
│   ├── consulta.py         # Interface de consultas
│   ├── dashboard.py        # Dashboard visual
│   └── .mysql              # Schema do banco de dados
├── banco/
│   ├── netguardian.db      # Banco de dados SQLite
│   └── netguardian.sqbpro  # Projeto SQLiteStudio
└── README.md
```

### 2. Iniciar a Coleta de Dados

```bash
cd src
python coletor.py
```

**Saída esperada:**
```
Iniciando programa
Iniciando coleta de dados. . .
Resposta do banco: OK
Baixando: Ataque a serviço SSH. . .
Resposta HTTP: OK
2541 novos IPs adicionados por Ataque a serviço SSH.
Baixando: Ataque a serviço de Email. . .
...
Processamento concluído
```

### 3. Consultar Ameaças

```bash
cd src
python consulta.py
```

**Menu interativo:**
```
--NETGUARDIAN--
--Escolha uma opção--
1 - Consulta por IP
2 - Consulta por ameaça
0 - Sair

Selecione: 1
Digite o IP a ser verificado (x.x.x.x): 192.168.1.100

-----------------------------------
ALERTA! IP 192.168.1.100 encontrado no banco!

Tipo: Botnet

Detectado em: 2026-02-03 12:45:30

Fonte: https://www.blocklist.de/en/export.html
-----------------------------------
```

### 4. Visualizar Dashboard

```bash
cd src
python dashboard.py
```

**Gera um gráfico em pizza mostrando:**
- Proporção de cada tipo de ameaça
- Porcentagem de ocorrência
- Total de registros analisados

## 📊 Estrutura do Banco de Dados

### Tabela: `ameacas`

```sql
CREATE TABLE ameacas (
    id INTEGER PRIMARY KEY,           -- ID único
    ip_address TEXT NOT NULL,         -- Endereço IP
    tipo_ameaca TEXT,                 -- Tipo de ameaça
    data_coleta DATETIME,             -- Quando foi detectado
    fonte_dados TEXT,                 -- Origem dos dados
    status TEXT DEFAULT 'Ativo'       -- Status da ameaça
);

CREATE INDEX idx_ip_search ON ameacas(ip_address);
```

**Vantagens:**
- Índice otimizado para busca de IPs
- Consultas rápidas mesmo com milhões de registros
- Histórico completo de detecções

## 📝 Detalhamento dos Módulos

### coletor.py
```python
# Principais funções:
- processar_amecas()           # Coleta e processa ameaças
- Conexão com SQLite
- Download de múltiplas fontes
- Validação de dados
- Contagem de novos registros
```

### consulta.py
```python
# Principais funções:
- Consulta.consultar_ip()      # Busca por IP específico
- Consulta.consultar_ameaca()  # Busca por tipo de ameaça
- menu()                       # Interface interativa
```

### dashboard.py
```python
# Principais funções:
- dashboard()                  # Gera visualização
- Leitura de dados com Pandas
- Processamento de dados
- Renderização com Matplotlib
```

## 🔗 Fontes de Dados

O sistema coleta dados de:
- **Blocklist.de** - Lista pública de IPs maliciosos
  - SSH Attacks
  - Email Attacks
  - Apache Attacks
  - IMAP Attacks
  - FTP Attacks
  - SIP Attacks
  - Botnets
  - Strong IPs
  - IRC Bots
  - Brute Force

**URL Principal:** https://lists.blocklist.de/

## 🎓 Casos de Uso

1. **Análise de Segurança** - Verificar IPs suspeitos
2. **Configuração de Firewall** - Criar listas de bloqueio
3. **Investigação de Incidentes** - Correlacionar IPs com ataques
4. **Inteligência de Ameaças** - Identificar padrões de ataque
5. **Relatórios de Segurança** - Gerar visualizações executivas

## ⚠️ Considerações

1. **Atualização Regular** - Execute `coletor.py` periodicamente
2. **Tamanho do Banco** - Pode crescer significativamente
3. **Falsos Positivos** - Algumas listas podem conter IPs legítimos
4. **Performance** - Índices garantem consultas rápidas
5. **Privacidade** - Os dados são públicos de fontes abertas

## 🔄 Fluxo de Trabalho Recomendado

```
1. Coletar dados
   python coletor.py

2. Aguardar atualização (diária/semanal)

3. Consultar ameaças
   python consulta.py

4. Analisar padrões
   python dashboard.py

5. Tomar ações de segurança
   (Bloquear IPs, investigar incidentes, etc)
```

## 📈 Exemplo de Saída do Dashboard

```
Total de registros analisados: 15247

Gráfico em Pizza:
- Botnet: 35%
- Brute Force: 25%
- SSH Attack: 20%
- Outros: 20%
```

## 🔒 Segurança

- Banco de dados local não exposto
- Sem credenciais hardcodeadas
- Dados públicos apenas
- Validação de entrada
- Tratamento de exceções robusto

## 📄 Licença

Este projeto não possui licença especificada.

## 👨‍💻 Autor

[deVictorS](https://github.com/deVictorS)

---

**Nota:** NetGuardian é uma ferramenta educacional para inteligência de ameaças. Use responsavelmente para proteger sua infraestrutura de rede.
