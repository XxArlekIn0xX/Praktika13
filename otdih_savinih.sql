# SQL Manager Lite for MySQL 5.5.0.45357
# ---------------------------------------
# Host     : localhost
# Port     : 3306
# Database : otdih_savinih


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES cp1251 */;

SET FOREIGN_KEY_CHECKS=0;

CREATE DATABASE `otdih_savinih`
    CHARACTER SET 'cp1251'
    COLLATE 'cp1251_general_ci';

USE `otdih_savinih`;

#
# Структура для таблицы `klienti`: 
#

CREATE TABLE `klienti` (
  `KodKlienta` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `Familia` VARCHAR(30) COLLATE cp1251_general_ci NOT NULL,
  `Name` VARCHAR(20) COLLATE cp1251_general_ci NOT NULL,
  `Otchestvo` VARCHAR(20) COLLATE cp1251_general_ci DEFAULT NULL,
  `Adres` VARCHAR(80) COLLATE cp1251_general_ci NOT NULL,
  `Gorod` VARCHAR(20) COLLATE cp1251_general_ci NOT NULL,
  PRIMARY KEY (`KodKlienta`) USING BTREE
) ENGINE=InnoDB
AUTO_INCREMENT=10016 CHARACTER SET 'cp1251' COLLATE 'cp1251_general_ci'
;

#
# Структура для таблицы `turistputevki`: 
#

CREATE TABLE `turistputevki` (
  `idTuristPutevki` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `Strana` VARCHAR(20) COLLATE cp1251_general_ci NOT NULL,
  `DataFirstDayOtdiha` DATE NOT NULL,
  `DataLastDayOtdiha` DATE NOT NULL,
  `KolichestvoKomnat` INTEGER(10) UNSIGNED NOT NULL,
  `Pitanie` TINYINT(1) UNSIGNED NOT NULL,
  `KulturnayaProgramma` TINYINT(1) UNSIGNED NOT NULL,
  `StoimostZaSutki` INTEGER(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`idTuristPutevki`) USING BTREE
) ENGINE=InnoDB
AUTO_INCREMENT=7385 CHARACTER SET 'cp1251' COLLATE 'cp1251_general_ci'
;

#
# Структура для таблицы `zakaz`: 
#

