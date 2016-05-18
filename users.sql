CREATE TABLE IF NOT EXISTS users (
    userid int(5) NOT NULL AUTO_INCREMENT,
    username varchar(50) DEFAULT NULL,
    password char(32) DEFAULT NULL,
    PRIMARY KEY(userid)
    );
