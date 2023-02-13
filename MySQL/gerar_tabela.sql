use basededados;
create table informacoes(
ID varchar(45) not null,
produtoID varchar(45) not null,
clienteID int(5) not null,
Desconto decimal(4,2) not null,
Preco decimal(5,1) not null,
Quantidade int(1) not null,
IDarmazenado int(1) not null,
ddata varchar(10) not null,
primary key(ID)) default charset=utf8mb4;
