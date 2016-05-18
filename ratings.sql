CREATE TABLE IF NOT EXISTS ratings (
    ratingid int(16) NOT NULL AUTO_INCREMENT,
    type char(1) DEFAULT '1',
    rating int(2) DEFAULT '5',
    bandid int(5) NOT NULL,
    userid int(5) NOT NULL,
    KEY (bandid),
    KEY (userid),
    PRIMARY KEY(ratingid)
    );
