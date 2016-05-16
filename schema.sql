use hopscotch;

CREATE TABLE IF NOT EXISTS bands (
    bandid int(5) NOT NULL AUTO_INCREMENT,
    name varchar(255) DEFAULT 'NONAME',
    location varchar(255) DEFAULT 'SOMECLUB',
    showdate date DEFAULT NULL,
    link text DEFAULT NULL,
    description text DEFAULT NULL,
    PRIMARY KEY(bandid)
    );

CREATE TABLE IF NOT EXISTS users (
    userid int(5) NOT NULL AUTO_INCREMENT,
    username varchar(50) DEFAULT NULL,
    password char(32) DEFULAT NULL,
    PRIMARY KEY(userid)
    );

CREATE TABLE IF NOT EXISTS ratings (
    ratingid int(16) NOT NULL AUTO_INCREMENT,
    type char(1) DEFAULT '1',
    rating int(2) DEFUALT '5',
    bandid int(5) NOT NULL,
    userid int(5) NOT NULL,
    KEY (bandid),
    KEY (userid),
    PRIMARY KEY(ratingid)
    );
