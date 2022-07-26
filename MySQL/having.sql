use cadastro;
select carga, count(nome) from cursos
group by carga
having count(nome) > 2;               # Vai mostrar a quantidade de cursos(maior que 2) que tiverem a maior carga horaria
