USE Pycoder:

CREATE TABLE produtos(
    id interger not null auto_increment, 
    produto varchar(30) not null,
    descricao varchar(50) not null,
    preco_original int not null,
    preco_promocional int not null,
    comercio varchar(30) not null,
    endereco varchar(40) not null,
    telefone varchar(12) not null,
    validade date not null,
    PRIMARY KEY(id)
    
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connetion = utf8_general_ci;

INSERT INTO produtos (produto, descicao, preco_original, preco_promocional, comercio, endereco, telefone, validade)
 VALUES ('feijoada' 'feijoada almoco','50.00','40.00','restaurante fazenda', 'rua joao mineiro 75', '2000-0000','01\04\2024')