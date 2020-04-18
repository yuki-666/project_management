-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: achieveit
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `authority`
--

DROP TABLE IF EXISTS `authority`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authority` (
  `project_id` varchar(45) NOT NULL COMMENT '项目ID',
  `worker_id` varchar(45) NOT NULL COMMENT '人员ID',
  `git_authority` int DEFAULT NULL COMMENT 'git权限',
  `file_authority` int DEFAULT NULL COMMENT '文件权限',
  `mail_authority` int DEFAULT NULL COMMENT '邮箱权限',
  PRIMARY KEY (`project_id`,`worker_id`),
  KEY `worker_id_idx` (`worker_id`),
  CONSTRAINT `authority_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `authority_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authority`
--

LOCK TABLES `authority` WRITE;
/*!40000 ALTER TABLE `authority` DISABLE KEYS */;
INSERT INTO `authority` VALUES ('01','0012',1,0,0),('01','0013',0,0,0),('2020-0000-D-01','0012',1,0,0),('2020-0000-D-01','0015',1,1,0),('2020-0000-D-01','0016',1,0,1);
/*!40000 ALTER TABLE `authority` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `business_area`
--

DROP TABLE IF EXISTS `business_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `business_area` (
  `id` varchar(45) NOT NULL,
  `code` varchar(45) DEFAULT NULL COMMENT '客户代码',
  `name` varchar(45) DEFAULT NULL,
  `delete_label` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_area`
--

LOCK TABLES `business_area` WRITE;
/*!40000 ALTER TABLE `business_area` DISABLE KEYS */;
INSERT INTO `business_area` VALUES ('01','123456','软件',0),('02','234567','设计',0);
/*!40000 ALTER TABLE `business_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` varchar(45) NOT NULL,
  `project_broker_id` varchar(45) NOT NULL COMMENT '对接人id ',
  `company_name` varchar(45) NOT NULL COMMENT '公司名称',
  `address` varchar(45) NOT NULL COMMENT '公司地址（客户的）',
  `customer_tele` varchar(45) NOT NULL COMMENT '客户电弧',
  `customer_mail` varchar(45) DEFAULT NULL COMMENT '客户邮箱',
  `customer_level` varchar(45) NOT NULL COMMENT '客户等级',
  `delete_label` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_project_broker_idx` (`project_broker_id`),
  CONSTRAINT `customer_project_broker_id` FOREIGN KEY (`project_broker_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('001','0012','小黄游戏','上海','000111','000111','1',0),('002','0013','费费影业','无锡','111222','111222','2',0),('003','0014','坤坤米粉','新疆','222333','222333','1',0),('004','0015','大虾鞋服','上海','333444','333444','3',0),('005','0016','倩倩美妆','桂林','444555','444555','5',0);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` varchar(45) NOT NULL COMMENT '每个员工都有自己的ID',
  `name` varchar(45) DEFAULT NULL COMMENT '员工名称',
  `gender` varchar(45) DEFAULT NULL COMMENT '员工性别',
  `career` varchar(45) DEFAULT NULL COMMENT '员工职位信息',
  `superior_id` varchar(45) DEFAULT NULL COMMENT '员工的项目上级',
  `tele` varchar(45) DEFAULT NULL COMMENT '员工电话信息',
  `department` varchar(45) DEFAULT NULL COMMENT '员工部门',
  `mailbox` varchar(45) DEFAULT NULL COMMENT '员工邮箱地址',
  `delete_label` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('0000','老板','女','0',NULL,'000111',NULL,NULL,0),('0011','卡桑','男','0','0000','12344321','软件1组','12344321',0),('0012','小黄','女','1','0011','11112222','软件1组','11112222',0),('0013','费费','女','1','0011','22223333','软件1组','22223333',0),('0014','坤','女','2','0013','33334444','软件1组','33334444',0),('0015','大虾','男','1','0013','44445555','软件1组','44445555',0),('0016','倩','女','1','0011','55556666','软件1组','55556666',0),('0017','工具人','男','2','0016','66667777','软件1组','66667777',0),('0018','gsggf',NULL,'0',NULL,NULL,'gfsgfdsgf',NULL,0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `function_partition`
--

DROP TABLE IF EXISTS `function_partition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `function_partition` (
  `project_id` varchar(45) NOT NULL COMMENT '项目ID',
  `function_id` varchar(45) NOT NULL COMMENT '项目功能ID',
  `worker_id` varchar(45) NOT NULL COMMENT '员工ID',
  PRIMARY KEY (`project_id`,`function_id`,`worker_id`),
  KEY `function_partition_function_id_idx` (`function_id`),
  KEY `function_partition_worker_id_idx` (`worker_id`),
  CONSTRAINT `function_partition_function_id` FOREIGN KEY (`function_id`) REFERENCES `project_function` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `function_partition_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `function_partition_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `function_partition`
--

LOCK TABLES `function_partition` WRITE;
/*!40000 ALTER TABLE `function_partition` DISABLE KEYS */;
INSERT INTO `function_partition` VALUES ('2020-0000-D-02','001002','0012'),('2020-0000-D-02','001003','0013'),('2020-0000-D-02','002','0013'),('2020-0000-D-01','002004','0012'),('2020-0000-D-01','002005','0014'),('2020-0000-D-01','002005','0015'),('2020-0000-D-02','0029ZZ','0016'),('2020-0000-D-02','0029ZZ','0017');
/*!40000 ALTER TABLE `function_partition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `id` varchar(45) NOT NULL COMMENT '员工ID',
  `username` varchar(45) DEFAULT NULL COMMENT '登录名',
  `password` varchar(45) DEFAULT NULL COMMENT '用户密码',
  `delete_label` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `login_worker_id` FOREIGN KEY (`id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('0000','老板','000000',0),('0011','卡桑','000111',0),('0012','小黄','123456',0),('0013','费费','111222',0),('0014','坤','222333',0),('0015','大虾','333444',0),('0016','倩 ','444555',0),('0017','工具人','555666',0),('0018','fdasadsfdsa','fdfads',0);
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `id` varchar(45) NOT NULL COMMENT '项目ID',
  `name` varchar(45) DEFAULT NULL COMMENT '项目名称',
  `status` int DEFAULT NULL COMMENT '项目状态',
  `customer_id` varchar(45) DEFAULT NULL COMMENT '客户ID',
  `describe` varchar(45) DEFAULT NULL COMMENT '项目描述',
  `main_function` varchar(45) DEFAULT NULL COMMENT '主要功能',
  `major_milestones` varchar(45) DEFAULT NULL COMMENT '主要里程碑',
  `business_area` varchar(45) DEFAULT NULL COMMENT '业务领域',
  `adopting_technology` varchar(45) DEFAULT NULL COMMENT '采用技术',
  `project_superior_id` varchar(45) DEFAULT NULL COMMENT '项目上级',
  `delivery_day` date DEFAULT NULL COMMENT '交付日',
  `scheduled_time` date DEFAULT NULL COMMENT '预定时间',
  `update_time` timestamp NULL DEFAULT NULL COMMENT '更新时间',
  `delete_label` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_customer_id_idx` (`customer_id`),
  CONSTRAINT `project_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES ('01','图书馆系统12',2,'003','good1','图书租借','123','01','345','0018','2020-03-20','2020-03-03','2020-04-18 05:57:37',0),('2020-0000-D-01','图书馆系统',2,'001','good1','图书租借','123','01','345','0018','2020-03-20','2020-03-03','2020-04-17 17:16:41',0),('2020-0000-D-02','外卖系统',0,'002','hi','点外卖',NULL,'01',NULL,'0000','2020-03-20','2020-03-25','2020-01-12 02:23:45',0),('2020-001-S-00','afds1',1,'001','fdsa','fsad','afsd','02','fdsa','0011','2020-04-08','2020-04-07','2020-04-18 04:36:31',0);
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_equipment`
--

DROP TABLE IF EXISTS `project_equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_equipment` (
  `id` varchar(45) NOT NULL,
  `project_id` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `start_time` date DEFAULT NULL,
  `end_time` date DEFAULT NULL,
  `status` int DEFAULT NULL,
  `label` int DEFAULT NULL,
  `return_time` date DEFAULT NULL,
  `manager_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proeq_project_id_idx` (`project_id`),
  KEY `proeq_worker_id_idx` (`manager_id`),
  CONSTRAINT `proeq_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`),
  CONSTRAINT `proeq_worker_id` FOREIGN KEY (`manager_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_equipment`
--

LOCK TABLES `project_equipment` WRITE;
/*!40000 ALTER TABLE `project_equipment` DISABLE KEYS */;
INSERT INTO `project_equipment` VALUES ('1','01','范德萨范德萨','2020-04-08','2020-04-23',1,0,'0000-00-00','0012');
/*!40000 ALTER TABLE `project_equipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_flaw`
--

DROP TABLE IF EXISTS `project_flaw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_flaw` (
  `id` varchar(45) NOT NULL COMMENT '缺陷ID',
  `project_id` varchar(45) DEFAULT NULL COMMENT '项目ID',
  `describe` varchar(45) DEFAULT NULL COMMENT '缺陷描述',
  `level` int DEFAULT NULL COMMENT '风险等级',
  `follower_id` varchar(45) DEFAULT NULL COMMENT '追踪者',
  `status` int DEFAULT NULL COMMENT '缺陷状态（是否修复）',
  PRIMARY KEY (`id`),
  KEY `flaw_project_id_idx` (`project_id`),
  KEY `flaw_follower_id_idx` (`follower_id`),
  CONSTRAINT `flaw_follower_id` FOREIGN KEY (`follower_id`) REFERENCES `employee` (`id`),
  CONSTRAINT `flaw_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_flaw`
--

LOCK TABLES `project_flaw` WRITE;
/*!40000 ALTER TABLE `project_flaw` DISABLE KEYS */;
INSERT INTO `project_flaw` VALUES ('1','01','abc',0,'0013',1),('2','01','大师傅',2,'0013',1),('3','01','啊啊',0,'0012',1),('4','01','123',1,'0012',0),('5','01','嗷嗷嗷',1,'0012',0),('6','01','嗷嗷嗷123',0,'0013',0),('7','01','行政村',1,'0012',0);
/*!40000 ALTER TABLE `project_flaw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_function`
--

DROP TABLE IF EXISTS `project_function`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_function` (
  `id` varchar(45) NOT NULL,
  `project_id` varchar(45) NOT NULL COMMENT '项目id',
  `function_name` varchar(45) DEFAULT NULL COMMENT '功能名称',
  `function_status` int DEFAULT NULL COMMENT '功能状态',
  `parent_function_id` varchar(45) DEFAULT NULL COMMENT '父功能id',
  `delete_label` int DEFAULT NULL,
  PRIMARY KEY (`id`,`project_id`),
  KEY `project_id_idx` (`project_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `project_function_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_function`
--

LOCK TABLES `project_function` WRITE;
/*!40000 ALTER TABLE `project_function` DISABLE KEYS */;
INSERT INTO `project_function` VALUES ('001','2020-0000-D-01','ddd',0,'000',1),('001','2020-001-S-00','abc',0,'000',1),('001001','2020-0000-D-01','abc',0,'001',1),('001001','2020-001-S-00','bbb',0,'001',1),('001001001','2020-0000-D-01','aa',0,'001001',1),('001001002','2020-0000-D-01','bz',0,'001001',1),('001002','01','图书馆登录',0,'001',0),('001003','01','图书租借',1,'001',0),('002','2020-0000-D-01','aaa',0,'000',0),('002','2020-0000-D-02','图书馆登录',0,NULL,0),('002','2020-001-S-00','qq',0,'000',0),('002004','2020-0000-D-01','拼单数据库',1,'002',1),('002004002','2020-0000-D-01','fdfdsa',0,'002004',1),('002004002003','2020-0000-D-01','11111',0,'002004002',1),('002004002004','2020-0000-D-01','fadsfasfsa',0,'002004002',1),('002004002005','2020-0000-D-01','fdsafasdaa1',0,'002004002',1),('002004002006','2020-0000-D-01','qqqq',0,'002004002',1),('002004003','2020-0000-D-01','zzz',0,'002004',1),('002005','2020-0000-D-01','拼单测试',1,'002',0),('002005001','2020-0000-D-01','aaa',0,'002005',1),('002005001001','2020-0000-D-01','eee',0,'002005001',1),('002005001002','2020-0000-D-01','abc',0,'002005001',1),('002006','2020-0000-D-01','aaa',0,'002',1),('002007','2020-0000-D-01','65',0,'002',0),('0029ZZ','2020-0000-D-02','拼单测试',1,'002',0),('003','2020-0000-D-01','abc',0,'000',0),('004','2020-0000-D-01','abc',0,'000',0);
/*!40000 ALTER TABLE `project_function` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_participant`
--

DROP TABLE IF EXISTS `project_participant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_participant` (
  `project_id` varchar(45) NOT NULL,
  `person_id` varchar(45) NOT NULL,
  `leader_id` varchar(45) NOT NULL,
  PRIMARY KEY (`project_id`,`person_id`,`leader_id`),
  KEY `person_id_idx` (`person_id`),
  KEY `person_id2_idx` (`leader_id`),
  CONSTRAINT `project_participant_leader_id` FOREIGN KEY (`leader_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `project_participant_person_id` FOREIGN KEY (`person_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `project_participant_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_participant`
--

LOCK TABLES `project_participant` WRITE;
/*!40000 ALTER TABLE `project_participant` DISABLE KEYS */;
INSERT INTO `project_participant` VALUES ('2020-0000-D-01','0011','0000'),('01','0012','0000'),('01','0013','0012'),('02','0013','0011'),('02','0014','0013'),('02','0015','0013'),('02','0016','0011'),('02','0017','0016');
/*!40000 ALTER TABLE `project_participant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_risk`
--

DROP TABLE IF EXISTS `project_risk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_risk` (
  `id` varchar(45) NOT NULL,
  `project_id` varchar(45) DEFAULT NULL,
  `risk_level` varchar(45) DEFAULT NULL,
  `risk_describe` varchar(45) DEFAULT NULL,
  `project_label` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `risk_project_id_idx` (`project_id`),
  CONSTRAINT `risk_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_risk`
--

LOCK TABLES `project_risk` WRITE;
/*!40000 ALTER TABLE `project_risk` DISABLE KEYS */;
INSERT INTO `project_risk` VALUES ('1','01','1','213','0');
/*!40000 ALTER TABLE `project_risk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `super_login`
--

DROP TABLE IF EXISTS `super_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `super_login` (
  `username` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `super_login`
--

LOCK TABLES `super_login` WRITE;
/*!40000 ALTER TABLE `super_login` DISABLE KEYS */;
INSERT INTO `super_login` VALUES ('fdsafdsa','fdafdsa');
/*!40000 ALTER TABLE `super_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `work_time`
--

DROP TABLE IF EXISTS `work_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `work_time` (
  `id` int NOT NULL COMMENT '工时ID',
  `worker_id` varchar(45) DEFAULT NULL COMMENT '员工id',
  `project_id` varchar(45) DEFAULT NULL COMMENT '项目ID',
  `date` datetime DEFAULT NULL COMMENT '日期',
  `function_id` varchar(45) DEFAULT NULL COMMENT '功能id',
  `event_name` varchar(45) DEFAULT NULL COMMENT '活动名称',
  `start_time` int DEFAULT NULL COMMENT '开始时间',
  `end_time` int DEFAULT NULL COMMENT '结束时间',
  `remain` varchar(45) DEFAULT NULL COMMENT '剩余工时',
  `status` varchar(45) DEFAULT NULL COMMENT '审批状态',
  `remarks` varchar(45) DEFAULT NULL COMMENT '备注',
  `describe` varchar(45) DEFAULT NULL COMMENT '描述',
  `delete_label` int DEFAULT NULL COMMENT '删除标记',
  PRIMARY KEY (`id`),
  KEY `work_time_project_id_idx` (`project_id`),
  KEY `work_time_worker_id_idx` (`worker_id`),
  KEY `work_time_function_id_idx` (`function_id`),
  CONSTRAINT `work_time_function_id` FOREIGN KEY (`function_id`) REFERENCES `project_function` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `work_time_project_id` FOREIGN KEY (`project_id`) REFERENCES `project` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `work_time_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `employee` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `work_time`
--

LOCK TABLES `work_time` WRITE;
/*!40000 ALTER TABLE `work_time` DISABLE KEYS */;
INSERT INTO `work_time` VALUES (1,'0012','01','2020-03-14 00:00:00','01','图书馆',4,6,'5','0',NULL,'emm',1),(2,'0012','01','2020-04-21 00:00:00','01','图书馆代码',2,8,'8','1',NULL,'emm',0),(3,'0013','01','2020-03-16 00:00:00','02','图书馆代码实现',4,8,'9','1',NULL,'emm',0),(4,'0012','01','2020-03-14 00:00:00','02','图书馆代码实现',1,4,'10','0',NULL,'emm',1),(5,'0014','02','2020-03-15 00:00:00','03','拼单',5,16,'3','1',NULL,'emm',0),(6,'0015','02','2020-03-13 00:00:00','03','外卖系统',10,17,'4','1',NULL,'emm',1),(7,'0014','01','2020-03-15 00:00:00','04','图书馆页面',8,20,'6','0',NULL,'emm',0),(8,'0016','02','2020-03-16 00:00:00','04','测试',9,18,'9','0',NULL,'emm',1),(9,'0017','01','2020-03-15 00:00:00','05','测试',8,18,'7','1',NULL,'emm',0),(10,'0011','02','2020-03-16 00:00:00','05','代码设计',9,23,'0','0',NULL,'emm',0),(11,'0012','01','2020-04-21 00:00:00','002004','afsd',1,2,'3','1',NULL,'fdsas',0),(12,'0012','01','2020-04-17 00:00:00','002004','fdsa',1,24,'1','1',NULL,'21',0),(13,'0012','01','2020-04-16 00:00:00','002004','afsd',1,23,'22','1',NULL,'1',0);
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

-- Dump completed on 2020-04-18 21:27:36
