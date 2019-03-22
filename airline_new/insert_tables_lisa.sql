-- Person
INSERT INTO Person
VALUES
       (0, 'Test', 'Test', 'Test', 0000, 'Test'),
       (1, 'Sonja', 'Kranz', 'Fischgasse 7', 1100, 'Wien'),
       (2, 'Thomas', 'Pflanze', 'Steingasse 26', 1020, 'Wien'),
       (3, 'Laura', 'Stern', 'Sterngasse 1', 1010, 'Wien'),
       (4, 'Susanne', 'Kind', 'Baumgasse 15', 1070, 'Wien');

-- has_phoneNumber
INSERT INTO has_phoneNumber
VALUES (0, '+0000'),
       (1, '+436604728442'),
       (2, '+438390245776'),
       (3, '+433224553642'),
       (4, '+478885994832');

-- Staff_has_bank_account
INSERT INTO Staff_has_bank_account
VALUES (1, 1, 2220444055506, 11130, 1500.0, 'Bank Austria'),
       (2, 2, 5554999283778, 12122, 2000.0, 'Erste Bank'),
       (3, 3, 8449393984557, 11130,  3000.0, 'Bank Austria'),
       (4, 4, 8866699332111, 11130, 1700.0, 'Bank Austria');

--Passenger
INSERT INTO Passenger
VALUES (0, 0);

--Pilot
INSERT INTO Pilot
VALUES (1, 111, 350),
       (2, 222, 500);

--Producer
INSERT INTO Producer
VALUES ('Boeing'),
       ('Airbus');

--PlaneType_made_by
INSERT INTO PlaneType_made_by
VALUES (1212, 350, 5, 'Boeing 747', 'Boeing'),
       (2323, 200, 5, 'Airbus A320', 'Airbus');

--Engineer_services
INSERT INTO Engineer_services
VALUES (3, 3333, 'Engineer', 1212),
       (4, 4444, 'Engineer', 2323);

--Plane_has_BlackBox_borrowed_by
INSERT INTO Plane_has_BlackBox_borrowed_by
VALUES (1212, 1111111, 10300.0, 2009, 23654, 1),
       (2323, 2222222, 10000.0, 2006, 89654, 3);

--Flight
INSERT INTO Flight
VALUES ('GA1234', 'VIE', 'MAD', '09:32', '11:30', '2019-04-10', 125, 1212, 70),
       ('GA2563', 'MAD', 'BER', '12:00', '15:00', '2019-04-10', 80, 2323, 90),
       ('GA9876', 'VIE', 'MAD', '18:00', '21:30', '2019-04-10', 125, 2323, 35),
       ('GA1234', 'VIE', 'MAD', '09:32', '11:30', '2019-05-10', 125, 1212, 90),
       ('GA9876', 'VIE', 'MAD', '12:30', '14:30', '2019-04-12', 125, 2323, 60),
       ('GA9999', 'VIE', 'BER', '15:30', '17:30', '2019-04-15', 160, 1212, 30),
       ('GA9999', 'VIE', 'BER', '16:30', '18:30', '2019-04-16', 170, 1212, 35),
       ('GA2345', 'MAD', 'VIE', '09:32', '11:30', '2019-04-10', 125, 1212, 70),
       ('GA8765', 'MAD', 'VIE', '18:00', '21:30', '2019-04-10', 125, 2323, 35),
       ('GA2345', 'MAD', 'VIE', '09:32', '11:30', '2019-05-10', 125, 1212, 90),
       ('GA8765', 'MAD', 'VIE', '12:30', '14:30', '2019-04-12', 125, 2323, 60),
       ('GA1111', 'BER', 'VIE', '15:30', '17:30', '2019-04-15', 160, 1212, 30),
       ('GA1111', 'BER', 'VIE', '16:30', '18:30', '2019-04-16', 170, 1212, 35);

--books
INSERT INTO books
VALUES (0, 'GA0000', 2000-01-01, 2000-01-01, 'E', 0, 'mail@mail.com');

--waits_for
INSERT INTO waits_for
VALUES ('GA1234', 'GA2563', '2019-04-10', '2019-04-10');

--flies_with
INSERT INTO flies_with
VALUES (1111, 'GA1234', '2019-04-10', 1111111),
       (2222, 'GA1111', '2019-04-15', 2222222);

