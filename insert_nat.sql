INSERT INTO Person (SSN, FirstName, LastName, Address, PostCode, Location)
VALUES (3412, 'Sonja', 'Kranz', 'Fischgasse 7', 1100, 'Wien');

INSERT INTO Person (SSN, FirstName, LastName, Address, PostCode, Location)
VALUES (2781, 'Thomas', 'Pflanze', 'Steingasse 26', 1020, 'Wien');

INSERT INTO Person (SSN, FirstName, LastName, Address, PostCode, Location)
VALUES (1987, 'Laura', 'Stern', 'Sterngasse 1', 1010, 'Wien');

INSERT INTO Person (SSN, FirstName, LastName, Address, PostCode, Location)
VALUES (7653, 'Susanne', 'Kind', 'Baumgasse 15', 1070, 'Wien');

INSERT INTO has_phoneNumber (SSN, PhoneNumber)
VALUES (3412, '+436604728442');

INSERT INTO has_phoneNumber (SSN, PhoneNumber)
VALUES (2781, '+438390245776');

INSERT INTO has_phoneNumber (SSN, PhoneNumber)
VALUES (1987, '+433224553642');

INSERT INTO has_phoneNumber (SSN, PhoneNumber)
VALUES (7653, '+478885994832');

INSERT INTO Staff_has_bank_account (SSN, StaffID, AccountNumber, BankCode, Balance, BankName)
VALUES (3412, 1, 2220444055506, 11130, 1500, 'Bank Austria');

INSERT INTO Staff_has_bank_account (SSN, StaffID, AccountNumber, BankCode, Balance, BankName)
VALUES (2781, 2, 5554999283778, 12122, 2000, 'Erste Bank');

INSERT INTO Staff_has_bank_account (SSN, StaffID, AccountNumber, BankCode, Balance, BankName)
VALUES (1987, 3, 8449393984557, 11130, 3000, 'Bank Austria');

INSERT INTO Staff_has_bank_account (SSN, StaffID, AccountNumber, BankCode, Balance, BankName)
VALUES (7653, 4, 8866699332111, 11130, 1700, 'Bank Austria');

INSERT INTO Pilot (StaffID, PilotLicenceNumber, FlightHours)
VALUES (1, 1111, 350);

INSERT INTO Pilot (StaffID, PilotLicenceNumber, FlightHours)
VALUES (2, 2222, 500);

INSERT INTO Producer (ProducerName)
VALUES ('Steiner GmBh');

INSERT INTO PlaneType_made_by (TypeNumber, Seats, FlightAttendantNumber, TextualTypeDescription, ProducerName)
VALUES (1212, 120, 5, 'Boeing 747', 'Steiner GmBh');

INSERT INTO PlaneType_made_by (TypeNumber, Seats, FlightAttendantNumber, TextualTypeDescription, ProducerName)
VALUES (2323, 120, 5, 'Boeing 747', 'Steiner GmBh');

INSERT INTO Engineer_services (StaffID, LicenceNumber, Education, TypeNumber)
VALUES (3, 3333, 'Engineer', 1212);

INSERT INTO Engineer_services (StaffID, LicenceNumber, Education, TypeNumber)
VALUES (4, 4444, 'Engineer', 2323);

INSERT INTO Plane_has_BlackBox_borrowed_by (TypeNumber, InventoryNumber, FlightHours, ProductionYear, BackBoxCode)
VALUES (1212, 1111111, 10300, 2009, 787878);

INSERT INTO Plane_has_BlackBox_borrowed_by (TypeNumber, InventoryNumber, FlightHours, ProductionYear, BackBoxCode)
VALUES (2323, 2222222, 10000, 2006, 454545);

INSERT INTO Flight (FlightNumber, DepartureAirport, TargetAirport, DepartureTime, ArrivalTime, Date, Price)
VALUES ('GA88888', 'VIE', 'MAD', '09:32:00', '11:30:00', '2019-04-10', 125);

INSERT INTO Flight (FlightNumber, DepartureAirport, TargetAirport, DepartureTime, ArrivalTime, Date, Price)
VALUES ('GA88888', 'MAD', 'VIE', '10:30:00', '12:30:00', '2019-04-11', 150);

INSERT INTO Flight (FlightNumber, DepartureAirport, TargetAirport, DepartureTime, ArrivalTime, Date, Price)
VALUES ('GA99999', 'VIE', 'BER', '15:30:00', '17:30:00', '2019-04-15', 160 );

INSERT INTO Flight (FlightNumber, DepartureAirport, TargetAirport, DepartureTime, ArrivalTime, Date, Price)
VALUES ('GA99999', 'BER', 'VIE', '16:30:00', '18:30:00', '2019-04-16', 170);

INSERT INTO flies_with (PilotLicenceNumber, FlightNumber, Date, InventoryNumber)
VALUES (1111, 88888, '2019-04-10', 1111111);

INSERT INTO flies_with (PilotLicenceNumber, FlightNumber, Date, InventoryNumber)
VALUES (2222, 99999, '2019-04-15', 2222222);




