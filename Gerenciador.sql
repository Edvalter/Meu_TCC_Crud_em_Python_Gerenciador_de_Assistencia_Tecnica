CREATE DATABASE  IF NOT EXISTS `gerenciador` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gerenciador`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: gerenciador
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
-- Table structure for table `cad_pessoas`
--

DROP TABLE IF EXISTS `cad_pessoas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cad_pessoas` (
  `id_pessoas` int NOT NULL AUTO_INCREMENT,
  `cpf` int DEFAULT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `telefone` varchar(100) DEFAULT NULL,
  `whatsapp` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cep` int DEFAULT NULL,
  `rua` varchar(100) DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  `observacoes` varchar(200) DEFAULT NULL,
  `data_cadastro` date DEFAULT NULL,
  PRIMARY KEY (`id_pessoas`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cad_pessoas`
--

LOCK TABLES `cad_pessoas` WRITE;
/*!40000 ALTER TABLE `cad_pessoas` DISABLE KEYS */;
INSERT INTO `cad_pessoas` VALUES (1,47487931,'Edvalter Feliciano','992479998','47992479998','feliciano_edvalter@hotmail.com',89120000,'Quenia',94,'centro','timbo','SC','Apartamento 202','2022-08-05'),(3,47487933,'Ed Feliciano','992479998','47992479998','feliciano_edvalter@hotmail.com',89120000,'Quenia',94,'centro','timbo','SC','Apartamento 202','0005-09-22'),(4,47487934,'Ed Feliciano','992479998','47992479998','feliciano_edvalter@hotmail.com',89120000,'Quenia',94,'centro','timbo','SC','Apartamento 202','0005-02-22'),(5,47487935,'Edvalter Feliciano','992479998','47992479998','feliciano_edvalter@hotmail.com',89120000,'Quenia',94,'centro','timbo','SC','Apartamento 202','2022-09-05'),(6,47487933,'Ed Feliciano','992479998','47992479998','feliciano_edvalter@hotmail.com',89120000,'Quenia',94,'centro','timbo','SC','Apartamento 202','0005-09-22');
/*!40000 ALTER TABLE `cad_pessoas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cad_produto`
--

DROP TABLE IF EXISTS `cad_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cad_produto` (
  `id_produto` int NOT NULL AUTO_INCREMENT,
  `produto` varchar(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `cor` varchar(100) DEFAULT NULL,
  `valor_compra` float DEFAULT NULL,
  `valor_venda` float DEFAULT NULL,
  `estoque` int DEFAULT NULL,
  PRIMARY KEY (`id_produto`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cad_produto`
--

LOCK TABLES `cad_produto` WRITE;
/*!40000 ALTER TABLE `cad_produto` DISABLE KEYS */;
INSERT INTO `cad_produto` VALUES (11,'Dock Carga','Xiaomi','Note 8 Plus','Padrão',35,140,1),(12,'Tela Display','Asus','Zenfone 3','Branca',105,270,1),(13,'Tela Display','Asus','Zenfone 3','Preta',100,260,1),(14,'Dock Carga','Xiaomi','Note 8 Plus','Padrão',35,140,1),(15,'Tela Display','Asus','Zenfone 3','Preta',100,260,1),(16,'Tela Display','Asus','Zenfone 3','Branca',105,270,1),(17,'Tela Display','Asus','Zenfone 4','Preta',100,260,1),(18,'Tela Display','Asus','Zenfone 5','Preta',100,260,1),(19,'Tela Display','Asus','Zenfone 5','Preta',230,460,1),(20,'Tela Display','Apple','Iphone 6','Preta',60,160,1),(21,'Tela Display','Apple','Iphone 6','Branca',60,160,1),(22,'Tela Display','Apple','Iphone 6s','Preta',85,190,1),(23,'Tela Display','Apple','Iphone 6s','Branca',80,200,1),(24,'Tela Display','Apple','Iphone 7','Preta',140,320,1),(25,'Tela Display','Apple','Iphone 8','Preta',180,390,1),(26,'Tela Display','Apple','Iphone 8 Plus','Preta',180,390,1),(27,'Tela Display','Samsung','Galaxy J7 Pro','Preta',260,460,1),(28,'Tela Display','Samsung','Galaxy J7 Pro','Dourada',260,460,1),(29,'Tela Display','Samsung','Galaxy J5 Pro','Preta',240,440,1),(30,'Conector','Samsung','Galaxy J7 Pro','Padrão',2,260,10),(31,'Conector','Samsung','Galaxy J5 Pro','Padrão',2,260,10),(32,'Conector','Samsung','Galaxy S9','Padrão',30,320,10),(33,'Conector','Samsung','Galaxy S9','Padrão',30,370,10),(34,'Dock Carga','Asus','Zenfone 3','Padrão',25,110,1),(35,'Dock Carga','Asus','Zenfone 5','Padrão',27,120,1),(36,'Dock Carga','Asus','Zenfone 5 Selfie','Padrão',27,120,1),(37,'Dock Carga','Apple','Iphone 7','Padrão',35,160,1),(38,'Dock Carga','Apple','Iphone 7 Plus','Padrão',35,160,1),(39,'Dock Carga','Apple','Iphone 8','Padrão',35,160,1),(40,'Dock Carga','Apple','Iphone 8 Plus','Padrão',35,160,1),(41,'Dock Carga','Xiaomi','Note 8','Padrão',35,140,1),(42,'Dock Carga','Xiaomi','Note 8 Plus','Padrão',35,140,1),(43,'Dock Carga','Xiaomi','Note 9','Padrão',35,140,1);
/*!40000 ALTER TABLE `cad_produto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orcamento`
--

DROP TABLE IF EXISTS `orcamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orcamento` (
  `id_orcamento` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `cpf` int NOT NULL,
  `nome` varchar(10) NOT NULL,
  `whatsapp` int NOT NULL,
  `produto` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `cor` varchar(100) DEFAULT NULL,
  `defeito` varchar(100) DEFAULT NULL,
  `observacao` varchar(200) DEFAULT NULL,
  `data_entrada` int DEFAULT NULL,
  `data_retirada` int DEFAULT NULL,
  PRIMARY KEY (`id_orcamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orcamento`
--

LOCK TABLES `orcamento` WRITE;
/*!40000 ALTER TABLE `orcamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `orcamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orcamentoteste`
--

DROP TABLE IF EXISTS `orcamentoteste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orcamentoteste` (
  `id_orcamento` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `cpf` int NOT NULL,
  `nome` varchar(10) NOT NULL,
  `whatsapp` int NOT NULL,
  `produto` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `cor` varchar(100) DEFAULT NULL,
  `defeito` varchar(100) DEFAULT NULL,
  `observacao` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_orcamento`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orcamentoteste`
--

LOCK TABLES `orcamentoteste` WRITE;
/*!40000 ALTER TABLE `orcamentoteste` DISABLE KEYS */;
INSERT INTO `orcamentoteste` VALUES (1,5,474,'Edv',999,'tela','Iphone 6s','aple','preto','tela','pelici');
/*!40000 ALTER TABLE `orcamentoteste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orcamentoteste2`
--

DROP TABLE IF EXISTS `orcamentoteste2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orcamentoteste2` (
  `id_orcamento` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `cpf` int NOT NULL,
  `nome` varchar(10) NOT NULL,
  `whatsapp` int NOT NULL,
  `produto` varchar(100) NOT NULL,
  `modelo` varchar(100) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `cor` varchar(100) DEFAULT NULL,
  `defeito` varchar(100) DEFAULT NULL,
  `observacao` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_orcamento`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orcamentoteste2`
--

LOCK TABLES `orcamentoteste2` WRITE;
/*!40000 ALTER TABLE `orcamentoteste2` DISABLE KEYS */;
INSERT INTO `orcamentoteste2` VALUES (1,5,474,'Edv',999,'tela','Iphone 6s','aple','preto','tela','pelici');
/*!40000 ALTER TABLE `orcamentoteste2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-14  7:51:52