CREATE TABLE `zakaz` (
  `idZakaz` INTEGER(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `TuristPutevki_idTuristPutevki` INTEGER(10) UNSIGNED NOT NULL,
  `Klienti_KodKlienta` INTEGER(10) UNSIGNED NOT NULL,
  `KolichestvoLudey` INTEGER(10) UNSIGNED NOT NULL,
  `DataPribitia` DATE NOT NULL,
  `Skidka` INTEGER(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`idZakaz`, `TuristPutevki_idTuristPutevki`, `Klienti_KodKlienta`) USING BTREE,
  KEY `Zakaz_FKIndex1` (`TuristPutevki_idTuristPutevki`) USING BTREE,
  KEY `Zakaz_FKIndex2` (`Klienti_KodKlienta`) USING BTREE
) ENGINE=InnoDB
AUTO_INCREMENT=116 CHARACTER SET 'cp1251' COLLATE 'cp1251_general_ci'
;

#
# Data for the `klienti` table  (LIMIT 0,500)
#

INSERT INTO `klienti` (`KodKlienta`, `Familia`, `Name`, `Otchestvo`, `Adres`, `Gorod`) VALUES
  (10001,'Морозова','Юлия','Петровна','Ул. Маяковского д. 15','Москва'),
  (10002,'Иванов','Алексей','Сергеевич','Пр. Ленина д. 45 кв. 12','Санкт-Петербург'),
  (10003,'Петрова','Мария','Игоревна','Ул. Пушкина д. 23','Новосибирск'),
  (10004,'Сидоров','Дмитрий','Александрович','Бульвар Мира д. 67','Екатеринбург'),
  (10005,'Кузнецова','Анна','Владимировна','Ул. Гагарина д. 8 кв. 34','Казань'),
  (10006,'Попов','Артем','Олегович','Пр. Победы д. 12','Нижний Новгород'),
  (10007,'Васильева','Елена','Дмитриевна','Ул. Советская д. 56','Челябинск'),
  (10008,'Смирнов','Максим','Викторович','Аллея Космонавтов д. 3','Самара'),
  (10009,'Федорова','Ольга','Алексеевна','Ул. Лермонтова д. 78','Омск'),
  (10010,'Волков','Сергей','Павлович','Пр. Октября д. 25 кв. 9','Ростов-на-Дону'),
  (10011,'Савиных','Алексей','Александрович','Ул. Вознесенского д. 15','Троицк'),
  (10012,'Алексеева','Татьяна','Сергеевна','Ул. Чехова д. 14','Уфа'),
  (10013,'Лебедев','Андрей','Иванович','Бульвар Строителей д. 41','Красноярск'),
  (10014,'Семенова','Ирина','Петровна','Ул. Горького д. 29 кв. 15','Воронеж'),
  (10015,'Козлов','Павел','Николаевич','Пр. Мира д. 33','Москва');
COMMIT;

#
# Data for the `turistputevki` table  (LIMIT 0,500)
#

INSERT INTO `turistputevki` (`idTuristPutevki`, `Strana`, `DataFirstDayOtdiha`, `DataLastDayOtdiha`, `KolichestvoKomnat`, `Pitanie`, `KulturnayaProgramma`, `StoimostZaSutki`) VALUES
  (1001,'Испания','2024-08-05','2024-08-19',16,1,1,4200),
  (1002,'Россия','2025-02-08','2025-03-08',14,1,1,3000),
  (1003,'ОАЭ','2025-01-05','2025-01-19',8,1,0,6800),
  (1004,'США','2025-01-04','2025-03-04',13,1,1,2100),
  (1005,'Греция','2024-09-01','2024-09-14',7,0,1,3100),
  (1006,'Россия','2025-12-08','2025-12-25',15,0,1,1009),
  (1007,'Тайланд','2024-10-15','2024-10-29',6,1,0,3800),
  (1008,'Турция','2024-06-01','2024-06-15',14,1,1,3500),
  (1009,'Хорватия','2025-04-01','2025-04-15',8,1,1,4100),
  (1010,'Египет','2024-07-10','2024-07-24',5,1,0,2800),
  (1011,'Франция','2024-12-20','2024-12-31',6,0,1,5200),
  (1012,'США','2025-02-01','2025-04-01',12,1,1,2000),
  (1013,'Кипр','2025-02-14','2025-02-28',12,1,1,3900),
  (1014,'Италия','2024-11-01','2024-11-10',9,1,1,4500),
  (1015,'Болгария','2025-03-10','2025-03-20',10,0,0,2200);
COMMIT;

#
# Data for the `zakaz` table  (LIMIT 0,500)
#

INSERT INTO `zakaz` (`idZakaz`, `TuristPutevki_idTuristPutevki`, `Klienti_KodKlienta`, `KolichestvoLudey`, `DataPribitia`, `Skidka`) VALUES
  (101,1015,10001,3,'2025-03-09',15),
  (102,1014,10002,4,'2024-10-31',5),
  (103,1013,10003,3,'2025-02-13',4),
  (104,1012,10004,6,'2025-01-31',10),
  (105,1011,10005,5,'2024-12-19',10),
  (106,1010,10006,7,'2024-07-09',7),
  (107,1009,10007,2,'2025-03-31',10),
  (108,1008,10008,4,'2024-05-31',10),
  (109,1007,10009,1,'2024-10-14',20),
  (110,1006,10010,5,'2025-12-07',5),
  (111,1005,10011,3,'2024-08-31',7),
  (112,1004,10012,2,'2025-01-03',2),
  (113,1003,10013,6,'2025-01-04',6),
  (114,1002,10014,4,'2025-02-07',6),
  (115,1001,10015,9,'2024-08-04',10);
COMMIT;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;