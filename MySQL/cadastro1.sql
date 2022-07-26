create database cadastro                        # Vai criar o banco de dados cadastro 
default character set utf8                      
default collate utf8_general_ci;

create table pessoas(                          # Vai criar a tabela pessoas no banco de dados cadastro 
  id int not null auto_increment,              # id é um número inteiro não nulo e a informação é autoincrementável, autonumeração de novos ids
  nome varchar(30) not null,                   # Quantidade de caracteres variável até 30 caracteres e comando not null não aceitará ficar sem o nome  
  nascimento date,
  sexo enum('M','F'),                          # O comando enum vai aceitar apenas M ou F 
  peso decimal(5,2),                           # Total de 5 algarismos com 2 algarismos após o ponto decimal
  altura decimal(3,2),                         # Total de 3 algarismos com 2 algarismos após o ponto decimal
  nacionalidade varchar(20) default 'Brasil',  # Caracteres variando até 20 caracteres e se não digitar a nacionalidade, o padrão será o Brasil
  primary key (id)                             # Chave primária serve para identificar cada uma das tuplas e não repetir tuplas dentro de uma tabela  
) default charset = utf8;                      # Vai aceitar carcteres acentuados no padr
describe pessoas;
