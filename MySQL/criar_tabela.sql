use cadastro;
create table if not exists cursos(       # Vai criar a tabela cursos se não existir essa tabela
 nome varchar(30) not null unique,       # O comando unique não vai deixar colocar dois cursos com o mesmo nome
 descricao text,                         # Vai ter a descrição do curso em texto  
 carga int unsigned,                     # A coluna carga será um número inteiro 
 totalaulas int unsigned,                # A coluna totalaulas será um número inteiro
 ano year default '2016'                 # O anop padrão será 2016 
 ) default charset = utf8;

alter table cursos                       # Vai alterar a tabela cursos
add column idcurso int first;            # Vai adicionar o idcurso como primeira coluna

alter table cursos
add primary key(idcursos);               # Vai definir idcursos como chave primária
describe cursos; 
 
