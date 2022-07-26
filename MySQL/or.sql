use cadastro;
select nome, totalaulas from cursos
where carga > 35 or totalaulas < 30;   # Vai selecionar os cursos que tem a carga maior que 35 ou total de aulas menor que 30
describe cursos;
