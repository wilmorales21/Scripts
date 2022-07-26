use cadastro;
insert into pessoas                                         # Vai inserir informações na tabela pessoas
(id,nome,nascimento,sexo,peso,altura,nacionalidade)         # Informaç
values
('1','Godofredo','1983-01-02','M','78.5','1.83','Brasil'),
('2','Maria','1988-06-21','F','54.5','1.64','Portugal'),
('3','Renata','1980-11-08','F','50.1','1.68','Uruguai');
select * from pessoas;
