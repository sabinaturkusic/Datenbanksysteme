# Datenbanksysteme
Projekt - Teil 4

@ Server: 
Starten des Servers: 
1. git pull origin master
2. python3 flugbuchung_server.py
3. http://localhost:5000/signUp (bzw http://localhost:5000/<Name des HTML in camelCase>) im Browser eingeben
4. Jetzt wird eine ziemlich basic HTML Seite angezeigt

@ Datenbank: 
Jeder braucht eine lokale Kopie der gesamten Datenbank, da wir ja unseren Server nur lokal hosten. Daher bitte: 
1. SQlite installieren (siehe SQLite_installation.txt)
2. Die Datenbank NICHT auf Git erstellen, sondern lokal
  $ sqlite3 <databasename>.db
3. Die Tables werden durch das einlesen der create_tables.sql Datei erstellt 
  sqlite> .read create_tables.sql
  sqlite> .tables #überprüfen welche tables in der Datenbank sind

