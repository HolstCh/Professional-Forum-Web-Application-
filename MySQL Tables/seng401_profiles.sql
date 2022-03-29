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
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profiles` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `middleNames` varchar(255) DEFAULT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `currentCompany` varchar(255) DEFAULT NULL,
  `profession` text NOT NULL,
  `skills` text,
  `description` text,
  `projects` text,
  PRIMARY KEY (`ID`),
  KEY `username` (`username`),
  CONSTRAINT `profiles_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
INSERT INTO `profiles` VALUES (1,'test1','fName','None','lName','email@site.xyz','None','some','None','None','None'),(3,'dmah','Dylan','Connor','Mah','dylan.mah@ucalgary.ca','None','Software','Can code in Java, C/C++, HTML/CSS, Python, PHP','20 year old male software engineer student at the University of Calgary. Canadian citizen of Chinese descent.','None'),(10,'test123','Joe','Xander','Smith','jxsmith@email.xyz','Husky','Project Manager','Leadership experience, quick learner','30 years of work experience','Gas stations around town'),(17,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(18,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(19,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(20,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(21,'testUser','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(26,'testUser','chad','daniel','holst','fake@email.com','DGC','Engineer','machinery design','hands on','designing engine'),(27,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(28,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(29,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(30,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(31,'chad','chad','daniel','holst','editMyFakeEmail@email.com','DGC','Engineer','circuit building','hands on','designing electrical grid'),(32,'chad','chad','daniel','holst','fake@email.com','DGC','Engineer','machinery design','hands on','designing engine');
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
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
