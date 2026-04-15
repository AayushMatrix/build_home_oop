create table labours(
    id int generated always as identity primary key,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    wage        INTEGER,    
    role        VARCHAR(50),
    email       VARCHAR(100)
);


CREATE TABLE attendance (
    id         INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    labour_id  INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time   TIMESTAMP,
    FOREIGN KEY (labour_id) REFERENCES labours(id)
);


CREATE TABLE skills (
    id         INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    labour_id  INTEGER NOT NULL,
    skill varchar(100),
    FOREIGN KEY (labour_id) REFERENCES labours(id)
);