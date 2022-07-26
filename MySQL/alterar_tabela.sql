use cadastro;
alter table pessoas
add column profissao varchar(10) after nome;     #Vai adicionar a coluna profissão depois da coluna nome
select * from pessoas;
