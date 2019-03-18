CREATE TABLE Person(
  SSN INTEGER,
  FirstName TEXT,
  LastName TEXT,
  Address TEXT, --oder Straße, Hausnummer
  PostCode INTEGER,
  Location TEXT,
  PRIMARY KEY (SSN)
);

CREATE TABLE has_phoneNumber(
  SSN INTEGER,
  PhoneNumber INTEGER,
  PRIMARY KEY (SSN, PhoneNumber),
  FOREIGN KEY (SSN) REFERENCES Person (SSN)
);

CREATE TABLE Staff_has_bank_account(
  SSN INTEGER NOT NULL,
  StaffID INTEGER,
  AccountNumber INTEGER NOT NULL,
  BankCode INTEGER NOT NULL,
  Balance REAL,
  BankName TEXT,
  PRIMARY KEY (StaffID, SSN),
  FOREIGN KEY (SSN) REFERENCES Person(SSN)
);

CREATE TABLE Passenger(
  SSN INTEGER NOT NULL,
  PassengerID INTEGER,
  PRIMARY KEY (PassengerID, SSN),
  FOREIGN KEY (SSN) REFERENCES Person(SSN)
);

CREATE TABLE Pilot(
  StaffID INTEGER NOT NULL,
  PilotLicenceNumber INTEGER,
  FlightHours REAL,
  PRIMARY KEY (PilotLicenceNumber, StaffID),
  FOREIGN KEY (StaffID) REFERENCES Staff_has_bank_account(StaffID)
);

CREATE TABLE Producer(
  ProducerName TEXT,
  PRIMARY KEY (ProducerName)
);

CREATE TABLE PlaneType_made_by(
  TypeNumber INTEGER,
  Seats INTEGER,
  FlightAttendantNumber INTEGER,
  TextualTypeDescription TEXT,
  ProducerName TEXT NOT NULL,
  PRIMARY KEY (TypeNumber),
  FOREIGN KEY (ProducerName) REFERENCES Producer(ProducerName)
);

CREATE TABLE Engineer_services(
  StaffID INTEGER NOT NULL,
  LicenceNumber INTEGER,
  Education TEXT,
  TypeNumber INTEGER,
  PRIMARY KEY (LicenceNumber, StaffID),
  FOREIGN KEY (StaffID) REFERENCES Staff_has_bank_account(StaffID),
  FOREIGN KEY (TypeNumber) REFERENCES PlaneType_made_by(TypeNumber)
);

CREATE TABLE Plane_has_BlackBox_borrowed_by(
  TypeNumber INTEGER NOT NULL,
  InventoryNumber INTEGER,
  FlightHours REAL,
  ProductionYear INTEGER,
  BlackBoxCode INTEGER,
  StaffID INTEGER,
  PRIMARY KEY (InventoryNumber, BlackBoxCode),
  FOREIGN KEY (TypeNumber) REFERENCES PlaneType_made_by(TypeNumber),
  FOREIGN KEY (StaffID) REFERENCES Staff_has_bank_account(StaffID)
);

CREATE TABLE Flight(
  FlightNumber TEXT,
  DepartureAirport TEXT,
  TargetAirport TEXT,
  DepartureTime time,
  ArrivalTime time,
  Date date,
  Price REAL,
  PRIMARY KEY (FlightNumber, Date)
);

CREATE TABLE books(
  PassengerID INTEGER NOT NULL,
  FlightNumber TEXT NOT NULL,
  Date date NOT NULL,
  BookingDate date,
  Class INTEGER,
  BookingNumber INTEGER UNIQUE NOT NULL, --Autoincrement?
  MailAddress TEXT,
  PRIMARY KEY (FlightNumber, Date, PassengerID),
  FOREIGN KEY (PassengerID) REFERENCES Passenger(PassengerID),
  FOREIGN KEY (FlightNumber, Date) REFERENCES Flight(FlightNumber, Date)
);

CREATE TABLE waits_for(
  beforeFlightNumber TEXT,
  afterFlightNumber TEXT,
  beforeDate date,
  afterDate date,
  PRIMARY KEY (beforeFlightNumber, beforeDate, afterFlightNumber, afterDate),
  FOREIGN KEY (beforeFlightNumber, beforeDate) REFERENCES Flight(FlightNumber, Date),
  FOREIGN KEY (afterFlightNumber, afterDate) REFERENCES Flight(FlightNumber, Date)
);

CREATE TABLE flies_with(
  PilotLicenceNumber INTEGER,
  FlightNumber TEXT,
  Date date,
  InventoryNumber INTEGER,
  PRIMARY KEY (PilotLicenceNumber, FlightNumber, Date, InventoryNumber),
  FOREIGN KEY (PilotLicenceNumber) REFERENCES Pilot(PilotLicenceNumber),
  FOREIGN KEY (FlightNumber, Date) REFERENCES Flight(FlightNumber, Date),
  FOREIGN KEY (InventoryNumber) REFERENCES Plane_has_BlackBox_borrowed_by(InventoryNumber)
);
