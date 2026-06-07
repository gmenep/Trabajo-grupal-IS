-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: labtrack
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `assets`
--

DROP TABLE IF EXISTS `assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assets` (
  `asset_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `asset_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `risk_level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`asset_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assets`
--

LOCK TABLES `assets` WRITE;
/*!40000 ALTER TABLE `assets` DISABLE KEYS */;
INSERT INTO `assets` VALUES (1,'Etanol 70','material','Medio'),(2,'Buffer PBS','material','Bajo'),(3,'Acido clorhidrico','material','Alto'),(4,'Centrifuga C-200','machine','Medio'),(5,'Microscopio M-10','machine','Bajo'),(6,'Autoclave A-5','machine','Alto'),(7,'PBC','material','Bajo'),(8,'Bartola','machine',''),(9,'Bartolo','machine','Bajo'),(10,'Bartolomeo','machine','Alto'),(11,'adsa','machine','adsa'),(12,'wdad','machine','dwadw'),(14,'var','machine','Bajo');
/*!40000 ALTER TABLE `assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `belongsto`
--

DROP TABLE IF EXISTS `belongsto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `belongsto` (
  `project_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`project_id`,`user_id`),
  KEY `FK_BelongsTo_Users` (`user_id`),
  CONSTRAINT `FK_BelongsTo_Projects` FOREIGN KEY (`project_id`) REFERENCES `projects` (`project_id`),
  CONSTRAINT `FK_BelongsTo_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `belongsto`
--

LOCK TABLES `belongsto` WRITE;
/*!40000 ALTER TABLE `belongsto` DISABLE KEYS */;
INSERT INTO `belongsto` VALUES (1,14),(2,14),(1,15),(2,15),(1,16),(2,16);
/*!40000 ALTER TABLE `belongsto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  `event_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reference_id` int DEFAULT NULL,
  `raw_data` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `FK_Logs_Users` (`user_id`),
  CONSTRAINT `FK_Logs_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=329 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs`
--

