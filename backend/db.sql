-- MySQL dump 10.13  Distrib 8.0.15, for macos10.14 (x86_64)
--
-- Host: 127.0.0.1    Database: ACHIEVEIT
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `employee` (
  `id` varchar(45) NOT NULL COMMENT '每个员工都有自己的ID',
  `name` varchar(45) DEFAULT NULL COMMENT '员工名称',
  `gender` varchar(45) DEFAULT NULL COMMENT '员工性别',
  `career` varchar(45) DEFAULT NULL COMMENT '员工职位信息',
  `superior_id` varchar(45) DEFAULT NULL COMMENT '员工的项目上级',
  `tele` varchar(45) DEFAULT NULL COMMENT '员工电话信息',
  `department` varchar(45) DEFAULT NULL COMMENT '员工部门',
  `mailbox` varchar(45) DEFAULT NULL COMMENT '员工邮箱地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('0000','老板','女','项目上级',NULL,'000111',NULL,NULL),('0011','卡桑','男','项目经理','0000','12344321','软件1组','12344321'),('0012','小黄','女','架构师','0011','11112222','软件1组','11112222'),('0013','费费','男','开发leader','0011','22223333','软件1组','22223333'),('0014','坤','女','开发','0013','33334444','软件1组','33334444'),('0015','大虾','男','开发','0013','44445555','软件1组','44445555'),('0016','倩','女','测试leader','0011','55556666','软件1组','55556666'),('0017','工具人','男','测试','0016','66667777','软件1组','66667777');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `login` (
  `id` varchar(45) NOT NULL COMMENT '员工ID',
  `username` varchar(45) DEFAULT NULL COMMENT '用户名',
  `password` varchar(45) DEFAULT NULL COMMENT '用户密码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('0000','老板','000000'),('0011','卡桑','000111'),('0012','小黄','123456'),('0013','费费','111222'),('0014','坤','222333'),('0015','大虾','333444'),('0016','倩 ','444555'),('0017','工具人','555666');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `project` (
  `id` varchar(45) NOT NULL COMMENT '项目ID',
  `name` varchar(45) DEFAULT NULL COMMENT '项目名称',
  `status` int(11) DEFAULT NULL COMMENT '项目状态',
  `customer_id` varchar(45) DEFAULT NULL COMMENT '客户ID',
  `main_function` varchar(45) DEFAULT NULL COMMENT '主要功能',
  `domain_id` varchar(45) DEFAULT NULL COMMENT '业务领域',
  `tech` varchar(45) DEFAULT NULL,
  `project_leader_id` varchar(45) DEFAULT NULL COMMENT '项目上级',
  `submit_date` date DEFAULT NULL COMMENT '交付日',
  `reserve_date` date DEFAULT NULL COMMENT '交付日',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES ('01','图书馆系统',0,NULL,'图书租借',NULL,'共享','0000','2020-03-20','2020-03-25'),('02','外卖系统',3,NULL,'外卖拼单',NULL,'拼单','0000','2020-03-28','2020-03-29');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_participatnt`
--

DROP TABLE IF EXISTS `project_participatnt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `project_participatnt` (
  `project_id` varchar(45) NOT NULL,
  `person_id` varchar(45) NOT NULL,
  `leader_id` varchar(45) NOT NULL,
  PRIMARY KEY (`project_id`,`person_id`,`leader_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_participatnt`
--

LOCK TABLES `project_participatnt` WRITE;
/*!40000 ALTER TABLE `project_participatnt` DISABLE KEYS */;
INSERT INTO `project_participatnt` VALUES ('01','0011','0000'),('01','0012','0011'),('02','0011','0000'),('02','0012','0011'),('02','0013','0011'),('02','0014','0013'),('02','0015','0013'),('02','0016','0011'),('02','0017','0016');
/*!40000 ALTER TABLE `project_participatnt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_time`
--

DROP TABLE IF EXISTS `work_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `work_time` (
  `work_time_id` int(11) NOT NULL COMMENT '工时ID',
  `worker_id` varchar(45) DEFAULT NULL COMMENT '员工id',
  `project_id` varchar(45) DEFAULT NULL COMMENT '项目ID',
  `work_date` varchar(45) DEFAULT NULL COMMENT '日期',
  `work_info` varchar(45) DEFAULT NULL COMMENT '工时信息',
  `worktime_remian` varchar(45) DEFAULT NULL COMMENT '工时剩余',
  `status` varchar(45) DEFAULT NULL COMMENT '状态',
  `remarks` varchar(45) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`work_time_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_time`
--

LOCK TABLES `work_time` WRITE;
/*!40000 ALTER TABLE `work_time` DISABLE KEYS */;
INSERT INTO `work_time` VALUES (1,'0012','01','2020-03-14','图书馆','5','0',NULL),(2,'0012','01','2020-03-15','图书馆代码','8','1',NULL),(3,'0013','01','2020-03-16','图书馆代码实现','9','1',NULL),(4,'0013','01','2020-03-14','图书馆代码实现','10','0',NULL),(5,'0014','02','2020-03-15','拼单','3','1',NULL),(6,'0015','02','2020-03-13','外卖系统','4','1',NULL),(7,'0014','01','2020-03-15','图书馆页面','6','0',NULL),(8,'0016','02','2020-03-16','测试','9','0',NULL),(9,'0017','01','2020-03-15','测试','7','1',NULL),(10,'0011','02','2020-03-16','代码设计','0','0',NULL);
/*!40000 ALTER TABLE `work_time` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-16 11:46:52
