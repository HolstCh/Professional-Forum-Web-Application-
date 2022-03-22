-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: seng401
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `question_post`
--

DROP TABLE IF EXISTS `question_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question_post` (
  `QuestionPostID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Title` text NOT NULL,
  `Body` longtext NOT NULL,
  `Timestamp` datetime NOT NULL,
  `Approvals` int DEFAULT NULL,
  `Disapprovals` int DEFAULT NULL,
  `Profession` text NOT NULL,
  `ProfessionCategory` text,
  PRIMARY KEY (`QuestionPostID`),
  KEY `Username` (`Username`),
  CONSTRAINT `question_post_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_post`
--

LOCK TABLES `question_post` WRITE;
/*!40000 ALTER TABLE `question_post` DISABLE KEYS */;
INSERT INTO `question_post` VALUES (1,'dmah','Another question','How to start?','2022-03-19 17:11:15',NULL,NULL,'6',NULL),(19,'dmah','How to read arrays?','I\'m getting errors when trying to do \"System.out.println(array);\"','2022-03-19 17:34:01',NULL,NULL,'Software',NULL),(20,'dmah','Sample q','OH MY GOH I CANNOT','2022-03-19 17:35:34',NULL,NULL,'Software',NULL),(21,'dmah','Title','Body','2022-03-19 17:36:29',NULL,NULL,'Chemical','maba');
/*!40000 ALTER TABLE `question_post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-21 21:58:50
