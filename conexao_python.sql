create database cinema;
use cinema;

CREATE TABLE ingressos (
    id INT NOT NULL AUTO_INCREMENT,
    filme VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (id)
) DEFAULT CHARSET = utf8;

select * from ingressos;