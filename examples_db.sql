---- insert data into user table for PostgreSQL
--INSERT INTO auth_user (is_superuser, email, password, is_active, is_staff, created_at, updated_at)
--VALUES
--    (true, 'e22yford@gmail.co', md5('123'), true, true, NOW(), NOW()),
--    (true, '2ryord@gmail.co',  pgp_sym_encrypt('123', 'key'), true, true, NOW(), NOW()),
--    (true, 'a2eox@gmail.co', crypt('123', gen_salt('bf')), true, true, NOW(), NOW()) ,
----    (true, 'a2ox@gmail.co',  SHA2('ford1980', 256), true, true, NOW(), NOW
----()) , ----FOR MYSQL
--    (false, 'genryford@gmail.co', crypt('ford1980', gen_salt('bf')), true, false, NOW(), NOW());


-- insert data into user table for SQLite
INSERT INTO auth_user(is_superuser, email, password, is_active, is_staff, created_at, updated_at)
VALUES
    (FALSE, 'objohnson@gmail.co', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', TRUE, FALSE, '2023-12-23 12:30:26.729465', '2023-12-23 12:30:26.729465'),
    (FALSE, 'lexfox@gmail.co', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', TRUE, FALSE, '2023-12-23 12:30:26.729465', '2023-12-23 12:30:26.729465'),
    (FALSE, 'ndrbot@gmail.co', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', TRUE, FALSE, '2023-12-23 12:30:26.729465', '2023-12-23 12:30:26.729465'),
    (FALSE, 'enryford@gmail.co', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', TRUE, FALSE, '2023-12-23 12:30:26.729465', '2023-12-23 12:30:26.729465');



--INSERT INTO profile(name, surname, age, user_id)
--VALUES
--    ('Bob', 'Johnson', 30, 1),
--    ('Alex', 'Fox', 33, 2),
--    ('Andru', 'Bot', 30, 3),
--    ('Genry', 'Ford', 43, 4);

-- insert data into brand table
INSERT INTO brand(name)
VALUES
    ('Audi'),
    ('BMW'),
    ('Toyota'),
    ('Volkswagen'),
    ('Volvo');

-- insert data into model table
INSERT INTO model(name, brande_id)
VALUES
    ('320', 2),
    ('350', 2),
    ('A6', 1),
    ('A8', 1),
    ('C70', 5),
    ('C90', 5),
    ('Camry', 3),
    ('Corola', 3),
    ('V50', 3),
    ('Q5', 1),
    ('Q3', 1),
    ('XC90', 5);

-- insert data into color table
INSERT INTO color(name)
VALUES
    ('Balck'),
    ('Blue'),
    ('Brown'),
    ('Burgundy'),
    ('Cyan'),
    ('Green'),
    ('Grey'),
    ('Pink'),
    ('Purple'),
    ('Red'),
    ('White');

-- insert data into condition table
INSERT INTO condition(name)
VALUES
    ('Hail Damage'),
    ('Low Damage'),
    ('Normal Wear Damage'),
    ('Minor Dent/Scratches Damage');

-- insert data into engine table
INSERT INTO engine(name)
VALUES
    ('1.2L 3'),
    ('1.2L 4'),
    ('1.3L 3'),
    ('1.4L 4'),
    ('1.5L 4'),
    ('1.6L 4'),
    ('1.7L 4'),
    ('1.8L 4'),
    ('2.0L 4'),
    ('2.2L 4'),
    ('2.3L 4'),
    ('2.4L 4'),
    ('2.5L 4'),
    ('2.5L 5'),
    ('2.5L 6'),
    ('2.7L 4'),
    ('2.7L 6'),
    ('2.8L 4');

-- insert data into fuel table
INSERT INTO fuel(name)
VALUES
    ('Gas'),
    ('Electric'),
    ('Diesel');

-- insert data into vehicle table
INSERT INTO vehicle(name)
VALUES
    ('Automobiles'),
    ('Box trucks'),
    ('RVs'),
    ('SUVs'),
    ('Trailers');

-- insert data into lots table
INSERT INTO lot (
 created_at,
 updated_at,
    status,
    name,
    description,
    year,
    odometer,
    color_id,
    condition_id,
    engine_id,
    fuel_id,
    owner_id,
    model_id,
    vehicle_id,
    is_active
   )
VALUES
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0001', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 1, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0002', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 1, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0003', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 1, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0004', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 1, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0005', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 1, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0006', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 2, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0007', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 2, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0008', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 2, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0009', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 2, 1, 1, 1),
    ('2023-12-23 12:30:26.729465','2023-12-23 12:30:26.729465','draft','Lot #0010', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquam', 2023, 198850, 1, 1, 1, 1, 2, 1, 1, 1);

-- insert data into lot photo table
INSERT INTO photo(url, lot_id)
VALUES
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1123/29d63893e9d145c29c8353971b9af81d_thb.jpg', 1),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/707f2a9003194341bcde31ae6b36cc27_thb.jpg', 1),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 1),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 3),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 4),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 5),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 6),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 7),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/98619b3025ad4f829c98554a870d3a61_thb.jpg', 8),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/707f2a9003194341bcde31ae6b36cc27_thb.jpg', 9),
    ('https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/1223/707f2a9003194341bcde31ae6b36cc27_thb.jpg', 10);


INSERT INTO auction (status, start_date, end_date, lot_id, created_at, updated_at)
VALUES
  ('OPEN', '2023-12-28', '2023-12-28', 2, '2023-12-28 11:02:34.669280', '2023-12-28 11:02:34.669280'),
  ('PENDING', '2023-12-28', '2023-12-28', 10, '2023-12-28 11:02:34.669280', '2023-12-28 11:02:34.669280'),
  ('CLOSED', '2023-12-28', '2023-12-28', 1, '2023-12-28 11:02:34.669280', '2023-12-28 11:02:34.669280');



INSERT INTO bid_bid(created_at,	updated_at,	bet,	auction_id,	user_id )
VALUES
(	'2023-12-28 11:02:34.669280',	'2023-12-28 11:02:34.669280',	50,	1,	1),
(	'2023-12-28 11:15:30.015325',	'2023-12-28 11:15:30.015325',	60,	1,	2),
(	'2023-12-28 11:15:45.974092',	'2023-12-28 11:15:45.974092',	70,	1,	3),
(	'2023-12-28 11:16:09.043886',	'2023-12-28 11:16:09.043886',	90,	1,	1);
