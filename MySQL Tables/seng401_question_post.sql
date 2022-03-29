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
  `Tags` text,
  PRIMARY KEY (`QuestionPostID`),
  KEY `Username` (`Username`),
  CONSTRAINT `question_post_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question_post`
--

LOCK TABLES `question_post` WRITE;
/*!40000 ALTER TABLE `question_post` DISABLE KEYS */;
INSERT INTO `question_post` VALUES (1,'dmah','Another question','How to start?','2022-03-19 17:11:15',NULL,NULL,'6',NULL,NULL),(19,'dmah','How to read arrays?','I\'m getting errors when trying to do \"System.out.println(array);\"','2022-03-19 17:34:01',NULL,NULL,'Software',NULL,NULL),(20,'dmah','Sample q','OH MY GOH I CANNOT','2022-03-19 17:35:34',NULL,NULL,'Software',NULL,NULL),(21,'dmah','Title','Body','2022-03-19 17:36:29',NULL,NULL,'Chemical','maba',NULL),(22,'test1','WOWIE','How do?','2022-03-22 16:49:35',NULL,NULL,'Chemical','Mass Balance',NULL),(23,'test123','Best shape for structural integrity and strength','What is the best shape to hold up a bridge?','2022-03-28 17:09:46',NULL,NULL,'Engineer','Civil','Bridges'),(24,'test123','Best shape for structural integrity and strength','What is the best shape to hold up a bridge?','2022-03-28 17:10:03',NULL,NULL,'Engineer','Civil','Bridges'),(25,'dmah','1','1','2022-03-28 17:41:09',NULL,NULL,'Engineer','Chemical','[]'),(26,'dmah','Sample Title','Sample Body','2022-03-29 00:03:44',NULL,NULL,'Engineer','Software','[]'),(27,'dmah','Sample Title','Sample Body','2022-03-29 00:04:06',NULL,NULL,'Engineer','Software','[]'),(28,'dmah','Sample Title','Sample Body','2022-03-29 00:04:19',NULL,NULL,'Engineer','Software','[]'),(29,'dmah','Sample Title','Sample Body','2022-03-29 00:09:56',NULL,NULL,'Engineer','Software','[]'),(30,'dmah','Sample Title','Sample Body','2022-03-29 00:10:18',NULL,NULL,'Engineer','Software','[]'),(31,'dmah','Sample Title','Sample Body','2022-03-29 12:09:41',NULL,NULL,'Engineer','Software','[]'),(44,'dmah','Sample Title','Sample Body','2022-03-29 12:42:33',NULL,NULL,'Engineer','Software','[]'),(45,'dmah','Sample Title','Sample Body','2022-03-29 12:44:12',NULL,NULL,'Engineer','Software','[]'),(46,'dmah','Sample Title','Sample Body','2022-03-29 12:45:19',NULL,NULL,'Engineer','Software','[]'),(47,'dmah','Sample Title','Sample Body','2022-03-29 12:45:57',NULL,NULL,'Engineer','Software','[]'),(48,'testUser','Sample Title','Sample Body','2022-03-29 12:48:31',NULL,NULL,'Engineer','Software','[]'),(49,'testUser','Sample Title','Sample Body','2022-03-29 13:47:29',NULL,NULL,'Engineer','Software','[]'),(50,'dmah','Sample Title','Sample Body','2022-03-29 13:48:58',NULL,NULL,'Engineer','Software','[]'),(51,'dmah','Sample Title','Sample Body','2022-03-29 13:49:16',NULL,NULL,'Engineer','Software','[]'),(52,'dmah','Sample Title','Sample Body','2022-03-29 13:49:51',NULL,NULL,'Engineer','Software','[]'),(53,'dmah','Sample Title','Sample Body','2022-03-29 13:50:01',NULL,NULL,'Engineer','Software','[]'),(54,'dmah','Sample Title','Sample Body','2022-03-29 13:50:11',NULL,NULL,'Engineer','Software','[]'),(55,'dmah','Sample Title','Sample Body','2022-03-29 13:50:22',NULL,NULL,'Engineer','Software','[]');
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

-- Dump completed on 2022-03-29 13:52:33
