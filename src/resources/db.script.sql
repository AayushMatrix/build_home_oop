create table labours(
    id int generated always as identity primary key,
    first_name  VARCHAR(50),
    last_name   VARCHAR(50),
    wage        INTEGER,    
    role        VARCHAR(50),
    email       VARCHAR(100)
);