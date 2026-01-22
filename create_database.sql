drop database 	if exists pizza;
create database pizza; 
use pizza;

create table sabores(
id int primary key auto_increment,
sabor varchar(100),
tamanho varchar(100)

);

INSERT INTO sabores (sabor)
VALUES 
('calabresa', 'P'),
('chocolate', 'M'),
('frango com catipiry','G'),
('baiana','P'),
('portuguesa', 'G');

select * from sabores;

DROP TABLE IF EXISTS CLIENTE;	
create table CLIENTE(
id int primary key auto_increment,
nome varchar(150),
cpf varchar(14) not null,
id_sabor int,

foreign key (id_sabor) references sabores(id)


);

insert into CLIENTE (nome, cpf, id_sabor) values ('Maria leide da silva', '123.123.123-12', 2);

select * from CLIENTE;


SELECT SABORES.SABOR, CLIENTE.NOME FROM CLIENTE INNER JOIN SABORES ON (CLIENTE.ID_SABOR = SABORES.ID );





