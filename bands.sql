CREATE TABLE IF NOT EXISTS bands (
    bandid int(5) NOT NULL AUTO_INCREMENT,
    name varchar(255) DEFAULT 'NONAME',
    location varchar(255) DEFAULT 'SOMECLUB',
    showdate date DEFAULT NULL,
    link text DEFAULT NULL,
    description text DEFAULT NULL,
    PRIMARY KEY(bandid)
    );
