/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 8.0.26 : Database - carpooling
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`carpooling` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `carpooling`;

/*Table structure for table `driver` */

DROP TABLE IF EXISTS `driver`;

CREATE TABLE `driver` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(12) DEFAULT NULL,
  `tel` varchar(32) DEFAULT NULL,
  `cartype` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `limitedload` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `driver` */

insert  into `driver`(`id`,`name`,`tel`,`cartype`,`limitedload`) values 
(1,'李师傅','19949992999','七座SUV',6),
(2,'王师傅','18882888888','五座轿车',4),
(3,'谢师傅','12223122222','七座面包车',6),
(5,'郑师傅','18898889888','梅赛德斯总统款',2),
(6,'于师傅','19929993999','特斯拉model3',4);

/*Table structure for table `orderdetails` */

DROP TABLE IF EXISTS `orderdetails`;

CREATE TABLE `orderdetails` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `orderid` int DEFAULT NULL,
  `userid` varchar(48) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `orderdetails` */

insert  into `orderdetails`(`id`,`orderid`,`userid`) values 
(6,1,'a'),
(7,2,'x');

/*Table structure for table `orderlist` */

DROP TABLE IF EXISTS `orderlist`;

CREATE TABLE `orderlist` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `driverid` int DEFAULT NULL,
  `limited` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `current` int DEFAULT '0',
  `routeid` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `orderlist` */

insert  into `orderlist`(`id`,`driverid`,`limited`,`price`,`current`,`routeid`) values 
(1,1,6,20,3,1),
(6,2,4,20,0,2);

/*Table structure for table `route` */

DROP TABLE IF EXISTS `route`;

CREATE TABLE `route` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `start` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `end` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `length` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `route` */

insert  into `route`(`id`,`start`,`end`,`length`) values 
(1,'西工大长安校区','西工大友谊校区',30),
(2,'西工大长安校区','韦曲南',28),
(3,'西工大长安校区','国际医学中心',15),
(23,'西工大大东门','西电正门',15),
(24,'西工大','西电',10);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `password` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `type` varchar(16) DEFAULT NULL,
  `tel` varchar(24) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`password`,`type`,`tel`) values 
(13,'q','7694f4a66316e53c8cdd9d9954bd611d','manager','12232223222'),
(14,'a','0cc175b9c0f1b6a831c399e269772661','user','12232292999'),
(15,'z','fbade9e36a3f36d3d676c1b808451dd7','driver','13332292999'),
(16,'w','f1290186a5d0b1ceab27f4e77c0c5d68','manager','19993999299'),
(17,'e','e1671797c52e15f763380b45e841ec32','manager','18828883888'),
(18,'x','9dd4e461268c8034f5c8564e155c67a6','user','122232223222');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
