# Integração MS SQL Server com Python
O integrador funciona tanto com Windows quanto Unix.

Com este pequeno software, você pode executar a query que deseja via Python.
Na versão v0.0.1: Teste simples de insert pré-fixado ao Python.
Na versão v0.0.2: Em desenvolvimento...


## Pré requisitos sistema operacional Windows:
Contando que o Python esteja instalado.

No cmd instalate o pyodbc:
```batch
pip install pyodbc
pip install --upgrade pip
```

## Container Microsoft SQL Server:
Este container será utilizado para o banco de dados, caso você não tenha uma instalação já efetivada.

Crie os diretórios:
```batch
sudo mkdir -p /container/sql-server/sqlserver/data
```
Execute a composição do container do mssql:
```batch
docker-compose -f mssql_compose.yaml up -d
```

## Pré requisitos sistema operacional Unix:
Contando que o Python esteja instalado.

# Instale o unixodbc-dev para usar drivers ODBC no Unix:
Fonte:(https://www.unixodbc.org/)
```batch
sudo apt-get install unixodbc-dev python3-pymssql -y
```
# Instale o gerenciador de pacotes Python:
```batch
sudo apt-get install python-pip python3-pip -y
```
# Modo de instalação 01
No shell crie o script abaixo:
```shell
vim install_odbc_sqlserver.sh
```

Cole o conteúdo abaixo no script:

```shell
if ! [[ "18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi

sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

exit
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
source ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install -y unixodbc-dev
```
Dê permissão ao script para execução:
```shell
chmod +x install_odbc_sqlserver.sh
```

Execute o script instale o pyodbc:

```shell
./install_odbc_sqlserver.sh
```

# Modo de instalação 02
No shell execute os comandos abaixo:
```shell
wget https://packages.microsoft.com/ubuntu/21.04/prod/pool/main/m/msodbcsql18/msodbcsql18_18.0.1.1-1_amd64.deb
wget https://packages.microsoft.com/ubuntu/21.04/prod/pool/main/m/mssql-tools18/mssql-tools18_18.0.1.1-1_amd64.deb
sudo dpkg -i msodbcsql18_18.0.1.1-1_amd64.deb
sudo dpkg -i mssql-tools18_18.0.1.1-1_amd64.deb
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
```

## Query no MS SQL Server

# Sintaxe para conexão ao SQL Server:

```sql
SINTAXE: /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Sua_Senha
```

# Criando database:
Utilize a sintaxe para conexão ao SQL Server antes.

```sql
CREATE DATABASE caio_db;
GO
USE caio_db;
GO
CREATE TABLE Vendas (
    id_venda int, 
    cliente varchar(255), 
    produto varchar(255), 
    data_venda date, 
    preco decimal(12, 2), 
    quantidade int,
    )
GO
```

# Inserindo dados:
Utilize a sintaxe para conexão ao SQL Server antes.

```sql
USE caio_db;
INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (1, 'Caio', 'Computer', GetDate(), 7680, 1)
GO
```
# Consultando dados:
Utilize a sintaxe para conexão ao SQL Server antes.

```sql
USE caio_db;
SELECT * FROM Vendas;
GO
```

# Documentação da prova de conexão:
https://learn.microsoft.com/pt-br/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16