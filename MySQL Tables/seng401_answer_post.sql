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
-- Table structure for table `answer_post`
--

DROP TABLE IF EXISTS `answer_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer_post` (
  `AID` int NOT NULL AUTO_INCREMENT,
  `QID` int NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Body` longtext NOT NULL,
  `Timestamp` datetime NOT NULL,
  `Approvals` int DEFAULT NULL,
  `Disapprovals` int DEFAULT NULL,
  `Profession` text NOT NULL,
  `ProfessionCategory` text NOT NULL,
  PRIMARY KEY (`AID`),
  KEY `QID` (`QID`),
  KEY `Username` (`Username`),
  CONSTRAINT `answer_post_ibfk_1` FOREIGN KEY (`QID`) REFERENCES `question_post` (`QuestionPostID`),
  CONSTRAINT `answer_post_ibfk_2` FOREIGN KEY (`Username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer_post`
--

LOCK TABLES `answer_post` WRITE;
/*!40000 ALTER TABLE `answer_post` DISABLE KEYS */;
INSERT INTO `answer_post` VALUES (3,1,'test1','Test response...','2022-03-20 01:04:03',NULL,NULL,'Software','Java'),(4,1,'test1','Test response...','2022-03-20 01:04:03',NULL,NULL,'Software','Java'),(5,1,'test1','Test response...','2022-03-20 01:04:03',NULL,NULL,'Software','Java');
/*!40000 ALTER TABLE `answer_post` ENABLE KEYS */;
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
