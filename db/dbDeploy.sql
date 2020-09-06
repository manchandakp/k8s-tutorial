CREATE TABLE IF NOT EXISTS registrations
(
    registration_id serial,
    person_name varchar(100),
    person_email varchar(100),
    person_phone varchar(100),
    registration_datetime timestamp default NOW()
);

COMMIT;