LOCK TABLES `logs` WRITE;
/*!40000 ALTER TABLE `logs` DISABLE KEYS */;
INSERT INTO `logs` VALUES (1,'2026-06-07 03:37:44','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(2,'2026-06-07 03:37:44','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(3,'2026-06-07 03:37:44','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(4,'2026-06-07 03:37:44','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(5,'2026-06-07 03:38:03','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(6,'2026-06-07 03:38:05','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(7,'2026-06-07 03:38:06','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(8,'2026-06-07 03:38:08','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(9,'2026-06-07 03:41:30','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(10,'2026-06-07 03:41:30','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(11,'2026-06-07 03:41:31','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(12,'2026-06-07 03:41:31','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(13,'2026-06-07 03:42:15','LOGIN_CORRECTO',16,'Inicio de sesion correcto',16),(14,'2026-06-07 03:42:15','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(15,'2026-06-07 03:42:15','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(16,'2026-06-07 03:42:56','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(17,'2026-06-07 03:42:56','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(18,'2026-06-07 03:42:56','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(19,'2026-06-07 03:42:56','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(20,'2026-06-07 04:11:48','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(21,'2026-06-07 04:11:48','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(22,'2026-06-07 04:11:49','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(23,'2026-06-07 04:11:50','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(24,'2026-06-07 04:11:50','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(25,'2026-06-07 04:11:51','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(26,'2026-06-07 04:30:54','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(27,'2026-06-07 04:30:54','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(28,'2026-06-07 04:30:59','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(29,'2026-06-07 04:31:13','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(30,'2026-06-07 04:31:38','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(31,'2026-06-07 04:31:38','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(32,'2026-06-07 04:31:38','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(33,'2026-06-07 04:31:38','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(34,'2026-06-07 04:31:39','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(35,'2026-06-07 04:31:39','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(36,'2026-06-07 04:31:39','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(37,'2026-06-07 04:31:39','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(38,'2026-06-07 04:31:39','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(39,'2026-06-07 04:31:39','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(40,'2026-06-07 04:31:40','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(41,'2026-06-07 04:31:40','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(42,'2026-06-07 04:31:40','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(43,'2026-06-07 04:31:40','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(44,'2026-06-07 04:31:47','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(45,'2026-06-07 04:31:50','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(46,'2026-06-07 04:31:52','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(47,'2026-06-07 04:31:52','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(48,'2026-06-07 04:31:57','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(49,'2026-06-07 04:32:19','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(50,'2026-06-07 04:32:23','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(51,'2026-06-07 04:33:15','ANADIR_MATERIAL',7,'PBC',13),(52,'2026-06-07 04:33:16','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(53,'2026-06-07 04:34:09','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(54,'2026-06-07 04:34:14','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(55,'2026-06-07 04:34:24','ACCION_NO_AUTORIZADA',NULL,'CONSULTAR_PROYECTOS',13),(56,'2026-06-07 04:34:27','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(57,'2026-06-07 04:34:27','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(58,'2026-06-07 04:34:29','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(59,'2026-06-07 04:34:31','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(60,'2026-06-07 04:36:53','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(61,'2026-06-07 04:37:37','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(62,'2026-06-07 04:37:37','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(63,'2026-06-07 04:37:40','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(64,'2026-06-07 04:37:41','CONSULTAR_LOGS',NULL,'Consulta de logs',13),(65,'2026-06-07 04:37:56','LOGIN_CORRECTO',16,'Inicio de sesion correcto',16),(66,'2026-06-07 04:37:56','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(67,'2026-06-07 04:37:58','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(68,'2026-06-07 04:37:59','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(69,'2026-06-07 04:38:00','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(70,'2026-06-07 04:38:01','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(71,'2026-06-07 04:38:01','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(72,'2026-06-07 04:38:14','LOGIN_CORRECTO',16,'Inicio de sesion correcto',16),(73,'2026-06-07 04:38:14','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(74,'2026-06-07 04:38:17','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(75,'2026-06-07 04:38:17','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(76,'2026-06-07 04:38:18','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(77,'2026-06-07 04:38:18','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(78,'2026-06-07 04:38:18','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(79,'2026-06-07 04:38:27','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(80,'2026-06-07 04:38:27','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(81,'2026-06-07 04:38:30','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(82,'2026-06-07 04:38:30','BACKUP',NULL,'mysqldump no disponible',13),(83,'2026-06-07 04:39:46','LOGIN_CORRECTO',18,'Inicio de sesion correcto',18),(84,'2026-06-07 04:39:46','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(85,'2026-06-07 04:40:22','ANADIR_LOTE',7,'PBC-001',18),(86,'2026-06-07 04:40:23','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(87,'2026-06-07 04:41:01','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(88,'2026-06-07 04:41:02','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(89,'2026-06-07 04:41:02','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(90,'2026-06-07 04:41:02','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(91,'2026-06-07 04:41:07','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(92,'2026-06-07 04:41:11','ELIMINAR_LOTE',7,'PBC-001',18),(93,'2026-06-07 04:41:11','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(94,'2026-06-07 04:41:12','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(95,'2026-06-07 04:41:14','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',18),(96,'2026-06-07 04:41:23','LOGIN_CORRECTO',17,'Inicio de sesion correcto',17),(97,'2026-06-07 04:41:23','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(98,'2026-06-07 04:41:25','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(99,'2026-06-07 04:41:30','MODIFICAR_MAQUINA',6,'Autoclave A-5',17),(100,'2026-06-07 04:41:31','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(101,'2026-06-07 04:41:33','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(102,'2026-06-07 04:42:15','ANADIR_MAQUINA',8,'Bartola',17),(103,'2026-06-07 04:42:16','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(104,'2026-06-07 04:42:17','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(105,'2026-06-07 04:42:18','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(106,'2026-06-07 04:42:24','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(107,'2026-06-07 04:42:25','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(108,'2026-06-07 04:42:25','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(109,'2026-06-07 04:42:26','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(110,'2026-06-07 04:42:35','ANADIR_MAQUINA',9,'Bartolo',17),(111,'2026-06-07 04:42:36','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(112,'2026-06-07 04:42:36','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(113,'2026-06-07 04:42:37','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(114,'2026-06-07 04:42:37','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(115,'2026-06-07 04:48:32','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(116,'2026-06-07 04:48:32','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(117,'2026-06-07 04:49:00','ANADIR_LOTE',1,'PBC-001',13),(118,'2026-06-07 04:49:01','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(119,'2026-06-07 04:49:03','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(120,'2026-06-07 04:49:04','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(121,'2026-06-07 04:49:04','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(122,'2026-06-07 04:49:04','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(123,'2026-06-07 04:49:31','ANADIR_LOTE',7,'pbc-001',13),(124,'2026-06-07 04:49:32','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(125,'2026-06-07 04:49:36','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(126,'2026-06-07 04:49:37','BACKUP',NULL,'backups\\labtrack_20260607_044937.sql',13),(127,'2026-06-07 04:52:17','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(128,'2026-06-07 04:52:23','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(129,'2026-06-07 04:52:23','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(130,'2026-06-07 04:52:24','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(131,'2026-06-07 04:52:32','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(132,'2026-06-07 04:54:54','BACKUP',NULL,'backups\\labtrack_20260607_045454.sql',13),(133,'2026-06-07 04:56:54','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(134,'2026-06-07 04:56:54','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(135,'2026-06-07 04:56:56','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(136,'2026-06-07 04:57:02','BACKUP',NULL,'C:\\Users\\GMP9721\\Documents\\GitHub\\Trabajo-grupal-IS\\backups\\labtrack_20260607_045701.sql',13),(137,'2026-06-07 04:57:11','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(138,'2026-06-07 04:57:12','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(139,'2026-06-07 04:57:12','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(140,'2026-06-07 04:57:12','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(141,'2026-06-07 04:57:14','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(142,'2026-06-07 04:57:14','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(143,'2026-06-07 05:00:49','LOGIN_CORRECTO',17,'Inicio de sesion correcto',17),(144,'2026-06-07 05:00:49','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(145,'2026-06-07 05:01:04','ANADIR_MAQUINA',10,'Bartolomeo',17),(146,'2026-06-07 05:01:13','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(147,'2026-06-07 05:01:19','ANADIR_MAQUINA',11,'adsa',17),(148,'2026-06-07 05:01:20','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(149,'2026-06-07 05:01:30','MODIFICAR_MAQUINA',4,'Centrifuga C-200',17),(150,'2026-06-07 05:01:31','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(151,'2026-06-07 05:01:35','MODIFICAR_MAQUINA',4,'Centrifuga C-200',17),(152,'2026-06-07 05:01:35','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(153,'2026-06-07 05:01:38','MODIFICAR_MAQUINA',4,'Centrifuga C-200',17),(154,'2026-06-07 05:01:39','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(155,'2026-06-07 05:01:40','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(156,'2026-06-07 05:01:40','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(157,'2026-06-07 05:01:40','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(158,'2026-06-07 05:01:40','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(159,'2026-06-07 05:01:44','MOVER_MAQUINA',4,'Nuevo almacen 1',17),(160,'2026-06-07 05:01:45','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(161,'2026-06-07 05:01:54','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(162,'2026-06-07 05:01:54','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(163,'2026-06-07 05:01:58','ANADIR_MAQUINA',12,'wdad',17),(164,'2026-06-07 05:01:59','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(165,'2026-06-07 05:02:00','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(166,'2026-06-07 05:02:00','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(167,'2026-06-07 05:02:24','LOGIN_CORRECTO',15,'Inicio de sesion correcto',15),(168,'2026-06-07 05:02:24','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(169,'2026-06-07 05:02:25','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(170,'2026-06-07 05:02:26','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(171,'2026-06-07 05:02:28','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(172,'2026-06-07 05:02:29','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(173,'2026-06-07 05:02:33','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(174,'2026-06-07 05:02:35','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(175,'2026-06-07 05:02:36','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(176,'2026-06-07 05:02:49','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(177,'2026-06-07 05:03:02','SOLICITAR_MATERIAL',3,'Cantidad 1',15),(178,'2026-06-07 05:03:04','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(179,'2026-06-07 05:03:07','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(180,'2026-06-07 05:03:07','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(181,'2026-06-07 05:03:07','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(182,'2026-06-07 05:03:08','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(183,'2026-06-07 05:03:11','SOLICITAR_MAQUINA',4,'Uso activo',15),(184,'2026-06-07 05:03:12','ACCION_NO_AUTORIZADA',NULL,'CONSULTAR_MAQUINARIA',15),(185,'2026-06-07 05:03:14','SOLICITAR_MAQUINA',6,'Uso activo',15),(186,'2026-06-07 05:03:14','ACCION_NO_AUTORIZADA',NULL,'CONSULTAR_MAQUINARIA',15),(187,'2026-06-07 05:03:16','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(188,'2026-06-07 05:03:17','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(189,'2026-06-07 05:03:18','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(190,'2026-06-07 05:03:29','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(191,'2026-06-07 05:03:29','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(192,'2026-06-07 05:03:30','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(193,'2026-06-07 05:03:30','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(194,'2026-06-07 05:03:31','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',13),(195,'2026-06-07 05:04:16','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(196,'2026-06-07 05:10:52','LOGIN_CORRECTO',15,'Inicio de sesion correcto',15),(197,'2026-06-07 05:10:52','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(198,'2026-06-07 05:10:53','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(199,'2026-06-07 05:10:56','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(200,'2026-06-07 05:10:57','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(201,'2026-06-07 05:11:40','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(202,'2026-06-07 05:11:40','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(203,'2026-06-07 05:11:43','SOLICITAR_MAQUINA',5,'Uso activo',15),(204,'2026-06-07 05:11:44','ACCION_NO_AUTORIZADA',NULL,'CONSULTAR_MAQUINARIA',15),(205,'2026-06-07 05:13:13','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(206,'2026-06-07 05:13:13','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(207,'2026-06-07 05:13:24','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(208,'2026-06-07 05:13:24','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(209,'2026-06-07 05:13:25','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(210,'2026-06-07 05:13:25','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(211,'2026-06-07 05:13:26','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(212,'2026-06-07 05:13:45','LOGIN_CORRECTO',14,'Inicio de sesion correcto',14),(213,'2026-06-07 05:13:45','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(214,'2026-06-07 05:13:55','ANADIR_USUARIO_PROYECTO',1,'Usuario 2',14),(215,'2026-06-07 05:14:02','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(216,'2026-06-07 05:14:14','ANADIR_USUARIO_PROYECTO',1,'Usuario 17',14),(217,'2026-06-07 05:14:18','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(218,'2026-06-07 05:14:21','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(219,'2026-06-07 05:14:24','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(220,'2026-06-07 05:14:33','ELIMINAR_USUARIO_PROYECTO',1,'Usuario 17',14),(221,'2026-06-07 05:14:38','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(222,'2026-06-07 05:14:38','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(223,'2026-06-07 05:14:46','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(224,'2026-06-07 05:14:48','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(225,'2026-06-07 05:15:10','ANADIR_ENTRADA_PANEL',3,'Cancer',14),(226,'2026-06-07 05:15:10','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(227,'2026-06-07 05:15:18','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(228,'2026-06-07 05:15:32','CONSULTAR_LOGS',NULL,'Consulta de logs',14),(229,'2026-06-07 05:15:37','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(230,'2026-06-07 05:15:37','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(231,'2026-06-07 05:15:47','LOGIN_CORRECTO',15,'Inicio de sesion correcto',15),(232,'2026-06-07 05:15:47','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(233,'2026-06-07 05:15:49','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(234,'2026-06-07 05:15:52','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(235,'2026-06-07 05:15:53','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(236,'2026-06-07 05:15:53','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(237,'2026-06-07 05:15:57','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(238,'2026-06-07 05:15:57','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(239,'2026-06-07 05:15:58','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(240,'2026-06-07 05:15:58','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(241,'2026-06-07 05:15:58','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(242,'2026-06-07 05:15:58','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(243,'2026-06-07 05:16:24','LOGIN_CORRECTO',14,'Inicio de sesion correcto',14),(244,'2026-06-07 05:16:24','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(245,'2026-06-07 05:16:29','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(246,'2026-06-07 05:16:29','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(247,'2026-06-07 05:16:29','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(248,'2026-06-07 05:16:32','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(249,'2026-06-07 05:16:35','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(250,'2026-06-07 05:16:36','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(251,'2026-06-07 05:16:36','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(252,'2026-06-07 05:16:37','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(253,'2026-06-07 05:16:39','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(254,'2026-06-07 05:36:35','LOGIN_CORRECTO',15,'Inicio de sesion correcto',15),(255,'2026-06-07 05:36:35','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(256,'2026-06-07 05:36:36','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(257,'2026-06-07 05:36:37','CONSULTAR_PANEL',NULL,'Consulta de panel',15),(258,'2026-06-07 05:36:40','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(259,'2026-06-07 05:36:42','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(260,'2026-06-07 05:36:43','ACCION_NO_AUTORIZADA',NULL,'CONSULTAR_MIEMBROS_PROYECTO',15),(261,'2026-06-07 05:36:45','ACCION_NO_AUTORIZADA',NULL,'CONSULTAR_MIEMBROS_PROYECTO',15),(262,'2026-06-07 05:36:47','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(263,'2026-06-07 05:36:57','FINALIZAR_USO_MAQUINA',5,'Uso finalizado',15),(264,'2026-06-07 05:36:57','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(265,'2026-06-07 05:36:58','FINALIZAR_USO_MAQUINA',4,'Uso finalizado',15),(266,'2026-06-07 05:36:59','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(267,'2026-06-07 05:37:00','FINALIZAR_USO_MAQUINA',6,'Uso finalizado',15),(268,'2026-06-07 05:37:00','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(269,'2026-06-07 05:37:03','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(270,'2026-06-07 05:37:08','SOLICITAR_MAQUINA',4,'Uso activo en proyecto 1',15),(271,'2026-06-07 05:37:09','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(272,'2026-06-07 05:37:09','FINALIZAR_USO_MAQUINA',4,'Uso finalizado',15),(273,'2026-06-07 05:37:10','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(274,'2026-06-07 05:37:58','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(275,'2026-06-07 05:37:59','SOLICITAR_MAQUINA',6,'Uso activo en proyecto 2',15),(276,'2026-06-07 05:38:00','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',15),(277,'2026-06-07 05:38:26','LOGIN_CORRECTO',14,'Inicio de sesion correcto',14),(278,'2026-06-07 05:38:26','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(279,'2026-06-07 05:38:30','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(280,'2026-06-07 05:38:36','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(281,'2026-06-07 05:38:38','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(282,'2026-06-07 05:38:39','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(283,'2026-06-07 05:38:40','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(284,'2026-06-07 05:38:42','SOLICITAR_MAQUINA',4,'Uso activo en proyecto 2',14),(285,'2026-06-07 05:38:43','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(286,'2026-06-07 05:38:45','FINALIZAR_USO_MAQUINA',4,'Uso finalizado',14),(287,'2026-06-07 05:38:46','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(288,'2026-06-07 05:38:48','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(289,'2026-06-07 05:38:49','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',14),(290,'2026-06-07 05:38:50','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(291,'2026-06-07 05:39:34','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(292,'2026-06-07 05:39:34','CONSULTAR_PANEL',NULL,'Consulta de panel',14),(293,'2026-06-07 05:39:35','CONSULTAR_LOGS',NULL,'Consulta de logs',14),(294,'2026-06-07 05:39:48','LOGIN_CORRECTO',16,'Inicio de sesion correcto',16),(295,'2026-06-07 05:39:48','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(296,'2026-06-07 05:39:53','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(297,'2026-06-07 05:39:56','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(298,'2026-06-07 05:39:57','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(299,'2026-06-07 05:40:00','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(300,'2026-06-07 05:40:08','LOGIN_CORRECTO',16,'Inicio de sesion correcto',16),(301,'2026-06-07 05:40:08','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(302,'2026-06-07 05:40:12','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(303,'2026-06-07 05:40:12','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(304,'2026-06-07 05:40:17','CONSULTAR_LOGS',NULL,'Consulta de logs',16),(305,'2026-06-07 05:40:19','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',16),(306,'2026-06-07 05:40:38','LOGIN_CORRECTO',17,'Inicio de sesion correcto',17),(307,'2026-06-07 05:40:38','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(308,'2026-06-07 05:40:45','ANADIR_MAQUINA',13,'bartolo',17),(309,'2026-06-07 05:40:46','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(310,'2026-06-07 05:40:51','ELIMINAR_MAQUINA',13,'Maquina eliminada o retirada',17),(311,'2026-06-07 05:40:51','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(312,'2026-06-07 05:41:32','ANADIR_MAQUINA',14,'var',17),(313,'2026-06-07 05:41:33','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(314,'2026-06-07 05:41:37','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(315,'2026-06-07 05:41:39','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(316,'2026-06-07 05:41:41','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(317,'2026-06-07 05:41:48','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(318,'2026-06-07 05:41:49','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',17),(319,'2026-06-07 05:41:52','CONSULTAR_MAQUINARIA',NULL,'Consulta de maquinaria',17),(320,'2026-06-07 05:41:54','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',17),(321,'2026-06-07 05:41:57','SOLICITAR_MATERIAL',3,'Cantidad 3',17),(322,'2026-06-07 05:42:00','CONSULTAR_PROYECTOS',NULL,'Consulta de proyectos',17),(323,'2026-06-07 05:43:46','CONSULTAR_PANEL',NULL,'Consulta de panel',17),(324,'2026-06-07 05:43:56','LOGIN_CORRECTO',13,'Inicio de sesion correcto',13),(325,'2026-06-07 05:43:56','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(326,'2026-06-07 05:43:57','CONSULTAR_INVENTARIO',NULL,'Consulta de inventario',13),(327,'2026-06-07 05:43:58','CONSULTAR_PANEL',NULL,'Consulta de panel',13),(328,'2026-06-07 05:44:17','CONSULTAR_PANEL',NULL,'Consulta de panel',13);
/*!40000 ALTER TABLE `logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machine_location`
--

DROP TABLE IF EXISTS `machine_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machine_location` (
  `machine_id` int NOT NULL,
  `storage_id` int NOT NULL,
  PRIMARY KEY (`machine_id`),
  KEY `FK_MachineLocation_Storage` (`storage_id`),
  CONSTRAINT `FK_MachineLocation_Machines` FOREIGN KEY (`machine_id`) REFERENCES `machines` (`machine_id`),
  CONSTRAINT `FK_MachineLocation_Storage` FOREIGN KEY (`storage_id`) REFERENCES `storage` (`storage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine_location`
--

LOCK TABLES `machine_location` WRITE;
/*!40000 ALTER TABLE `machine_location` DISABLE KEYS */;
INSERT INTO `machine_location` VALUES (4,1),(5,3),(6,3),(14,3);
/*!40000 ALTER TABLE `machine_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machine_usage`
--

DROP TABLE IF EXISTS `machine_usage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machine_usage` (
  `usage_id` int NOT NULL AUTO_INCREMENT,
  `machine_id` int NOT NULL,
  `user_id` int NOT NULL,
  `project_id` int DEFAULT NULL,
  `start_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `end_date` datetime DEFAULT NULL,
  `state` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`usage_id`),
  KEY `FK_MachineUsage_Machines` (`machine_id`),
  KEY `FK_MachineUsage_Users` (`user_id`),
  CONSTRAINT `FK_MachineUsage_Machines` FOREIGN KEY (`machine_id`) REFERENCES `machines` (`machine_id`),
  CONSTRAINT `FK_MachineUsage_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machine_usage`
--

LOCK TABLES `machine_usage` WRITE;
/*!40000 ALTER TABLE `machine_usage` DISABLE KEYS */;
INSERT INTO `machine_usage` VALUES (1,4,15,NULL,'2026-06-07 05:03:11','2026-06-07 05:36:58','FINALIZADO'),(2,6,15,NULL,'2026-06-07 05:03:14','2026-06-07 05:37:00','FINALIZADO'),(3,5,15,NULL,'2026-06-07 05:11:43','2026-06-07 05:36:57','FINALIZADO'),(4,4,15,1,'2026-06-07 05:37:08','2026-06-07 05:37:09','FINALIZADO'),(5,6,15,2,'2026-06-07 05:37:59',NULL,'ACTIVO'),(6,4,14,2,'2026-06-07 05:38:42','2026-06-07 05:38:45','FINALIZADO');
/*!40000 ALTER TABLE `machine_usage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machines`
--

DROP TABLE IF EXISTS `machines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `machines` (
  `machine_id` int NOT NULL,
  `state` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_revision_date` date DEFAULT NULL,
  `next_revision_date` date DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`machine_id`),
  CONSTRAINT `FK_Machines_Assets` FOREIGN KEY (`machine_id`) REFERENCES `assets` (`asset_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machines`
--

LOCK TABLES `machines` WRITE;
/*!40000 ALTER TABLE `machines` DISABLE KEYS */;
INSERT INTO `machines` VALUES (4,'Operativa','2026-01-15','2026-07-15','Centrifuga refrigerada'),(5,'Operativa','2026-02-01','2026-08-01','Microscopio optico'),(6,'En uso','2026-03-10','2026-06-30','Autoclave de esterilizacion'),(14,'Operativa','2020-07-08','2026-08-20','None');
/*!40000 ALTER TABLE `machines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_movements`
--

DROP TABLE IF EXISTS `material_movements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material_movements` (
  `movement_id` int NOT NULL AUTO_INCREMENT,
  `material_id` int NOT NULL,
  `storage_id` int NOT NULL,
  `batch_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` int NOT NULL,
  `quantity` decimal(10,2) NOT NULL,
  `movement_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `movement_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`movement_id`),
  KEY `FK_MaterialMovements_Materials` (`material_id`),
  KEY `FK_MaterialMovements_Storage` (`storage_id`),
  KEY `FK_MaterialMovements_Users` (`user_id`),
  CONSTRAINT `FK_MaterialMovements_Materials` FOREIGN KEY (`material_id`) REFERENCES `materials` (`material_id`),
  CONSTRAINT `FK_MaterialMovements_Storage` FOREIGN KEY (`storage_id`) REFERENCES `storage` (`storage_id`),
  CONSTRAINT `FK_MaterialMovements_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_movements`
--

LOCK TABLES `material_movements` WRITE;
/*!40000 ALTER TABLE `material_movements` DISABLE KEYS */;
INSERT INTO `material_movements` VALUES (1,7,2,'PBC-001',18,30.00,'ENTRADA','2026-06-07 04:40:22','Alta de lote'),(2,1,2,'PBC-001',13,35.00,'ENTRADA','2026-06-07 04:49:00','Alta de lote'),(3,7,2,'pbc-001',13,32.00,'ENTRADA','2026-06-07 04:49:31','Alta de lote'),(4,3,1,'HCL-001',15,1.00,'SOLICITUD','2026-06-07 05:03:02','Solicitud de material'),(5,3,1,'HCL-001',17,3.00,'SOLICITUD','2026-06-07 05:41:57','Solicitud de material');
/*!40000 ALTER TABLE `material_movements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materials`
--

DROP TABLE IF EXISTS `materials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materials` (
  `material_id` int NOT NULL,
  `specifications` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `formula` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `measure_unit` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`material_id`),
  CONSTRAINT `FK_Materials_Assets` FOREIGN KEY (`material_id`) REFERENCES `assets` (`asset_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materials`
--

LOCK TABLES `materials` WRITE;
/*!40000 ALTER TABLE `materials` DISABLE KEYS */;
INSERT INTO `materials` VALUES (1,'Desinfectante de laboratorio','C2H6O','L'),(2,'Solucion tampon','PBS','L'),(3,'Reactivo corrosivo','HCl','L'),(7,'ninguna','PBC','g');
/*!40000 ALTER TABLE `materials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panel_entries`
--

DROP TABLE IF EXISTS `panel_entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `panel_entries` (
  `entry_id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `study_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `likes` int NOT NULL DEFAULT '0',
  `dislikes` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`entry_id`),
  KEY `FK_PanelEntries_Projects` (`project_id`),
  KEY `FK_PanelEntries_Studies` (`study_id`),
  KEY `FK_PanelEntries_Users` (`user_id`),
  CONSTRAINT `FK_PanelEntries_Projects` FOREIGN KEY (`project_id`) REFERENCES `projects` (`project_id`),
  CONSTRAINT `FK_PanelEntries_Studies` FOREIGN KEY (`study_id`) REFERENCES `studies` (`study_id`),
  CONSTRAINT `FK_PanelEntries_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panel_entries`
--

LOCK TABLES `panel_entries` WRITE;
/*!40000 ALTER TABLE `panel_entries` DISABLE KEYS */;
INSERT INTO `panel_entries` VALUES (1,1,1,15,'Inicio de estudio','Registro inicial del estudio de bioseguridad.','2026-06-07 03:37:19',0,0),(2,2,2,14,'Revision de reactivos','Se revisan lotes con stock bajo y proxima caducidad.','2026-06-07 03:37:19',0,0),(3,1,2,14,'Cancer','investigacion','2026-06-07 05:15:10',0,0);
/*!40000 ALTER TABLE `panel_entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `project_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `state` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,'Proyecto Bioseguridad','Control de trazabilidad de muestras','2026-01-01',NULL,'Activo'),(2,'Proyecto Reactivos','Optimizacion de uso de reactivos','2026-02-01',NULL,'Activo');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `permisos` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Administrador','administracion, inventario, maquinaria, panel, logs, backup, estadisticas'),(2,'Director','proyectos, panel, miembros, solicitudes, logs'),(3,'Investigador','proyectos, panel, solicitudes'),(4,'Auditor','proyectos, logs, miembros'),(5,'Tecnico','maquinaria'),(6,'Reponedor','inventario');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage` (
  `storage_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `specifications` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`storage_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (1,'Almacen Quimico','Reactivos y sustancias controladas'),(2,'Almacen Biologico','Material biologico y consumibles'),(3,'Sala Maquinaria','Equipos de laboratorio');
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storedin`
--

DROP TABLE IF EXISTS `storedin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storedin` (
  `material_id` int NOT NULL,
  `storage_id` int NOT NULL,
  `quantity` decimal(10,2) DEFAULT NULL,
  `batch_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `exp_date` date DEFAULT NULL,
  PRIMARY KEY (`material_id`,`storage_id`,`batch_number`),
  KEY `FK_StoredIn_Storage` (`storage_id`),
  CONSTRAINT `FK_StoredIn_Materials` FOREIGN KEY (`material_id`) REFERENCES `materials` (`material_id`),
  CONSTRAINT `FK_StoredIn_Storage` FOREIGN KEY (`storage_id`) REFERENCES `storage` (`storage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storedin`
--

LOCK TABLES `storedin` WRITE;
/*!40000 ALTER TABLE `storedin` DISABLE KEYS */;
INSERT INTO `storedin` VALUES (1,1,25.00,'ET-001','2026-12-31'),(1,2,35.00,'PBC-001','2027-07-21'),(2,2,12.00,'PBS-001','2026-10-15'),(7,2,32.00,'pbc-001','2028-09-12');
/*!40000 ALTER TABLE `storedin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studies`
--

DROP TABLE IF EXISTS `studies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studies` (
  `study_id` int NOT NULL AUTO_INCREMENT,
  `project_id` int DEFAULT NULL,
  PRIMARY KEY (`study_id`),
  KEY `FK_Studies_Projects` (`project_id`),
  CONSTRAINT `FK_Studies_Projects` FOREIGN KEY (`project_id`) REFERENCES `projects` (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studies`
--

LOCK TABLES `studies` WRITE;
/*!40000 ALTER TABLE `studies` DISABLE KEYS */;
INSERT INTO `studies` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `studies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userrole`
--

DROP TABLE IF EXISTS `userrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userrole` (
  `user_id` int NOT NULL,
  `role_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`role_id`),
  KEY `FK_UserRole_Roles` (`role_id`),
  CONSTRAINT `FK_UserRole_Roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`),
  CONSTRAINT `FK_UserRole_Users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userrole`
--

LOCK TABLES `userrole` WRITE;
/*!40000 ALTER TABLE `userrole` DISABLE KEYS */;
INSERT INTO `userrole` VALUES (13,1),(14,2),(15,3),(17,3),(16,4),(17,5),(18,6);
/*!40000 ALTER TABLE `userrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pass_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `full_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DNI` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `state` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `studies` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `login` (`login`),
  UNIQUE KEY `DNI` (`DNI`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (13,'admin','$2b$12$Ib7I7gCauEzy3UhQQfCEROW6JUfoiA30MMHXAmR5D9JZtsX3JzA8u','Administrador LabTrack','00000001A','Activo','General'),(14,'director','$2b$12$3d/OK.ZIWphGN6kvQzgybeXu9whUl7e2sp/LNrU6SNXkqI8rTog52','Director de Proyecto','00000002B','Activo','General'),(15,'investigador','$2b$12$zf3S/u0rOhxE1K1l8ogqa.nWJXx5rLH1gItm7gIECKbi/NYjEaPHa','Investigador Principal','00000003C','Activo','General'),(16,'auditor','$2b$12$3B5BycNNz2GBbO80SzLtK.bfkAvLXInlCofpwpERVcYuFRPSJ2iKS','Auditor Calidad','00000004D','Activo','General'),(17,'tecnico','$2b$12$jE5hRN0y31n1Cpx9UDA3/OjByt5mATCWMQ/nTVAFcQ53KaZrdXl0u','Tecnico de Maquinaria','00000005E','Activo','General'),(18,'reponedor','$2b$12$G5oA/3Bc0MRlNcdGvIC.dO2kHAh2JG.z2ix4Hi0xMw3hplTi1eDAe','Reponedor de Inventario','00000006F','Activo','General');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-07  5:44:19
