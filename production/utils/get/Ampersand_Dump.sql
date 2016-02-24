CREATE DATABASE  IF NOT EXISTS `Ampersand` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `Ampersand`;
-- MySQL dump 10.13  Distrib 5.6.19, for osx10.7 (i386)
--
-- Host: 127.0.0.1    Database: Ampersand
-- ------------------------------------------------------
-- Server version	5.6.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coat_cutting_pattern`
--

DROP TABLE IF EXISTS `coat_cutting_pattern`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coat_cutting_pattern` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cutting_instructions` longtext,
  `panel_depth_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_coat_cutting_pattern_panel_depth1_idx` (`panel_depth_id`),
  CONSTRAINT `fk_coat_cutting_pattern_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coat_cutting_pattern`
--

LOCK TABLES `coat_cutting_pattern` WRITE;
/*!40000 ALTER TABLE `coat_cutting_pattern` DISABLE KEYS */;
INSERT INTO `coat_cutting_pattern` VALUES (1,'place instructions here\'',3),(2,'place instructions here\'',3),(3,'place instructions here\'',3),(4,'place instructions here\'',3),(5,'place instructions here\'',3),(6,'place instructions here\'',5),(7,'place instructions here\'',5);
/*!40000 ALTER TABLE `coat_cutting_pattern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coat_cutting_pattern_output`
--

DROP TABLE IF EXISTS `coat_cutting_pattern_output`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coat_cutting_pattern_output` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `coat_cutting_pattern_id` int(11) NOT NULL,
  `coating_size_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_coat_cutting_pattern_output_coat_cutting_pattern1_idx` (`coat_cutting_pattern_id`),
  KEY `fk_coat_cutting_pattern_output_coating_size1_idx` (`coating_size_id`),
  CONSTRAINT `fk_coat_cutting_pattern_output_coat_cutting_pattern1` FOREIGN KEY (`coat_cutting_pattern_id`) REFERENCES `coat_cutting_pattern` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_coat_cutting_pattern_output_coating_size1` FOREIGN KEY (`coating_size_id`) REFERENCES `coating_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coat_cutting_pattern_output`
--

LOCK TABLES `coat_cutting_pattern_output` WRITE;
/*!40000 ALTER TABLE `coat_cutting_pattern_output` DISABLE KEYS */;
INSERT INTO `coat_cutting_pattern_output` VALUES (1,2,1,1),(2,1,1,2),(3,3,2,3),(4,3,3,4),(5,1,3,2),(6,5,4,2),(7,2,4,5),(8,6,5,6),(9,3,6,7),(10,3,7,8),(11,1,7,9);
/*!40000 ALTER TABLE `coat_cutting_pattern_output` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coat_cutting_sheet`
--

DROP TABLE IF EXISTS `coat_cutting_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coat_cutting_sheet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `coat_cutting_sheet_entry_id` int(11) NOT NULL,
  `panel_depth_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_coat_cutting_sheet_coat_cutting_sheet_entry1_idx` (`coat_cutting_sheet_entry_id`),
  KEY `fk_coat_cutting_sheet_panel_depth1_idx` (`panel_depth_id`),
  CONSTRAINT `fk_coat_cutting_sheet_coat_cutting_sheet_entry1` FOREIGN KEY (`coat_cutting_sheet_entry_id`) REFERENCES `coat_cutting_sheet_entry` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_coat_cutting_sheet_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coat_cutting_sheet`
--

LOCK TABLES `coat_cutting_sheet` WRITE;
/*!40000 ALTER TABLE `coat_cutting_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `coat_cutting_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coat_cutting_sheet_entry`
--

DROP TABLE IF EXISTS `coat_cutting_sheet_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coat_cutting_sheet_entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coat_cutting_sheet_entry`
--

LOCK TABLES `coat_cutting_sheet_entry` WRITE;
/*!40000 ALTER TABLE `coat_cutting_sheet_entry` DISABLE KEYS */;
/*!40000 ALTER TABLE `coat_cutting_sheet_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coat_cutting_sheet_instruction`
--

DROP TABLE IF EXISTS `coat_cutting_sheet_instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coat_cutting_sheet_instruction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `output_string` varchar(90) NOT NULL,
  `coat_cutting_sheet_id` int(11) NOT NULL,
  `coat_cutting_pattern_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_coat_cutting_pattern_instructions_coat_cutting_sheet1_idx` (`coat_cutting_sheet_id`),
  KEY `fk_coat_cutting_pattern_instructions_coat_cutting_pattern1_idx` (`coat_cutting_pattern_id`),
  CONSTRAINT `fk_coat_cutting_pattern_instructions_coat_cutting_pattern1` FOREIGN KEY (`coat_cutting_pattern_id`) REFERENCES `coat_cutting_pattern` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_coat_cutting_pattern_instructions_coat_cutting_sheet1` FOREIGN KEY (`coat_cutting_sheet_id`) REFERENCES `coat_cutting_sheet` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coat_cutting_sheet_instruction`
--

LOCK TABLES `coat_cutting_sheet_instruction` WRITE;
/*!40000 ALTER TABLE `coat_cutting_sheet_instruction` DISABLE KEYS */;
/*!40000 ALTER TABLE `coat_cutting_sheet_instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coating`
--

DROP TABLE IF EXISTS `coating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coating` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `description` (`description`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coating`
--

LOCK TABLES `coating` WRITE;
/*!40000 ALTER TABLE `coating` DISABLE KEYS */;
INSERT INTO `coating` VALUES (13,'Aquabord'),(14,'Artist Panel'),(15,'Artist Panel Basswood'),(16,'Artist Panel Smooth'),(17,'Claybord'),(18,'Encausticbord'),(19,'Gessobord'),(20,'Hardbord'),(21,'Natural Wood Panel'),(22,'Pastelbord'),(23,'Scratchbord');
/*!40000 ALTER TABLE `coating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coating_size`
--

DROP TABLE IF EXISTS `coating_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coating_size` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `length` decimal(10,5) NOT NULL,
  `width` decimal(10,5) NOT NULL,
  `unit_of_measurement` enum('in','cm') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coating_size`
--

LOCK TABLES `coating_size` WRITE;
/*!40000 ALTER TABLE `coating_size` DISABLE KEYS */;
INSERT INTO `coating_size` VALUES (1,49.25000,39.00000,'in'),(2,48.50000,18.00000,'in'),(3,48.50000,32.00000,'in'),(4,48.50000,25.88000,'in'),(5,24.00000,5.00000,'in'),(6,48.50000,15.75000,'in'),(7,49.25000,32.00000,'in'),(8,49.25000,25.88000,'in'),(9,49.25000,18.00000,'in');
/*!40000 ALTER TABLE `coating_size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cradle_depth`
--

DROP TABLE IF EXISTS `cradle_depth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cradle_depth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `measurement` decimal(10,5) NOT NULL,
  `unit_of_measurement` enum('in','cm','mm') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cradle_depth`
--

LOCK TABLES `cradle_depth` WRITE;
/*!40000 ALTER TABLE `cradle_depth` DISABLE KEYS */;
INSERT INTO `cradle_depth` VALUES (1,0.75000,'in'),(2,1.37500,'in'),(3,2.00000,'in'),(4,0.62500,'in'),(5,0.37500,'in');
/*!40000 ALTER TABLE `cradle_depth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cradle_width`
--

DROP TABLE IF EXISTS `cradle_width`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cradle_width` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `measurement` decimal(10,5) NOT NULL,
  `unit_of_measurement` enum('in','cm','mm') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cradle_width`
--

LOCK TABLES `cradle_width` WRITE;
/*!40000 ALTER TABLE `cradle_width` DISABLE KEYS */;
INSERT INTO `cradle_width` VALUES (1,0.75000,'in'),(2,0.50000,'in');
/*!40000 ALTER TABLE `cradle_width` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `finished_goods_inventory`
--

DROP TABLE IF EXISTS `finished_goods_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `finished_goods_inventory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `quantity` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `type` enum('Daily','Adjustment','Loss','Beginning of Period Inventory') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idinventory_UNIQUE` (`id`),
  KEY `fk_finished_goods_inventory_item1_idx` (`item_id`),
  CONSTRAINT `fk_finished_goods_inventory_item1` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finished_goods_inventory`
--

LOCK TABLES `finished_goods_inventory` WRITE;
/*!40000 ALTER TABLE `finished_goods_inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `finished_goods_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `framed_wip`
--

DROP TABLE IF EXISTS `framed_wip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `framed_wip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `retail_size_id` int(11) NOT NULL,
  `cradle_depth_id` int(11) NOT NULL,
  `type` enum('Daily','Adjustment','Loss','Beginning of Period Inventory') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_framed_wip_retail_size1_idx` (`retail_size_id`),
  KEY `fk_framed_wip_cradle_depth1_idx` (`cradle_depth_id`),
  CONSTRAINT `fk_framed_wip_cradle_depth1` FOREIGN KEY (`cradle_depth_id`) REFERENCES `cradle_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_framed_wip_retail_size1` FOREIGN KEY (`retail_size_id`) REFERENCES `retail_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `framed_wip`
--

LOCK TABLES `framed_wip` WRITE;
/*!40000 ALTER TABLE `framed_wip` DISABLE KEYS */;
/*!40000 ALTER TABLE `framed_wip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `glued_wip`
--

DROP TABLE IF EXISTS `glued_wip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `glued_wip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `retail_size_id` int(11) NOT NULL,
  `coating_id` int(11) NOT NULL,
  `cradle_depth_id` int(11) NOT NULL,
  `panel_depth_id` int(11) NOT NULL,
  `spray_color_id` int(11) DEFAULT NULL,
  `type` enum('Daily','Adjustment','Loss','Beginning of Period Inventory') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idglue_wip_UNIQUE` (`id`),
  KEY `fk_glued_wip_retail_size1_idx` (`retail_size_id`),
  KEY `fk_glued_wip_coating1_idx` (`coating_id`),
  KEY `fk_glued_wip_cradle_depth1_idx` (`cradle_depth_id`),
  KEY `fk_glued_wip_panel_depth1_idx` (`panel_depth_id`),
  KEY `fk_glued_wip_spray_color1_idx` (`spray_color_id`),
  CONSTRAINT `fk_glued_wip_coating1` FOREIGN KEY (`coating_id`) REFERENCES `coating` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_glued_wip_cradle_depth1` FOREIGN KEY (`cradle_depth_id`) REFERENCES `cradle_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_glued_wip_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_glued_wip_retail_size1` FOREIGN KEY (`retail_size_id`) REFERENCES `retail_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_glued_wip_spray_color1` FOREIGN KEY (`spray_color_id`) REFERENCES `spray_color` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `glued_wip`
--

LOCK TABLES `glued_wip` WRITE;
/*!40000 ALTER TABLE `glued_wip` DISABLE KEYS */;
/*!40000 ALTER TABLE `glued_wip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `graded_wip`
--

DROP TABLE IF EXISTS `graded_wip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `graded_wip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `coating_id` int(11) NOT NULL,
  `grade` varchar(8) DEFAULT NULL,
  `panel_depth_id` int(11) NOT NULL,
  `coating_size_id` int(11) NOT NULL,
  `type` enum('Daily','Adjustment','Loss','Beginning of Period Inventory') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_graded_wip_coating1_idx` (`coating_id`),
  KEY `fk_graded_wip_panel_depth1_idx` (`panel_depth_id`),
  KEY `fk_graded_wip_coating_size1_idx` (`coating_size_id`),
  CONSTRAINT `fk_graded_wip_coating1` FOREIGN KEY (`coating_id`) REFERENCES `coating` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_graded_wip_coating_size1` FOREIGN KEY (`coating_size_id`) REFERENCES `coating_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_graded_wip_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `graded_wip`
--

LOCK TABLES `graded_wip` WRITE;
/*!40000 ALTER TABLE `graded_wip` DISABLE KEYS */;
/*!40000 ALTER TABLE `graded_wip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ampersand_sku` varchar(45) NOT NULL,
  `description` longtext NOT NULL,
  `case_quantity` int(11) DEFAULT '1',
  `item_recipe_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ampersand_sku` (`ampersand_sku`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_item_item_recipe1_idx` (`item_recipe_id`),
  CONSTRAINT `fk_item_item_recipe1` FOREIGN KEY (`item_recipe_id`) REFERENCES `item_recipe` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1044 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (346,'100120808','(10)Claybord 8x8-1/8\"',10,1),(347,'100121114','(10) Claybord 11x14-1/8\"',10,2),(348,'200120808','(10)Gessobord 8x8 1/8\"',10,3),(349,'200120810','(10)Gessobord 8x10 1/8\"',10,4),(350,'200120912','(10)Gessobord 9x12 1/8\"',10,5),(351,'400120507','(10)Aquabord  5x7- 1/8\"',10,6),(352,'400120810','(10)Aquabord  8x10- 1/8\"',10,7),(353,'400121114','(10)Aquabord  11x14- 1/8\"',10,8),(354,'CBB055S','Scratchbord 5x5 Single',1,9),(355,'CBB066S','Scratchbord 6x6 Single',1,10),(356,'200871824','(5)Gessobord Cradled 7/8\"18x24',5,11),(357,'400871216','(5)Aquabord Cradled 7/8\" 12x16',5,12),(358,'910120810','(20)AP Primed Smooth 1/8\"-8x10',20,13),(359,'910121114','(10)AP Primed Smooth1/8\"-11x14',10,14),(360,'910121620','(10)AP Primed Smooth1/8\"-16x20',10,15),(361,'APC7540404','Cs(12-4PK) 3/4\"  ArtistP - 4x4',12,NULL),(362,'APC7560604','Cs(12-4PK) 3/4\"  ArtistP - 6x6',12,NULL),(363,'UPWP754603','Cs(12-3PK) 7/8\" Unprimed 4X6',12,NULL),(364,'UPWP755703','Cs(12-3PK) 7/8\" Unprimed 5X7',12,NULL),(365,'EN0404','Cs.(10-4Pk) 1/8\" Encaustic 4x4',10,NULL),(366,'EN055','Cs.(10-4Pk) 1/8\" Encaustic 5x5',10,NULL),(367,'EN057','Cs.(10-3Pk) 1/8\" Encaustic 5x7',10,NULL),(368,'EN0608','Cs.(10-3Pk) 1/8\" Encaustic 6x8',10,NULL),(369,'EN066','Cs.(10-4Pk) 1/8\" Encaustic 6x6',10,NULL),(370,'CBB05','Case(10-3Pk) 5x7 Scratchbord',10,NULL),(371,'CBB055','Case(10-3Pk) 5x5 Scratchbord',10,NULL),(372,'GBS044','Case (10-4Pk) 4x4 Gessobord',10,NULL),(373,'GBS05','Case (10-3Pk) 5x7 Gessobord',10,NULL),(374,'GBS055','Case (10-4Pk) 5x5 Gessobord',10,NULL),(375,'GBS0608','Case (10-3Pk) 6x8 Gessobord',10,NULL),(376,'GBS066','Case (10-4Pk) 6x6 Gessobord',10,NULL),(377,'HB05','Case(10-3Pk) 5x7 Hardbord',10,NULL),(378,'HB0608','Case(10-3Pk) 6x8 Hardbord',10,NULL),(379,'CBS044','Case (10-4Pk) 4x4 Claybord',10,NULL),(380,'CBS05','Case (10-3Pk) 5x7 Claybord',10,NULL),(381,'CBS055','Case (10-4Pk) 5x5 Claybord',10,NULL),(382,'CBS0608','Case (10-3Pk) 6x8 Claybord',10,NULL),(383,'CBS066','Case (10-4Pk) 6x6 Claybord',10,NULL),(384,'PB05','Case(10-3Pk) 5x7 Pastelbord',10,NULL),(385,'PBG05','Cs.(10-3Pk) 5x7 Pastelbord Grn',10,NULL),(386,'CBT044','Cs.(10-4Pk) 4x4 Aquabord',10,NULL),(387,'CBT05','Cs.(10-3Pk) 5x7 Aquabord',10,NULL),(388,'CBT055','Cs.(10-4Pk) 5x5 Aquabord',10,NULL),(389,'CBT066','Cs.(10-4Pk) 6x6 Aquabord',10,NULL),(390,'APS0404','Cs.(30) Smooth Artist Pnl: 4x4',30,45),(391,'APS0507','Cs.(30) Smooth Artist Pnl: 5x7',30,46),(392,'APS0606','Cs.(30) Smooth Artist Pnl: 6x6',30,47),(393,'APS0808','Cs.(30) Smooth Artist Pnl: 8x8',30,48),(394,'APS0810','Cs(36) Smooth Artist Pnl: 8x10',36,49),(395,'APS0912','Cs(20) Smooth Artist Pnl: 9x12',20,50),(396,'APS1010','Cs(20) Smooth ArtistPnl: 10x10',20,51),(397,'APS1114','Cs(20) Smooth ArtistPnl: 11x14',20,52),(398,'APS1212','Cs(20) Smooth ArtistPnl: 12x12',20,53),(399,'APS1216','Cs(24) Smooth ArtistPnl: 12x16',24,54),(400,'APS1418','Cs(12) Smooth ArtistPnl: 14x18',12,55),(401,'APS1620','Cs(20) Smooth ArtistPnl: 16x20',20,56),(402,'APS1824','Cs(16) Smooth ArtistPnl: 18x24',16,57),(403,'PBW0612','Cs(20) White Pastelbord - 6x12',20,58),(404,'PBW0618','Cs(20) White Pastelbord - 6x18',20,59),(405,'PBW066','Cs.(30) White Pastelbord - 6x6',30,60),(406,'PBW08','Cs.(36) WhitePastelbord - 8x10',36,61),(407,'PBW0808','Cs.(12) WhitePastelbord - 8x8',12,62),(408,'PBW09','Cs.(20) Pastelbord  White 9x12',20,63),(409,'PBW11','Cs.(20) Pastelbord White 11x14',20,64),(410,'PBW12','Cs.(12) Pastelbord White 12x16',12,65),(411,'PBW1212','Cs.(12) Pastelbord White 12x12',12,66),(412,'PBW16','Cs.(20) Pastelbord White 16x20',20,67),(413,'PBW18','Cs.(16) Pastelbord White 18x24',16,68),(414,'PBW2436','Cs.(8) Pastelbord White 24x36',8,69),(415,'GP05','Cs.(30) Gessoed Hardbd Pnl 5x7',30,70),(416,'GP08','Cs.(36)Gessoed Hardbd Pnl 8x10',36,71),(417,'GP09','Cs.(20)Gessoed Hardbd Pnl 9x12',20,72),(418,'GP1010','Cs(20)Gessoed Hardbd Pnl 10x10',20,73),(419,'GP11','Cs(20)Gessoed Hardbd Pnl 11x14',20,74),(420,'GP1212','Cs(20)Gessoed Hardbd Pnl 12x12',20,75),(421,'GP14','Cs(12)Gessoed Hardbd Pnl 14x18',12,76),(422,'GP18','Cs(16)Gessoed Hardbd Pnl 18x24',16,77),(423,'GP44','Cs(30) Gessoed Hardbd Pnl 4x4',30,78),(424,'GP66','Cs(30) Gessoed Hardbd Pnl 6x6',30,79),(425,'GP88','Cs(30) Gessoed Hardbd Pnl 8x8',30,80),(426,'WP150606','Cs(10) 6x6 1.5\" Wood Panel',10,81),(427,'WP150612','Cs(10) 6x12 1.5\" Wood Panel',10,82),(428,'WP150808','Cs(10) 8x8 1.5\" Wood Panel',10,83),(429,'WP150810','Cs(10) 8x10 1.5\" Wood Panel',10,84),(430,'WP150912','Cs(10) 9x12 1.5\" Wood Panel',10,85),(431,'WP151010','Cs(10) 10x10 1.5\" Wood Panel',10,86),(432,'WP151114','Cs(10) 11x14 1.5\" Wood Panel',10,87),(433,'WP151212','Cs(10) 12x12 1.5\" Wood Panel',10,88),(434,'WP151248','Cs(4) 12x48 1.5\" Wood Panel',4,89),(435,'WP151616','Cs(5) 16x16 1.5\" Wood Panel',5,90),(436,'WP151620','Cs(5) 16x20 1.5\" Wood Panel',5,91),(437,'WP151818','Cs(5) 18x18 1.5\" Wood Panel',5,92),(438,'WP151824','Cs(5) 18x24 1.5\" Wood Panel',5,93),(439,'WP152020','Cs(5) 20x20 1.5\" Wood Panel',5,94),(440,'WP152024','Cs(5) 20x24 1.5\" Wood Panel',5,95),(441,'WP152424','Cs(4) 24x24 1.5\" Wood Panel',4,96),(442,'WP152430','Cs(4) 24x30 1.5\" Wood Panel',4,97),(443,'WP152436','Cs(4) 24x36 1.5\" Wood Panel',4,98),(444,'WP153040','Cs(2) 30x40 1.5\" Wood Panel',2,99),(445,'WP153636','Cs(2) 36x36 1.5\" Wood Panel',2,100),(446,'WP153648','Cs(2) 36x48 1.5\" Wood Panel',2,101),(447,'WP750505','Cs(10) 5x5 7/8\" Wood Panel',10,102),(448,'WP750612','Cs(10) 6x12 7/8\" Wood Panel',10,103),(449,'WP750808','Cs(10) 8x8 7/8\" Wood Panel',10,104),(450,'WP750810','Cs(10) 8x10 7/8\" Wood Panel',10,105),(451,'WP750912','Cs(10) 9x12 7/8\" Wood Panel',10,106),(452,'WP751010','Cs(10) 10x10 7/8\" Wood Panel',10,107),(453,'WP751114','Cs(10) 11x14 7/8\" Wood Panel',10,108),(454,'WP751212','Cs(10) 12x12 7/8\" Wood Panel',10,109),(455,'WP751216','Cs(5) 12x16 7/8\" Wood Panel',5,110),(456,'WP751224','Cs(5) 12x24 7/8\" Wood Panel',5,111),(457,'WP751616','Cs(5) 16x16 7/8\" Wood Panel',5,112),(458,'WP751818','Cs(5) 18x18 7/8\" Wood Panel',5,113),(459,'WP751824','Cs(5) 18x24 7/8\" Wood Panel',5,114),(460,'PWP150404','Cs(10) 4x4 1.5\" Smooth Primed',10,115),(461,'PWP150505','Cs(10) 5x5 1.5\" Smooth Primed',10,116),(462,'PWP150507','Cs(10) 5x7 1.5\" Smooth Primed',10,117),(463,'PWP150606','Cs(10) 6x6 1.5\" Smooth Primed',10,118),(464,'PWP150612','Cs(10) 6x12 1.5\" Smooth Primed',10,119),(465,'PWP150808','Cs(10) 8x8 1.5\" Smooth Primed',10,120),(466,'PWP150810','Cs(10) 8x10 1.5\" Smooth Primed',10,121),(467,'PWP150912','Cs(10) 9x12 1.5\" Smooth Primed',10,122),(468,'PWP151010','Cs(10) 10x10 1.5\" Smooth Prime',10,123),(469,'PWP151114','Cs(10) 11x14 1.5\" Smooth Prime',10,124),(470,'PWP151212','Cs(10) 12x12 1.5\" Smooth Prime',10,125),(471,'PWP151216','Cs(5) 12x16 1.5\" Smooth Primed',5,126),(472,'PWP151616','Cs(5) 16x16 1.5\" Smooth Primed',5,127),(473,'PWP151620','Cs(5) 16x20 1.5\" Smooth Primed',5,128),(474,'PWP151824','Cs(5) 18x24 1.5\" Smooth Primed',5,129),(475,'PWP750404','Cs(10) 4x4 7/8\" Smooth Primed',10,130),(476,'PWP750406','Cs(10) 4x6 7/8\" Smooth Primed',10,131),(477,'PWP750505','Cs(10) 5x5 7/8\" Smooth Primed',10,132),(478,'PWP750507','Cs(10) 5x7 7/8\" Smooth Primed',10,133),(479,'PWP750606','Cs(10) 6x6 7/8\" Smooth Primed',10,134),(480,'PWP750612','Cs(10) 6x12 7/8\" Smooth Primed',10,135),(481,'PWP750808','Cs(10) 8x8 7/8\" Smooth Primed',10,136),(482,'PWP750810','Cs(10) 8x10 7/8\" Smooth Primed',10,137),(483,'PWP750912','Cs(10) 9x12 7/8\" Smooth Primed',10,138),(484,'PWP751010','Cs(10) 10x10 7/8\" Smooth Prime',10,139),(485,'PWP751114','Cs(10) 11x14 7/8\" Smooth Prime',10,140),(486,'PWP751212','Cs(10) 12x12 7/8\" Smooth Prime',10,141),(487,'PWP751216','Cs(5) 12x16 7/8\" Smooth Primed',5,142),(488,'PWP751616','Cs(5) 16x16 7/8\" Smooth Primed',5,143),(489,'PWP751620','Cs(5) 16x20 7/8\" Smooth Primed',5,144),(490,'PWP751824','Cs(5) 18x24 7/8\" Smooth Primed',5,145),(491,'UPP150606','Cs(10) 6x6 1.5\" Unprimed Panel',10,146),(492,'UPP150808','Cs(10) 8x8 1.5\" Unprimed Panel',10,147),(493,'UPP750606','Cs(10) 6x6 7/8\" Unprimed Panel',10,148),(494,'UPP750808','Cs(10) 8x8 7/8\" Unprimed Panel',10,149),(495,'UPWP150404','Cs(10) 4x4 1.5\" Unprimed Bass',10,150),(496,'UPWP150505','Cs(10) 5x5 1.5\" Unprimed Bass',10,151),(497,'UPWP150507','Cs(10) 5x7 1.5\" Unprimed Bass',10,152),(498,'UPWP150606','Cs(10) 6x6 1.5\" Unprimed Bass',10,153),(499,'UPWP150612','Cs(10) 6x12 1.5\" Unprimed Bass',10,154),(500,'UPWP150808','Cs(10) 8x8 1.5\" Unprimed Bass',10,155),(501,'UPWP150810','Cs(10) 8x10 1.5\" Unprimed Bass',10,156),(502,'UPWP150816','Cs(5) 8x16 1.5\" Unprimed Pine',5,157),(503,'UPWP150912','Cs(10) 9x12 1.5\" Unprimed Bass',10,158),(504,'UPWP151010','Cs(10) 10x10 1.5\" Unprime Bass',10,159),(505,'UPWP151020','Cs(5) 10x20 1.5\" UP Pine',5,160),(506,'UPWP151114','Cs(10) 11x14 1.5\" Unprime Bass',10,161),(507,'UPWP151212','Cs(10) 12x12 1.5\" Unprime Bass',10,162),(508,'UPWP151216','Cs(5) 12x16 1.5\" Unprimed Bass',5,163),(509,'UPWP151224','Cs(5) 12x24 1.5\" UP Pine',5,164),(510,'UPWP151236','Cs(4) 12x36 1.5\" UP Pine',4,165),(511,'UPWP151418','Cs(5) 14x18 1.5\" UP Pine',5,166),(512,'UPWP151616','Cs(5) 16x16 1.5\" Unprimed Bass',5,167),(513,'UPWP151620','Cs(5) 16x20 1.5\" Unprimed Bass',5,168),(514,'UPWP151818','Cs(5) 18x18 1.5\" Unprimed Bass',5,169),(515,'UPWP151824','Cs(5) 18x24 1.5\" Unprimed Bass',5,170),(516,'UPWP152020','Cs(5) 20x20 1.5\" Unprimed Bass',5,171),(517,'UPWP750404','Cs(10) 4x4 7/8\" Unprimed Bass',10,172),(518,'UPWP750406','Cs(10) 4x6 7/8\" Unprimed Bass',10,173),(519,'UPWP750505','Cs(10) 5x5 7/8\" Unprimed Bass',10,174),(520,'UPWP750507','Cs(10) 5x7 7/8\" Unprimed Bass',10,175),(521,'UPWP750606','Cs(10) 6x6 7/8\" Unprimed Bass',10,176),(522,'UPWP750612','Cs(10) 6x12 7/8\" Unprimed Bass',10,177),(523,'UPWP750808','Cs(10) 8x8 7/8\" Unprimed Bass',10,178),(524,'UPWP750810','Cs(10) 8x10 7/8\" Unprimed Bass',10,179),(525,'UPWP750912','Cs(10) 9x12 7/8\" Unprimed Bass',10,180),(526,'UPWP751010','Cs(10) 10x10 7/8\" Unprime Bass',10,181),(527,'UPWP751114','Cs(10) 11x14 7/8\" Unprime Bass',10,182),(528,'UPWP751212','Cs(10) 12x12 7/8\" Unprime Bass',10,183),(529,'UPWP751216','Cs(5) 12x16 7/8\" Unprimed Bass',5,184),(530,'UPWP751616','Cs(5) 16x16 7/8\" Unprimed Bass',5,185),(531,'UPWP751620','Cs(5) 16x20 7/8\" Unprimed Bass',5,186),(532,'UPWP751818','Cs(5) 18x18 7/8\" UP Pine',5,187),(533,'UPWP751824','Cs(5) 18x24 7/8\" Unprimed Bass',5,188),(534,'CBS08','Case (36) 8x10 Claybord',36,189),(535,'CBS088','Case (12) 8x8 Claybord',12,190),(536,'CBS09','Case (20) 9x12 Claybord',20,191),(537,'CBS1010','Case (12) 10x10 Claybord',12,192),(538,'CBS11','Case (20) 11x14 Claybord',20,193),(539,'CBS12','Case (12) 12x16 Claybord',12,194),(540,'CBS122','Case (12) Claybord 12x12',12,195),(541,'CBS12L','Case (12) 12 x 24 Claybord',12,196),(542,'CBS14','Case (12) 14x18 Claybord',12,197),(543,'CBS1616','Case (12) 16x16 Claybord',12,198),(544,'CBS18','Case (16) 18x24 Claybord',16,199),(545,'CBS18L','Case (6) 18 x 36 Claybord',6,200),(546,'CBS24','Case (8) 24x36 Claybord',8,201),(547,'CBSC055','Case (10) 5x5 Claybord Cradle',10,202),(548,'CBSC066','Case (10) 6x6 Claybord Cradle',10,203),(549,'CBSC08','Case (12) 8x10 Claybord Cradle',12,204),(550,'CBSC088','Case (10) 8x8 Claybord Cradle',10,205),(551,'CBSC09','Case (10) 9x12 Claybord Cradle',10,206),(552,'CBSC1010','Case (10)10x10 Claybord Cradle',10,207),(553,'CBSC11','Case(10) 11x14 Claybord Cradle',10,208),(554,'CBSC12','Case(10) 12x16 Claybord Cradle',10,209),(555,'CBSC122','Case(10) 12x12 Claybord Cradle',10,210),(556,'CBSC12L','Case (6) 12x24 Claybord Cradle',6,211),(557,'CBSC14','Case(10) 14x18 Claybord Cradle',10,212),(558,'CBSC16','Case (8) 16x20 Claybord Cradle',8,213),(559,'CBSC18','Case (8) 18x24 Claybord Cradle',8,214),(560,'CBSC24','Case (4) 24x36 Claybord Cradle',4,215),(561,'HB18','Case(16) 18x24 Hardbord',16,216),(562,'HB18L','Case(6) 18 x 36 Hardbord',6,217),(563,'HB24','Case(8) 24x36 Hardbord',8,218),(564,'HBC06','Case(10) 6x8 Hardbord Cradled',10,219),(565,'HBC0606','Case(10) 6x6 Hardbord Cradled',10,220),(566,'HBC08','Case(12) 8x10 Hardbord Cradled',12,221),(567,'HBC0808','Case(10) 8x8 Hardbord Cradled',10,222),(568,'HBC09','Case(10) 9x12 Hardbord Cradled',10,223),(569,'HBC11','Cs.(10) 11x14 Hardbord Cradled',10,224),(570,'HBC12','Cs.(10) 12x16 Hardbord Cradled',10,225),(571,'HBC12L','Cs.(6) 12x24 Hardbord Cradled',6,226),(572,'HBC14','Cs.(10) 14x18 Hardbord Cradled',10,227),(573,'HBC16','Cs.(8) 16x20 Hardbord Cradled',8,228),(574,'HBC18','Cs.(8) 18x24 Hardbord Cradled',8,229),(575,'HBC18L','Cs.(4) 18x36 Hardbord Cradled',4,230),(576,'GBS08','Case (36) 8x10 Gessobord',36,231),(577,'GBS088','Case (12) 8x8 Gessobord',12,232),(578,'GBS09','Case (20) 9x12 Gessobord',20,233),(579,'GBS1010','Case (12) 10x10 Gessobord',12,234),(580,'GBS11','Case (20) 11x14 Gessobord',20,235),(581,'GBS12','Case (12) 12x16 Gessobord',12,236),(582,'GBS122','Case (12) 12x12 Gessobord',12,237),(583,'GBS12L','Case (12) 12x24 Gessobord',12,238),(584,'GBS14','Case (12) 14x18 Gessobord',12,239),(585,'GBS16','Case (20) 16x20 Gessobord',20,240),(586,'GBS1616','Case (12) 16x16 Gessobord',12,241),(587,'GBS18','Case (16) 18x24 Gessobord',16,242),(588,'GBS18L','Case (6) 18x36 Gessobord',6,243),(589,'GBS24','Case (8) 24x36 Gessobord',8,244),(590,'GBSC055','Cs.(10) 5x5 Gessobord Cradled',10,245),(591,'GBSC066','Cs.(10) 6x6 Gessobord Cradled',10,246),(592,'GBSC08','Cs.(12) 8x10 Gessobord Cradled',12,247),(593,'GBSC088','Cs.(10) 8x8 Gessobord Cradled',10,248),(594,'GBSC09','Cs.(10) 9x12 Gessobord Cradled',10,249),(595,'GBSC1010','Cs.(10)10x10 Gessobord Cradled',10,250),(596,'GBSC11','Cs.(10) 11x14 GessobordCradled',10,251),(597,'GBSC12','Cs.(10) 12x16 GessobordCradled',10,252),(598,'GBSC122','Cs.(10) 12x12 GessobordCradled',10,253),(599,'GBSC12L','Cs.(6) 12x24 Gessobord Cradled',6,254),(600,'GBSC14','Cs.(10) 14x18 GessobordCradled',10,255),(601,'GBSC16','Cs.(8) 16x20 Gessobord Cradled',8,256),(602,'GBSC18','Cs.(8) 18x24 Gessobord Cradled',8,257),(603,'GBSC18L','Cs.(4) 18x36 Gessobord Cradled',4,258),(604,'GBSC24','Cs.(4) 24x36 Gessobord Cradled',4,259),(605,'HB12','Case(12) 12x16 Hardbord',12,260),(606,'HB122','Case(12) 12x12 Hardbord',12,261),(607,'HB12L','Case(12) 12x24 Hardbord',12,262),(608,'HB14','Case(12) 14x18 Hardbord',12,263),(609,'HB16','Case(20) 16x20 Hardbord',20,264),(610,'HB08','Case(36) 8x10 Hardbord',36,265),(611,'HB09','Case(20) 9x12 Hardbord',20,266),(612,'CBB08','Case (36) 8x10 Scratchbord',36,267),(613,'CBB088','Case (12) 8x8 Scratchbord',12,268),(614,'CBB12','Case (12) 12x16 Scratchbord',12,269),(615,'CBB122','Case (12) 12x12 Scratchbord',12,270),(616,'CBB14','Case (12) 14x18 Scratchbord',12,271),(617,'CBB16','Case (20) 16x20 Scratchbord',20,272),(618,'CBB18','Case (16) 18x24 Scratchbord',16,273),(619,'CBB24','Case (8) 24x36 Scratchbord',8,274),(620,'HB11','Case(20) 11 x 14 Hardbord',20,275),(621,'PBG08','Case(36) 8x10 Pastelbord Green',36,276),(622,'PBG11','Cs.(20) 11x14 Pastelbord Green',20,277),(623,'PBG16','Cs.(20) 16x20 Pastelbord Green',20,278),(624,'PBG18','Cs.(16) 18x24 Pastelbord Green',16,279),(625,'PBS08','Case(36) 8x10 Pastelbord Sand',36,280),(626,'PBS09','Cs.(20) 9x12 Pastelbord SAND',20,281),(627,'PBS11','Cs.(20) 11x14 Pastelbord Sand',20,282),(628,'PBS12','Case(12) 12x16 Pastelbord Sand',12,283),(629,'PBS1212','Cs.(12) 12x12 Pastelbord Sand',12,284),(630,'PBS16','Cs.(20) 16x20 Pastelbord Sand',20,285),(631,'PBS18','Case(16) 18x24 Pastelbord Sand',16,286),(632,'PBS2436','Cs.(8) 24x36 Pastelbord Sand',8,287),(633,'PB24','Case(8) 24x36 Pastelbord',8,288),(634,'CBT08','Cs.(36) 8x10 Aquabord',36,289),(635,'CBT088','Cs. (12) 8x8 Aquabord',12,290),(636,'CBT09','Cs.(20) 9x12 Aquabord',20,291),(637,'CBT11','Cs.(20) 11x14 Aquabord',20,292),(638,'CBT12','Cs.(12) 12x16 Aquabord',12,293),(639,'CBT122','Cs.(12) 12x12 Aquabord',12,294),(640,'CBT14','Cs.(12) 14x18 Aquabord',12,295),(641,'CBT16','Cs.(20) 16x20 Aquabord',20,296),(642,'CBT18','Cs.(16) 18x24 Aquabord',16,297),(643,'CBT22','Cs.(6) 22x30 Aquabord',6,298),(644,'CBT24','Cs.(8) 24x36 Aquabord',8,299),(645,'AP9M 044','Cs(10) 3/8\" Artist Panel - 4x4',10,300),(646,'AP9M 055','Cs(10) 3/8\" Artist Panel - 5x5',10,301),(647,'AP9M 088','Cs(10) 3/8\" Artist Panel - 8x8',10,302),(648,'AP9M 1010','Cs(10) 3/8\" Artist Panel-10x10',10,303),(649,'AP9M 1114','Cs(10) 3/8\" Artist Panel-11x14',10,304),(650,'AP9M 1216','Cs(5) 3/8\" Artist Panel-12x16',5,305),(651,'AP9M 122','Cs(10) 3/8\" Artist Panel-12x12',10,306),(652,'AP9M 1620','Cs(5) 3/8\" Artist Panel-16x20',5,307),(653,'AP9M 1824','Cs(5) 3/8\" Artist Panel-18x24',5,308),(654,'AP9M 612','Cs(5) 3/8\" Artist Panel - 6x12',5,309),(655,'AP9M 810','Cs(10) 3/8\" Artist Panel- 8x10',10,310),(656,'AP9M 912','Cs(10) 3/8\" Artist Panel- 9x12',10,311),(657,'APC.75 055','Cs(10) 3/4\" Crad ArtistP - 5x5',10,312),(658,'APC.75 066','Cs(10) 3/4\" Crad ArtistP - 6x6',10,313),(659,'APC.75 088','Cs(10) 3/4\" Crad ArtistP - 8x8',10,314),(660,'APC.75 1114','Cs(10) 3/4\" Crad ArtistP-11x14',10,315),(661,'APC.75 1216','Cs(5) 3/4\" Crad ArtistP- 12x16',5,316),(662,'APC.75 122','Cs(10) 3/4\" Crad ArtistP-12x12',10,317),(663,'APC.75 612','Cs(5) 3/4\" Crad ArtistP - 6x12',5,318),(664,'APC.75 810','Cs(10) 3/4\" Crad ArtistP- 8x10',10,319),(665,'APC.75 912','Cs(5) 3/4\" Crad ArtistP - 9x12',5,320),(666,'APC1.5 044','Cs(10) 1.5\" Crad ArtistP - 4x4',10,321),(667,'APC1.5 055','Cs(10) 1.5\" Crad ArtistP - 5x5',10,322),(668,'APC1.5 066','Cs(10) 1.5\" Crad ArtistP - 6x6',10,323),(669,'APC1.5 088','Cs(10) 1.5\" Crad ArtistP - 8x8',10,324),(670,'APC1.5 1010','Cs(5) 1.5\" Crad ArtistP- 10x10',5,325),(671,'APC1.5 1114','Cs(5) 1.5\" Crad ArtistP- 11x14',5,326),(672,'APC1.5 1216','Cs(5) 1.5\" Crad ArtistP- 12x16',5,327),(673,'APC1.5 122','Cs(5) 1.5\" Crad ArtistP- 12x12',5,328),(674,'APC1.5 1616','Cs(5) 1.5\" Crad ArtistP- 16x16',5,329),(675,'APC1.5 1620','Cs(5) 1.5\" Crad ArtistP- 16x20',5,330),(676,'APC1.5 1818','Cs(5) 1.5\" Crad ArtistP- 18x18',5,331),(677,'APC1.5 1824','Cs(5) 1.5\" Crad ArtistP- 18x24',5,332),(678,'APC1.5 612','Cs(5) 1.5\" Crad ArtistP - 6x12',5,333),(679,'APC1.5 810','Cs(10) 1.5\" Crad ArtistP- 8x10',10,334),(680,'APC1.5 912','Cs(5) 1.5\" Crad ArtistP - 9x12',5,335),(681,'ENC150612','Cs(5) 1.5\" Crad Encaustic 6x12',5,336),(682,'ENC150624','Cs(5) 1.5\" Crad Encaustic 6x24',5,337),(683,'ENC15066','Cs(5) 1.5\" Crad Encaustic 6x6',5,338),(684,'ENC150810','Cs(5) 1.5\" Crad Encaustic 8x10',5,339),(685,'ENC15088','Cs(5) 1.5\" Crad Encaustic 8x8',5,340),(686,'ENC150912','Cs(5) 1.5\" Crad Encaustic 9x12',5,341),(687,'ENC151010','Cs(5) 1.5\" Crad Encaust 10x10',5,342),(688,'ENC151114','Cs(5) 1.5\" Crad Encaust 11x14',5,343),(689,'ENC151212','Cs(5) 1.5\" Crad Encaust 12x12',5,344),(690,'ENC151216','Cs(5) 1.5\" Crad Encaust 12x16',5,345),(691,'ENC151616','Cs(5) 1.5\" Crad Encaust 16x16',5,346),(692,'ENC151620','Cs(5) 1.5\" Crad Encaust 16x20',5,347),(693,'ENC151818','Cs(5) 1.5\" Crad Encaust 18x18',5,348),(694,'ENC151824','Cs(5) 1.5\" Crad Encaust 18x24',5,349),(695,'ENC152424','Cs(5) 1.5\" Crad Encaust 24x24',5,350),(696,'ENC152436','Cs(2)1.5\" Crad Encaustic 24x36',2,351),(697,'ENC153030','Cs(2) 1.5\" Crad Encaust 30x30',2,352),(698,'ENC20612','Cs(4) 2\" Crad Encaustic 6x12',4,353),(699,'ENC20624','Cs(4) 2\" Crad Encaustic 6x24',4,354),(700,'ENC2066','Cs(4) 2\" Crad Encaustic 6x6',4,355),(701,'ENC20810','Cs(4) 2\" Crad Encaustic 8x10',4,356),(702,'ENC2088','Cs(4) 2\" Crad Encaustic 8x8',4,357),(703,'ENC21010','Cs(4) 2\" Crad Encaustic 10x10',4,358),(704,'ENC21114','Cs(4) 2\" Crad Encaustic 11x14',4,359),(705,'ENC21212','Cs(4) 2\" Crad Encaustic 12x12',4,360),(706,'ENC21216','Cs(4) 2\" Crad Encaustic 12x16',4,361),(707,'ENC21616','Cs(4) 2\" Crad Encaustic 16x16',4,362),(708,'ENC21620','Cs(4) 2\" Crad Encaustic 16x20',4,363),(709,'ENC21818','Cs(4) 2\" Crad Encaustic 18x18',4,364),(710,'ENC21824','Cs(4) 2\" Crad Encaustic 18x24',4,365),(711,'ENC22424','Cs(4) 2\" Crad Encaustic 24x24',4,366),(712,'ENC23030','Cs(2) 2\" Crad Encaustic 30x30',2,367),(713,'ENC23040','Cs(2) 2\" Crad Encaustic 30x40',2,368),(714,'ENC23636','Cs(2) 2\" Crad Encaustic 36x36',2,369),(715,'ENC23648','Cs(2) 2\" Crad Encaustic 36x48',2,370),(716,'ENC75055','Cs(10) 3/4\" Crad Encaustic 5x5',10,371),(717,'ENC75066','Cs(10) 3/4\" Crad Encaustic 6x6',10,372),(718,'ENC750810','Cs(5) 3/4\" Crad Encaustic 8x10',5,373),(719,'ENC75088','Cs(10) 3/4\" Crad Encaustic 8x8',10,374),(720,'ENC750912','Cs(5) 3/4\" Crad Encaustic 9x12',5,375),(721,'ENC751010','Cs(5) 3/4\" Crad Encaust 10x10',5,376),(722,'ENC751114','Cs(5) 3/4\" Crad Encaust 11x14',5,377),(723,'ENC751212','Cs(5) 3/4\" Crad Encaust 12x12',5,378),(724,'ENC751216','Cs(5) 3/4\" Crad Encaust 12x16',5,379),(725,'ENC751620','Cs(8) 3/4\" Crad Encaust 16x20',8,380),(726,'CBSCG0505','Cs(5) 1.5\" Crad Claybord 5x5',5,381),(727,'CBSCG0606','Cs(5) 1.5\" Crad Claybord 6x6',5,382),(728,'CBSCG0808','Cs(5) 1.5\" Crad Claybord 8x8',5,383),(729,'CBSCG0810','Cs(5) 1.5\" Crad Claybord 8x10',5,384),(730,'CBSCG0912','Cs(5) 1.5\" Crad Claybord 9x12',5,385),(731,'CBSCG1010','Cs(5) 1.5\" Crad Claybord 10x10',5,386),(732,'CBSCG1114','Cs(5) 1.5\" Crad Claybord 11x14',5,387),(733,'CBSCG1212','Cs(5) 1.5\" Crad Claybord 12x12',5,388),(734,'CBSCG1216','Cs(5) 1.5\" Crad Claybord 12x16',5,389),(735,'CBSCG1616','Cs(5) 1.5\" Crad Claybord 16x16',5,390),(736,'CBSCG1620','Cs(5) 1.5\" Crad Claybord 16x20',5,391),(737,'CBSCG1824','Cs(5) 1.5\" Crad Claybord 18x24',5,392),(738,'CBSCG2024','Cs(5) 1.5\" Crad Claybord 20X24',5,393),(739,'CBSCG2030','Cs(2) 1.5\" Crad Claybord 20x30',2,394),(740,'CBSCG2228','Cs(2) 1.5\" Crad Claybord 22x28',2,395),(741,'CBSCG2430','Cs(2) 1.5\" Crad Claybord 24x30',2,396),(742,'CBSCG2436','Cs(2) 1.5\" Crad Claybord 24x36',2,397),(743,'CBSCG3030','Cs(2) 1.5\" Crad Claybord 30x30',2,398),(744,'CBSWC05','Cs.(6) 2\" Cradled Claybord 5x5',6,399),(745,'CBSWC06','Cs.(4) 2\" Cradle Claybord 6x8',4,400),(746,'CBSWC066','Cs.(6) 2\"Cradle Claybord 6x6',6,401),(747,'CBSWC08','Cs.(4) 2\" Cradle Claybord 8x10',4,402),(748,'CBSWC088','Cs.(6) 2\" Cradle Claybord 8x8',6,403),(749,'CBSWC10','Cs.(4) 2\" CradleClaybord 10x10',4,404),(750,'CBSWC1020','Cs(4) 2\" Cradle Claybord 10x20',4,405),(751,'CBSWC1030','Cs(4) 2\" Cradle Claybord 10x30',4,406),(752,'CBSWC11','Cs(4) 2\" Cradle Claybord 11x14',4,407),(753,'CBSWC1216','Cs(4) 2\" Cradle Claybord 12x16',4,408),(754,'CBSWC122','Cs(4) 2\" Cradle Claybord 12x12',4,409),(755,'CBSWC1224','Cs(4) 2\" Cradle Claybord 12x24',4,410),(756,'CBSWC12L','Cs(4) 2\" Cradle Claybord 12x36',4,411),(757,'CBSWC16','Cs(4) 2\" Cradle Claybord 16x20',4,412),(758,'CBSWC1616','Cs(4) 2\" Cradle Claybord 16x16',4,413),(759,'CBSWC1824','Cs(4) 2\" Cradle Claybord 18x24',4,414),(760,'CBSWC2430','Cs(2) 2\" Cradle Claybord 24x30',2,415),(761,'CBSWC2436','Cs(2) 2\" Cradle Claybord 24x36',2,416),(762,'CBSWC244','Cs(4) 2\" Cradle Claybord 24x24',4,417),(763,'CBSWC30','Cs(2) 2\" Cradle Claybord 30x30',2,418),(764,'CBSWC3040','Cs(2) 2\" Cradle Claybord 30x40',2,419),(765,'CBSWC3636','Cs(2) 2\" Cradle Claybord 36x36',2,420),(766,'CBSWC3648','Cs(2) 2\" Cradle Claybord 36x48',2,421),(767,'CBSWC612','Cs(4) 2\" Cradle Claybord 6x12',4,422),(768,'CBSWC618','Cs(4) 2\" Cradle Claybord 6x18',4,423),(769,'CBSWC624','Cs(4) 2\" Cradle Claybord 6x24',4,424),(770,'CBSWC816','Cs(4) 2\" Cradle Claybord 8x16',4,425),(771,'CBSWC824','Cs(4) 2\" Cradle Claybord 8x24',4,426),(772,'CBSWC912','Cs(4) 2\" Cradle Claybord 9x12',4,427),(773,'HBWC06','Case(4) 2\" Cradle Hardbord 6x8',4,428),(774,'HBWC08','Cs.(4) 2\" Cradle Hardbord 8x10',4,429),(775,'HBWC09','Cs.(4) 2\" Cradle Hardbord 9x12',4,430),(776,'HBWC1010','Cs.(4)2\" Cradle Hardbord 10x10',4,431),(777,'HBWC11','Cs.(4) 2\" CradleHardbord 11x14',4,432),(778,'HBWC12','Cs.(4) 2\" CradleHardbord 12x16',4,433),(779,'HBWC122','Cs.(4) 2\" CradleHardbord 12x12',4,434),(780,'HBWC16','Cs.(4) 2\" CradleHardbord 16x20',4,435),(781,'HBWC1616','Cs.(4)2\" Cradle Hardbord 16x16',4,436),(782,'HBWC18','Cs.(4) 2\" CradleHardbord 18x24',4,437),(783,'HBWC2436','Cs.(2) 2\" CradleHardbord 24x36',2,438),(784,'HBWC244','Cs.(4) 2\" CradleHardbord 24x24',4,439),(785,'HBWC3030','Cs.(2) 2\" CradleHardbord 30x30',2,440),(786,'HBWC3040','Cs.(2) 2\" CradleHardbord 30x40',2,441),(787,'HBWC3636','Cs.(2) 2\" CradleHardbord 36x36',2,442),(788,'HBWC3648','Cs.(2) 2\" CradleHardbord 36x48',2,443),(789,'HBCG0606','Cs(5) 1.5\" Crad Hardbord 6x6',5,444),(790,'HBCG0808','Cs(5) 1.5\" Crad Hardbord 8x8',5,445),(791,'HBCG0810','Cs(5) 1.5\" Crad Hardbord 8x10',5,446),(792,'HBCG0912','Cs(5) 1.5\" Crad Hardbord 9x12',5,447),(793,'HBCG1114','Cs(5) 1.5\" Crad Hardbord 11x14',5,448),(794,'HBCG1212','Cs(5) 1.5\" Crad Hardbord 12x12',5,449),(795,'HBCG1216','Cs(5) 1.5\" Crad Hardbord 12x16',5,450),(796,'HBCG1616','Cs(5) 1.5\" Crad Hardbord 16x16',5,451),(797,'HBCG1620','Cs(5) 1.5\" Crad Hardbord 16x20',5,452),(798,'HBCG1824','Cs(5) 1.5\" Crad Hardbord 18x24',5,453),(799,'GBSCG0505','Cs(5) 1.5\" Crad Gessobord 5x5',5,454),(800,'GBSCG0606','Cs(5) 1.5\" Crad Gessobord 6x6',5,455),(801,'GBSCG0808','Cs(5) 1.5\" Crad Gessobord 8x8',5,456),(802,'GBSCG0810','Cs(5) 1.5\" Crad Gessobord 8x10',5,457),(803,'GBSCG0912','Cs(5) 1.5\" Crad Gessobord 9x12',5,458),(804,'GBSCG1010','Cs(5) 1.5\" Crad Gessobd 10x10',5,459),(805,'GBSCG1114','Cs(5) 1.5\" Crad Gessobd 11x14',5,460),(806,'GBSCG1212','Cs(5) 1.5\" Crad Gessobd 12x12',5,461),(807,'GBSCG1216','Cs(5) 1.5\" Crad Gessobd 12x16',5,462),(808,'GBSCG1616','Cs(5) 1.5\" Crad Gessobd 16x16',5,463),(809,'GBSCG1620','Cs(5) 1.5\" Crad Gessobd 16x20',5,464),(810,'GBSCG1824','Cs(5) 1.5\" Crad Gessobd 18x24',5,465),(811,'GBSCG2024','Cs(5)1.5\" Crad Gessobord 20x24',5,466),(812,'GBSCG2030','Cs(2) 1.5\" Crad Gessobd 20x30',2,467),(813,'GBSCG2424','Cs(5) 1.5\" Crad Gessobd 24x24',5,468),(814,'GBSCG2430','Cs(2)1.5\" Crad Gessobord 24x30',2,469),(815,'GBSCG2436','Cs(2) 1.5\" Crad Gessobd 24x36',2,470),(816,'GBSCG3030','Cs(2) 1.5\" Crad Gessobd 30x30',2,471),(817,'GBSCG3036','Cs(2) 1.5\" Crad Gessobd 30x36',2,472),(818,'GBWC05','Cs.(6) 2\" Cradle Gessobord 5x5',6,473),(819,'GBWC06','Cs.(4) 2\" Cradle Gesso 6x8',4,474),(820,'GBWC066','Cs.(6) 2\" Cradle Gessobord 6x6',6,475),(821,'GBWC08','Cs.(4) 2\" Cradle Gesso 8x10',4,476),(822,'GBWC088','Cs.(6) 2\" Cradle Gessobord 8x8',6,477),(823,'GBWC10','Cs.(4) 2\" Cradle Gesso 10x10',4,478),(824,'GBWC1020','Cs.(4) 2\" Cradle Gesso 10x20',4,479),(825,'GBWC1030','Cs.(4) 2\" Cradle Gesso 10x30',4,480),(826,'GBWC11','Cs.(4) 2\" Cradle Gesso 11x14',4,481),(827,'GBWC1216','Cs.(4) 2\" Cradle Gesso 12x16',4,482),(828,'GBWC122','Cs.(4) 2\" Cradle Gesso 12x12',4,483),(829,'GBWC1224','Cs.(4) 2\" Cradle Gesso 12x24',4,484),(830,'GBWC12L','Cs.(4) 2\" Cradle Gesso 12x36',4,485),(831,'GBWC16','Cs.(4) 2\" Cradle Gesso 16x20',4,486),(832,'GBWC1616','Cs.(4) 2\" Cradle Gesso 16x16',4,487),(833,'GBWC1824','Cs.(4) 2\" Cradle Gesso 18x24',4,488),(834,'GBWC2430','Cs.(2) 2\" Cradle Gesso 24x30',2,489),(835,'GBWC2436','Cs.(2) 2\" Cradle Gesso 24x36',2,490),(836,'GBWC244','Cs.(4) 2\" Cradle Gesso 24x24',4,491),(837,'GBWC30','Cs.(2) 2\" Cradle Gesso 30x30',2,492),(838,'GBWC3040','Cs.(2) 2\" Cradle Gesso 30x40',2,493),(839,'GBWC3636','Cs.(2) 2\" Cradle Gesso 36x36',2,494),(840,'GBWC3648','Cs.(2) 2\" Cradle Gesso 36x48',2,495),(841,'GBWC612','Cs.(4) 2\" Cradle Gesso 6x12',4,496),(842,'GBWC618','Cs.(4) 2\" Cradle Gesso 6x18',4,497),(843,'GBWC624','Cs.(4) 2\" Cradle Gesso 6x24',4,498),(844,'GBWC816','Cs.(4) 2\" Cradle Gesso 8x16',4,499),(845,'GBWC824','Cs.(4) 2\" Cradle Gesso 8x24',4,500),(846,'GBWC912','Cs.(4) 2\" Cradle Gesso 9x12',4,501),(847,'CBTC0606','Cs(10)3/4\" Crad Aquabord 6x6',10,502),(848,'CBTC0808','Cs(10)3/4\" Crad Aquabord 8x8',10,503),(849,'CBTC0810','Cs(12)3/4\" Crad Aquabord 8x10',12,504),(850,'CBTC1114','Cs(10)3/4\" Crad Aquabord 11x14',10,505),(851,'CBTC1212','Cs(10)3/4\" Crad Aquabord 12x12',10,506),(852,'CBTC1620','Cs(8)3/4\" Crad Aquabord 16x20',8,507),(853,'CBTC1824','Cs(8)3/4\" Crad Aquabord 18x24',8,508),(854,'CBTW11','Cs.(4) 2\" Cradle Aquabd 11x14',4,509),(855,'CBTW115','Cs.(4) 2\" Cradle Aquabd 11x15',4,510),(856,'CBTW122','Cs.(4) 2\" Aquabd Cradle 12x12',4,511),(857,'CBTW15','Cs.(4) 2\" Cradle Aquabd 15x22',4,512),(858,'CBTW16','Cs.(4) 2\" Cradle Aquabd 16x20',4,513),(859,'CBTW22','Cs.(2) 2\" Cradle Aquabd 22x30',2,514),(860,'EN0810','Cs.(10) 1/4\" Encaustic 8x10',10,515),(861,'EN088','Cs.(10) 1/4\" Encaustic 8x8',10,516),(862,'EN0912','Cs.(10) 1/4\" Encaustic 9x12',10,517),(863,'EN1010','Cs.(10) 1/4\" Encaustic 10x10',10,518),(864,'EN1114','Cs.(10) 1/4\" Encaustic 11x14',10,519),(865,'EN1212','Cs.(10) 1/4\" Encaustic 12x12',10,520),(866,'CBTG0606','Cs(5) 1.5\" Crad Aquabord 6x6',5,521),(867,'CBTG0808','Cs(5) 1.5\" Crad Aquabord 8x8',5,522),(868,'CBTG0810','Cs(5)1.5\" Crad Aquabord 8x10',5,523),(869,'CBTG1114','Cs(5) 1.5\" Crad Aquabord 11x14',5,524),(870,'CBTG1212','Cs(5) 1.5\" Crad Aquabord 12x12',5,525),(871,'CBTG1620','Cs(5) 1.5\" Crad Aquabord 16x20',5,526),(872,'CBTG1824','Cs(5) 1.5\" Crad Aquabord 18x24',5,527),(873,'CBTG2436','Cs(2) 1.5\" Crad Aquabord 24x36',2,528),(874,'CBTW055','Case(6) 2\" Cradle Aquabd 5x5',6,529),(875,'CBTW06','Case(4) 2\" Cradle Aquabd 6x8',4,530),(876,'CBTW066','Case(6) 2\" Cradle Aquabd 6x6',6,531),(877,'CBTW08','Case(4) 2\" Cradle Aquabd 8x10',4,532),(878,'CBTW088','Case(6) 2\" Cradle Aquabd 8x8',6,533),(879,'10015','Encausticbord 5x7 Single',1,534),(880,'50031318','(10)13x18 Pastelbord 3mm Grey',10,535),(881,'50031824','(10)18x24 Pastelbord 3mm Grey',10,536),(882,'50032020','(10)20x20 Pastelbord 3mm Grey',10,537),(883,'50032430','(10)24x30 Pastelbord 3mm Grey',10,538),(884,'50033040','(10)30x40 Pastelbord 3mm Grey',10,539),(885,'50034050','(10)40x50 Pastelbord 3mm Grey',10,540),(886,'51031318','(10) 13x18Pastelbord 3mm White',10,541),(887,'51031824','(10)18x24 Pastelbord 3mm White',10,542),(888,'51032020','(10)20x20 Pastelbord 3mm White',10,543),(889,'51032430','(10)24x30 Pastelbord 3mm White',10,544),(890,'51033040','(10)30x40 Pastelbord 3mm White',10,545),(891,'90031010','(20)10x10 AP PrimedSmooth 3mm',20,546),(892,'90031318','(20)13x18 AP PrimedSmooth 3mm',20,547),(893,'90031824','(20)18x24 AP PrimedSmooth 3mm',20,548),(894,'90032020','(20)20x20 AP PrimedSmooth 3mm',20,549),(895,'90032430','(10)24x30 AP PrimedSmooth 3mm',10,550),(896,'90033030','(10)30x30 AP PrimedSmooth 3mm',10,551),(897,'90034050','(10)40x50 AP PrimedSmooth 3mm',10,552),(898,'90034060','(10)40x60 AP PrimedSmooth 3mm',10,553),(899,'90035070','(5)50x70 AP PrimedSmooth 3mm',5,554),(900,'90221010','(10)10x10 AP PrimedSmooth2.2cm',10,555),(901,'90221824','(10)18x24 AP PrimedSmooth2.2cm',10,556),(902,'90222020','(10)20x20 AP PrimedSmooth2.2cm',10,557),(903,'90222030','(10)20x30 AP PrimedSmooth2.2cm',10,558),(904,'90222430','(10)24x30 AP PrimedSmooth2.2cm',10,559),(905,'90223030','(10)30x30 AP PrimedSmooth2.2cm',10,560),(906,'90223040','(5)30x40 AP PrimedSmooth2.2cm',5,561),(907,'90381824','(10)18x24 AP PrimedSmooth3.8cm',10,562),(908,'90382020','(10)20x20 AP PrimedSmooth3.8cm',10,563),(909,'90382030','(10)20x30 AP PrimedSmooth3.8cm',10,564),(910,'90382430','(10)24x30 AP PrimedSmooth3.8cm',10,565),(911,'90383030','(10)30x30 AP PrimedSmooth3.8cm',10,566),(912,'90383040','(5)30x40 AP PrimedSmooth3.8cm',5,567),(913,'90384040','(5)40x40 AP PrimedSmooth3.8cm',5,568),(914,'90384060','(5)40x60 AP PrimedSmooth3.8cm',5,569),(915,'80221010','Cs(10) 10x10 2.2cm Unprimed WP',10,570),(916,'80221824','Cs(10) 18x24 2.2cm Unprimed WP',10,571),(917,'80222020','Cs(10) 20x20 2.2cm Unprimed WP',10,572),(918,'80222030','Cs(10) 20x30 2.2cm Unprimed WP',10,573),(919,'80222430','Cs(10) 24x30 2.2cm Unprimed WP',10,574),(920,'80223030','Cs(10) 30x30 2.2cm Unprimed WP',10,575),(921,'80223040','Cs(5) 30x40 2.2cm Unprimed WP',5,576),(922,'80381824','Cs(10) 18x24 3.8cm Unprimed WP',10,577),(923,'80382020','Cs(10) 20x20 3.8cm Unprimed WP',10,578),(924,'80382030','Cs(10) 20x30 3.8cm Unprimed WP',10,579),(925,'80382430','Cs(10) 24x30 3.8cm Unprimed WP',10,580),(926,'80383030','Cs(10) 30x30 3.8cm Unprimed WP',10,581),(927,'80383040','Cs(5) 30x40 3.8cm Unprimed WP',5,582),(928,'80384040','Cs(5) 40x40 3.8cm Unprimed WP',5,583),(929,'80384060','Cs(5) 40x60 3.8cm Unprimed WP',5,584),(930,'70091010','(10)10x10 Canvas Texture 9mm',10,585),(931,'70091530','(10)15x30 Canvas Texture 9mm',10,586),(932,'70091824','(10)18x24 Canvas Texture 9mm',10,587),(933,'70092020','(10)20x20 Canvas Texture 9mm',10,588),(934,'70092030','(10)20x30 Canvas Texture 9mm',10,589),(935,'70092430','(10)24x30 Canvas Texture 9mm',10,590),(936,'70093030','(10)30x30 Canvas Texture 9mm',10,591),(937,'70093040','(5)30x40 Canvas Texture 9mm',5,592),(938,'70094050','(5)40x50 Canvas Texture 9mm',5,593),(939,'70094060','(5)40x60 Canvas Texture 9mm',5,594),(940,'70191530','(10)15x30 Canvas Texture 1.9cm',10,595),(941,'70191824','(10)18x24 Canvas Texture 1.9cm',10,596),(942,'70192020','(10)20x20 Canvas Texture 1.9cm',10,597),(943,'70192030','(10)20x30 Canvas Texture 1.9cm',10,598),(944,'70192430','(10)24x30 Canvas Texture 1.9cm',10,599),(945,'70193030','(10)30x30 Canvas Texture 1.9cm',10,600),(946,'70193040','(5)30x40 Canvas Texture 1.9cm',5,601),(947,'70381530','(10)15x30 Canvas Texture 3.8cm',10,602),(948,'70381824','(10)18x24 Canvas Texture 3.8cm',10,603),(949,'70382020','(10)20x20 Canvas Texture 3.8cm',10,604),(950,'70382030','(10)20x30 Canvas Texture 3.8cm',10,605),(951,'70382430','(5)24x30 Canvas Texture 3.8cm',5,606),(952,'70383030','(5)30x30 Canvas Texture 3.8cm',5,607),(953,'70383040','(5)30x40 Canvas Texture 3.8cm',5,608),(954,'70384040','(5)40x40 Canvas Texture 3.8cm',5,609),(955,'70384050','(5)40x50 Canvas Texture 3.8cm',5,610),(956,'70384060','(5)40x60 Canvas Texture 3.8cm',5,611),(957,'10031318','(10)13x18 Claybord 3mm',10,612),(958,'10032020','(10)20x20 Claybord 3mm',10,613),(959,'10032430','(10)24x30 Claybord 3mm',10,614),(960,'10033030','(10)30x30 Claybord 3mm',10,615),(961,'10033040','(10)30x40 Claybord 3mm',10,616),(962,'10034040','(10)40x40 Claybord 3mm',10,617),(963,'10034050','(10)40x50 Claybord 3mm',10,618),(964,'10034060','(10)40x60 Claybord 3mm',10,619),(965,'10035070','(5)50x70 Claybord 3mm',5,620),(966,'10222020','(10)20x20 Claybord 2.2cm',10,621),(967,'10222030','(10)20x30 Claybord 2.2cm',10,622),(968,'10222430','(5)24x30 Claybord 2.2cm',5,623),(969,'10223030','(5)30x30 Claybord 2.2cm',5,624),(970,'10223040','(5)30x40 Claybord 2.2cm',5,625),(971,'10224050','(5)40x50 Claybord 2.2cm',5,626),(972,'10225050','(5)50x50 Claybord 2.2cm',5,627),(973,'10225070','(2)50x70 Claybord 2.2cm',2,628),(974,'10382020','(10)20x20 Claybord 3.8cm',10,629),(975,'10382030','(10)20x30 Claybord 3.8cm',10,630),(976,'10382430','(5)24x30 Claybord 3.8cm',5,631),(977,'10383030','(5)30x30 Claybord 3.8cm',5,632),(978,'10383040','(5)30x40 Claybord 3.8cm',5,633),(979,'10384040','(5)40x40 Claybord 3.8cm',5,634),(980,'10384050','(5)40x50 Claybord 3.8cm',5,635),(981,'10384060','(5)40x60 Claybord 3.8cm',5,636),(982,'20031318','(10)13 x18 Gessobord 3mm',10,637),(983,'20031824','(10)18 x24 Gessobord 3mm',10,638),(984,'20032020','(10)20 x20 Gessobord 3mm',10,639),(985,'20032430','(10)24 x30 Gessobord 3mm',10,640),(986,'20033030','(10)30 x30 Gessobord 3mm',10,641),(987,'20033040','(10)30 x40 Gessobord 3mm',10,642),(988,'20034050','(10)40 x50 Gessobord 3mm',10,643),(989,'20034060','(10)40 x60 Gessobord 3mm',10,644),(990,'20035070','(5)50 x70 Gessobord 3mm',5,645),(991,'20221530','(10)15 x30 Gessobord 2.2cm',10,646),(992,'20222020','(10)20 x20 Gessobord 2.2cm',10,647),(993,'20222030','(10)20 x30 Gessobord 2.2cm',10,648),(994,'20222430','(5)24 x30 Gessobord 2.2cm',5,649),(995,'20223040','(5)30 x40 Gessobord 2.2cm',5,650),(996,'20224040','(5)40 x40 Gessobord 2.2cm',5,651),(997,'20224050','(5)40 x50 Gessobord 2.2cm',5,652),(998,'20224060','(5)40 x60 Gessobord 2.2cm',5,653),(999,'20225050','(5)50 x50 Gessobord 2.2cm',5,654),(1000,'20381530','(10)15 x30 Gessobord 3.8cm',10,655),(1001,'20382020','(10)20 x20 Gessobord 3.8cm',10,656),(1002,'20382030','(10)20 x30 Gessobord 3.8cm',10,657),(1003,'20382430','(5)24 x30 Gessobord 3.8cm',5,658),(1004,'20383040','(5)30 x40 Gessobord 3.8cm',5,659),(1005,'20384040','(5)40 x40 Gessobord 3.8cm',5,660),(1006,'20385050','(5)50 x50 Gessobord 3.8cm',5,661),(1007,'30031318','(10)13x18 Encausticbord 3mm',10,662),(1008,'30221530','(10)15x30 Encausticbord 2.2cm',10,663),(1009,'30222030','(10)20x30 Encausticbord 2.2cm',10,664),(1010,'30222430','(5)24x30 Encausticbord 2.2cm',5,665),(1011,'30223030','(5)30x30 Encausticbord 2.2cm',5,666),(1012,'30223040','(5)30x40 Encausticbord 2.2cm',5,667),(1013,'30224040','(5)40x40 Encausticbord 2.2cm',5,668),(1014,'30224050','(5)40x50 Encausticbord 2.2cm',5,669),(1015,'30381530','(10)15x30 Encausticbord 3.8cm',10,670),(1016,'30382030','(10)20x30 Encausticbord 3.8cm',10,671),(1017,'30382430','(5)24x30 Encausticbord 3.8cm',5,672),(1018,'30383040','(5)30x40 Encausticbord 3.8cm',5,673),(1019,'30384040','(5)40x40 Encausticbord 3.8cm',5,674),(1020,'30384060','(5)40x60 Encausticbord 3.8cm',5,675),(1021,'30385050','(5)50x50 Encausticbord 3.8cm',5,676),(1022,'30385070','(2)50x70 Encausticbord 3.8cm',2,677),(1023,'30631824','(10)18x24 Encausticbord 6.3mm',10,678),(1024,'30632020','(10)20x20 Encausticbord 6.3mm',10,679),(1025,'30632030','(10)20x30 Encausticbord 6.3mm',10,680),(1026,'30632430','(10)24x30 Encausticbord 6.3mm',10,681),(1027,'30633030','(5)30x30 Encausticbord 6.3mm',5,682),(1028,'40031318','(10)13x18 Aquabord 3mm',10,683),(1029,'40031824','(10)18x24 Aquabord 3mm',10,684),(1030,'40032020','(10)20x20 Aquabord 3mm',10,685),(1031,'40032430','(10)24x30 Aquabord 3mm',10,686),(1032,'40033040','(10)30x40 Aquabord 3mm',10,687),(1033,'40034050','(10)40x50 Aquabord 3mm',10,688),(1034,'40222030','(10)20x30 Aquabord 2.2cm',10,689),(1035,'40223030','(5)30x30 Aquabord 2.2cm',5,690),(1036,'40223040','(5)30x40 Aquabord 2.2cm',5,691),(1037,'40224050','(5)40x50 Aquabord 2.2cm',5,692),(1038,'60031318','(10)13 x 18  Scratchbord 3mm',10,693),(1039,'60031824','(10)18 x 24  Scratchbord 3mm',10,694),(1040,'60032020','(10)20 x 20  Scratchbord 3mm',10,695),(1041,'60032430','(10)24 x 30  Scratchbord 3mm',10,696),(1042,'60033040','(10)30 x 40  Scratchbord 3mm',10,697),(1043,'60034050','(10)40 x 50  Scratchbord 3mm',10,698);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item_recipe`
--

DROP TABLE IF EXISTS `item_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item_recipe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coating_id` int(11) NOT NULL,
  `cradle_depth_id` int(11) DEFAULT NULL,
  `panel_depth_id` int(11) NOT NULL,
  `retail_size_id` int(11) NOT NULL,
  `cradle_width_id` int(11) DEFAULT NULL,
  `spray_color_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `item_recipe_ea19a463` (`coating_id`),
  KEY `item_recipe_5bb2c1a6` (`cradle_depth_id`),
  KEY `item_recipe_33358c5d` (`panel_depth_id`),
  KEY `item_recipe_5f23a61c` (`retail_size_id`),
  KEY `fk_item_recipe_cradle_width1_idx` (`cradle_width_id`),
  KEY `fk_item_recipe_spray_color1_idx` (`spray_color_id`),
  CONSTRAINT `fk_item_recipe_cradle_width1` FOREIGN KEY (`cradle_width_id`) REFERENCES `cradle_width` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_item_recipe_spray_color1` FOREIGN KEY (`spray_color_id`) REFERENCES `spray_color` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `item_recipe_coating_id_536ccb924239efb9_fk_coating_id` FOREIGN KEY (`coating_id`) REFERENCES `coating` (`id`),
  CONSTRAINT `item_recipe_cradle_depth_id_1cfc8abb78274264_fk_cradle_depth_id` FOREIGN KEY (`cradle_depth_id`) REFERENCES `cradle_depth` (`id`),
  CONSTRAINT `item_recipe_panel_depth_id_35f8509853794b18_fk_panel_depth_id` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`),
  CONSTRAINT `item_recipe_retail_size_id_14d55430d78b67bb_fk_retail_size_id` FOREIGN KEY (`retail_size_id`) REFERENCES `retail_size` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=699 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_recipe`
--

LOCK TABLES `item_recipe` WRITE;
/*!40000 ALTER TABLE `item_recipe` DISABLE KEYS */;
INSERT INTO `item_recipe` VALUES (1,17,NULL,3,92,NULL,NULL),(2,17,NULL,3,85,NULL,NULL),(3,19,NULL,3,92,NULL,NULL),(4,19,NULL,3,61,NULL,NULL),(5,19,NULL,3,59,NULL,NULL),(6,13,NULL,3,82,NULL,NULL),(7,13,NULL,3,61,NULL,NULL),(8,13,NULL,3,85,NULL,NULL),(9,23,NULL,3,62,NULL,NULL),(10,23,NULL,3,53,NULL,NULL),(11,19,1,3,91,1,NULL),(12,13,1,3,84,1,NULL),(13,16,NULL,3,61,NULL,NULL),(14,16,NULL,3,85,NULL,NULL),(15,16,NULL,3,95,NULL,NULL),(16,14,4,3,65,2,NULL),(17,14,4,3,53,2,NULL),(18,15,1,3,75,1,NULL),(19,15,1,3,82,1,NULL),(20,18,NULL,3,65,NULL,NULL),(21,18,NULL,3,62,NULL,NULL),(22,18,NULL,3,82,NULL,NULL),(23,18,NULL,3,72,NULL,NULL),(24,18,NULL,3,53,NULL,NULL),(25,23,NULL,3,82,NULL,NULL),(26,23,NULL,3,62,NULL,NULL),(27,19,NULL,3,65,NULL,NULL),(28,19,NULL,3,82,NULL,NULL),(29,19,NULL,3,62,NULL,NULL),(30,19,NULL,3,72,NULL,NULL),(31,19,NULL,3,53,NULL,NULL),(32,20,NULL,3,82,NULL,NULL),(33,20,NULL,3,72,NULL,NULL),(34,17,NULL,3,65,NULL,NULL),(35,17,NULL,3,82,NULL,NULL),(36,17,NULL,3,62,NULL,NULL),(37,17,NULL,3,72,NULL,NULL),(38,17,NULL,3,53,NULL,NULL),(39,22,NULL,3,82,NULL,6),(40,22,NULL,3,82,NULL,7),(41,13,NULL,3,65,NULL,NULL),(42,13,NULL,3,82,NULL,NULL),(43,13,NULL,3,62,NULL,NULL),(44,13,NULL,3,53,NULL,NULL),(45,16,NULL,3,65,NULL,NULL),(46,16,NULL,3,82,NULL,NULL),(47,16,NULL,3,53,NULL,NULL),(48,16,NULL,3,92,NULL,NULL),(49,16,NULL,3,61,NULL,NULL),(50,16,NULL,3,59,NULL,NULL),(51,16,NULL,3,87,NULL,NULL),(52,16,NULL,3,85,NULL,NULL),(53,16,NULL,3,54,NULL,NULL),(54,16,NULL,3,84,NULL,NULL),(55,16,NULL,3,88,NULL,NULL),(56,16,NULL,3,95,NULL,NULL),(57,16,NULL,3,91,NULL,NULL),(58,22,NULL,3,66,NULL,5),(59,22,NULL,3,58,NULL,5),(60,22,NULL,3,53,NULL,5),(61,22,NULL,3,61,NULL,5),(62,22,NULL,3,92,NULL,5),(63,22,NULL,3,59,NULL,5),(64,22,NULL,3,85,NULL,5),(65,22,NULL,3,84,NULL,5),(66,22,NULL,3,54,NULL,5),(67,22,NULL,3,95,NULL,5),(68,22,NULL,3,91,NULL,5),(69,22,NULL,3,83,NULL,5),(70,19,NULL,3,82,NULL,NULL),(71,19,NULL,3,61,NULL,NULL),(72,19,NULL,3,59,NULL,NULL),(73,19,NULL,3,87,NULL,NULL),(74,19,NULL,3,85,NULL,NULL),(75,19,NULL,3,54,NULL,NULL),(76,19,NULL,3,88,NULL,NULL),(77,19,NULL,3,91,NULL,NULL),(78,19,NULL,3,65,NULL,NULL),(79,19,NULL,3,53,NULL,NULL),(80,19,NULL,3,92,NULL,NULL),(81,21,2,3,53,1,NULL),(82,21,2,3,66,1,NULL),(83,21,2,3,92,1,NULL),(84,21,2,3,61,1,NULL),(85,21,2,3,59,1,NULL),(86,21,2,3,87,1,NULL),(87,21,2,3,85,1,NULL),(88,21,2,3,54,1,NULL),(89,21,2,3,94,1,NULL),(90,21,2,3,52,1,NULL),(91,21,2,3,95,1,NULL),(92,21,2,3,93,1,NULL),(93,21,2,3,91,1,NULL),(94,21,2,3,76,1,NULL),(95,21,2,3,73,1,NULL),(96,21,2,3,68,1,NULL),(97,21,2,3,74,1,NULL),(98,21,2,3,83,1,NULL),(99,21,2,3,63,1,NULL),(100,21,2,3,69,1,NULL),(101,21,2,3,70,1,NULL),(102,21,1,3,62,1,NULL),(103,21,1,3,66,1,NULL),(104,21,1,3,92,1,NULL),(105,21,1,3,61,1,NULL),(106,21,1,3,59,1,NULL),(107,21,1,3,87,1,NULL),(108,21,1,3,85,1,NULL),(109,21,1,3,54,1,NULL),(110,21,1,3,84,1,NULL),(111,21,1,3,78,1,NULL),(112,21,1,3,52,1,NULL),(113,21,1,3,93,1,NULL),(114,21,1,3,91,1,NULL),(115,16,2,3,65,1,NULL),(116,16,2,3,62,1,NULL),(117,16,2,3,82,1,NULL),(118,16,2,3,53,1,NULL),(119,16,2,3,66,1,NULL),(120,16,2,3,92,1,NULL),(121,16,2,3,61,1,NULL),(122,16,2,3,59,1,NULL),(123,16,2,3,87,1,NULL),(124,16,2,3,85,1,NULL),(125,16,2,3,54,1,NULL),(126,16,2,3,84,1,NULL),(127,16,2,3,52,1,NULL),(128,16,2,3,95,1,NULL),(129,16,2,3,91,1,NULL),(130,16,1,3,65,1,NULL),(131,16,1,3,75,1,NULL),(132,16,1,3,62,1,NULL),(133,16,1,3,82,1,NULL),(134,16,1,3,53,1,NULL),(135,16,1,3,66,1,NULL),(136,16,1,3,92,1,NULL),(137,16,1,3,61,1,NULL),(138,16,1,3,59,1,NULL),(139,16,1,3,87,1,NULL),(140,16,1,3,85,1,NULL),(141,16,1,3,54,1,NULL),(142,16,1,3,84,1,NULL),(143,16,1,3,52,1,NULL),(144,16,1,3,95,1,NULL),(145,16,1,3,91,1,NULL),(146,15,2,3,53,1,NULL),(147,15,2,3,92,1,NULL),(148,15,4,3,53,2,NULL),(149,15,4,3,92,2,NULL),(150,15,2,3,65,1,NULL),(151,15,2,3,62,1,NULL),(152,15,2,3,82,1,NULL),(153,15,2,3,53,1,NULL),(154,15,2,3,66,1,NULL),(155,15,2,3,92,1,NULL),(156,15,2,3,61,1,NULL),(157,15,2,3,86,1,NULL),(158,15,2,3,59,1,NULL),(159,15,2,3,87,1,NULL),(160,15,2,3,81,1,NULL),(161,15,2,3,85,1,NULL),(162,15,2,3,54,1,NULL),(163,15,2,3,84,1,NULL),(164,15,2,3,78,1,NULL),(165,15,2,3,90,1,NULL),(166,15,2,3,88,1,NULL),(167,15,2,3,52,1,NULL),(168,15,2,3,95,1,NULL),(169,15,2,3,93,1,NULL),(170,15,2,3,91,1,NULL),(171,15,2,3,76,1,NULL),(172,15,1,3,65,1,NULL),(173,15,1,3,75,1,NULL),(174,15,1,3,62,1,NULL),(175,15,1,3,82,1,NULL),(176,15,1,3,53,1,NULL),(177,15,1,3,66,1,NULL),(178,15,1,3,92,1,NULL),(179,15,1,3,61,1,NULL),(180,15,1,3,59,1,NULL),(181,15,1,3,87,1,NULL),(182,15,1,3,85,1,NULL),(183,15,1,3,54,1,NULL),(184,15,1,3,84,1,NULL),(185,15,1,3,52,1,NULL),(186,15,1,3,95,1,NULL),(187,15,1,3,93,1,NULL),(188,15,1,3,91,1,NULL),(189,17,NULL,3,61,NULL,NULL),(190,17,NULL,3,92,NULL,NULL),(191,17,NULL,3,59,NULL,NULL),(192,17,NULL,3,87,NULL,NULL),(193,17,NULL,3,85,NULL,NULL),(194,17,NULL,3,84,NULL,NULL),(195,17,NULL,3,54,NULL,NULL),(196,17,NULL,3,78,NULL,NULL),(197,17,NULL,3,88,NULL,NULL),(198,17,NULL,3,52,NULL,NULL),(199,17,NULL,3,91,NULL,NULL),(200,17,NULL,3,64,NULL,NULL),(201,17,NULL,3,83,NULL,NULL),(202,17,1,3,62,1,NULL),(203,17,1,3,53,1,NULL),(204,17,1,3,61,1,NULL),(205,17,1,3,92,1,NULL),(206,17,1,3,59,1,NULL),(207,17,1,3,87,1,NULL),(208,17,1,3,85,1,NULL),(209,17,1,3,84,1,NULL),(210,17,1,3,54,1,NULL),(211,17,1,3,78,1,NULL),(212,17,1,3,88,1,NULL),(213,17,1,3,95,1,NULL),(214,17,1,3,91,1,NULL),(215,17,1,3,83,1,NULL),(216,20,NULL,3,91,NULL,NULL),(217,20,NULL,3,64,NULL,NULL),(218,20,NULL,3,83,NULL,NULL),(219,20,1,3,72,1,NULL),(220,20,1,3,53,1,NULL),(221,20,1,3,61,1,NULL),(222,20,1,3,92,1,NULL),(223,20,1,3,59,1,NULL),(224,20,1,3,85,1,NULL),(225,20,1,3,84,1,NULL),(226,20,1,3,78,1,NULL),(227,20,1,3,88,1,NULL),(228,20,1,3,95,1,NULL),(229,20,1,3,91,1,NULL),(230,20,1,3,64,1,NULL),(231,19,NULL,3,61,NULL,NULL),(232,19,NULL,3,92,NULL,NULL),(233,19,NULL,3,59,NULL,NULL),(234,19,NULL,3,87,NULL,NULL),(235,19,NULL,3,85,NULL,NULL),(236,19,NULL,3,84,NULL,NULL),(237,19,NULL,3,54,NULL,NULL),(238,19,NULL,3,78,NULL,NULL),(239,19,NULL,3,88,NULL,NULL),(240,19,NULL,3,95,NULL,NULL),(241,19,NULL,3,52,NULL,NULL),(242,19,NULL,3,91,NULL,NULL),(243,19,NULL,3,64,NULL,NULL),(244,19,NULL,3,83,NULL,NULL),(245,19,1,3,62,1,NULL),(246,19,1,3,53,1,NULL),(247,19,1,3,61,1,NULL),(248,19,1,3,92,1,NULL),(249,19,1,3,59,1,NULL),(250,19,1,3,87,1,NULL),(251,19,1,3,85,1,NULL),(252,19,1,3,84,1,NULL),(253,19,1,3,54,1,NULL),(254,19,1,3,78,1,NULL),(255,19,1,3,88,1,NULL),(256,19,1,3,95,1,NULL),(257,19,1,3,91,1,NULL),(258,19,1,3,64,1,NULL),(259,19,1,3,83,1,NULL),(260,20,NULL,3,84,NULL,NULL),(261,20,NULL,3,54,NULL,NULL),(262,20,NULL,3,78,NULL,NULL),(263,20,NULL,3,88,NULL,NULL),(264,20,NULL,3,95,NULL,NULL),(265,20,NULL,3,61,NULL,NULL),(266,20,NULL,3,59,NULL,NULL),(267,23,NULL,3,61,NULL,NULL),(268,23,NULL,3,92,NULL,NULL),(269,23,NULL,3,84,NULL,NULL),(270,23,NULL,3,54,NULL,NULL),(271,23,NULL,3,88,NULL,NULL),(272,23,NULL,3,95,NULL,NULL),(273,23,NULL,3,91,NULL,NULL),(274,23,NULL,3,83,NULL,NULL),(275,20,NULL,3,85,NULL,NULL),(276,22,NULL,3,61,NULL,7),(277,22,NULL,3,85,NULL,7),(278,22,NULL,3,95,NULL,7),(279,22,NULL,3,91,NULL,7),(280,22,NULL,3,61,NULL,8),(281,22,NULL,3,59,NULL,8),(282,22,NULL,3,85,NULL,8),(283,22,NULL,3,84,NULL,8),(284,22,NULL,3,54,NULL,8),(285,22,NULL,3,95,NULL,8),(286,22,NULL,3,91,NULL,8),(287,22,NULL,3,83,NULL,8),(288,22,NULL,3,83,NULL,6),(289,13,NULL,3,61,NULL,NULL),(290,13,NULL,3,92,NULL,NULL),(291,13,NULL,3,59,NULL,NULL),(292,13,NULL,3,85,NULL,NULL),(293,13,NULL,3,84,NULL,NULL),(294,13,NULL,3,54,NULL,NULL),(295,13,NULL,3,88,NULL,NULL),(296,13,NULL,3,95,NULL,NULL),(297,13,NULL,3,91,NULL,NULL),(298,13,NULL,3,56,NULL,NULL),(299,13,NULL,3,83,NULL,NULL),(300,14,NULL,4,65,NULL,NULL),(301,14,NULL,4,62,NULL,NULL),(302,14,NULL,4,92,NULL,NULL),(303,14,NULL,4,87,NULL,NULL),(304,14,NULL,4,85,NULL,NULL),(305,14,NULL,4,84,NULL,NULL),(306,14,NULL,4,54,NULL,NULL),(307,14,NULL,4,95,NULL,NULL),(308,14,NULL,4,91,NULL,NULL),(309,14,NULL,4,66,NULL,NULL),(310,14,NULL,4,61,NULL,NULL),(311,14,NULL,4,59,NULL,NULL),(312,14,4,3,62,1,NULL),(313,14,4,3,53,1,NULL),(314,14,4,3,92,1,NULL),(315,14,4,3,85,1,NULL),(316,14,4,3,84,1,NULL),(317,14,4,3,54,1,NULL),(318,14,4,3,66,1,NULL),(319,14,4,3,61,1,NULL),(320,14,4,3,59,1,NULL),(321,14,2,3,65,1,NULL),(322,14,2,3,62,1,NULL),(323,14,2,3,53,1,NULL),(324,14,2,3,92,1,NULL),(325,14,2,3,87,1,NULL),(326,14,2,3,85,1,NULL),(327,14,2,3,84,1,NULL),(328,14,2,3,54,1,NULL),(329,14,2,3,52,1,NULL),(330,14,2,3,95,1,NULL),(331,14,2,3,93,1,NULL),(332,14,2,3,91,1,NULL),(333,14,2,3,66,1,NULL),(334,14,2,3,61,1,NULL),(335,14,2,3,59,1,NULL),(336,18,2,3,66,1,NULL),(337,18,2,3,77,1,NULL),(338,18,2,3,53,1,NULL),(339,18,2,3,61,1,NULL),(340,18,2,3,92,1,NULL),(341,18,2,3,59,1,NULL),(342,18,2,3,87,1,NULL),(343,18,2,3,85,1,NULL),(344,18,2,3,54,1,NULL),(345,18,2,3,84,1,NULL),(346,18,2,3,52,1,NULL),(347,18,2,3,95,1,NULL),(348,18,2,3,93,1,NULL),(349,18,2,3,91,1,NULL),(350,18,2,3,68,1,NULL),(351,18,2,3,83,1,NULL),(352,18,2,3,80,1,NULL),(353,18,3,3,66,1,NULL),(354,18,3,3,77,1,NULL),(355,18,3,3,53,1,NULL),(356,18,3,3,61,1,NULL),(357,18,3,3,92,1,NULL),(358,18,3,3,87,1,NULL),(359,18,3,3,85,1,NULL),(360,18,3,3,54,1,NULL),(361,18,3,3,84,1,NULL),(362,18,3,3,52,1,NULL),(363,18,3,3,95,1,NULL),(364,18,3,3,93,1,NULL),(365,18,3,3,91,1,NULL),(366,18,3,3,68,1,NULL),(367,18,3,3,80,1,NULL),(368,18,3,3,63,1,NULL),(369,18,3,3,69,1,NULL),(370,18,3,3,70,1,NULL),(371,18,1,3,62,1,NULL),(372,18,1,3,53,1,NULL),(373,18,1,3,61,1,NULL),(374,18,1,3,92,1,NULL),(375,18,1,3,59,1,NULL),(376,18,1,3,87,1,NULL),(377,18,1,3,85,1,NULL),(378,18,1,3,54,1,NULL),(379,18,1,3,84,1,NULL),(380,18,1,3,95,1,NULL),(381,17,2,3,62,1,NULL),(382,17,2,3,53,1,NULL),(383,17,2,3,92,1,NULL),(384,17,2,3,61,1,NULL),(385,17,2,3,59,1,NULL),(386,17,2,3,87,1,NULL),(387,17,2,3,85,1,NULL),(388,17,2,3,54,1,NULL),(389,17,2,3,84,1,NULL),(390,17,2,3,52,1,NULL),(391,17,2,3,95,1,NULL),(392,17,2,3,91,1,NULL),(393,17,2,3,73,1,NULL),(394,17,2,3,71,1,NULL),(395,17,2,3,55,1,NULL),(396,17,2,3,74,1,NULL),(397,17,2,3,83,1,NULL),(398,17,2,3,80,1,NULL),(399,17,3,3,62,1,NULL),(400,17,3,3,72,1,NULL),(401,17,3,3,53,1,NULL),(402,17,3,3,61,1,NULL),(403,17,3,3,92,1,NULL),(404,17,3,3,87,1,NULL),(405,17,3,3,81,1,NULL),(406,17,3,3,89,1,NULL),(407,17,3,3,85,1,NULL),(408,17,3,3,84,1,NULL),(409,17,3,3,54,1,NULL),(410,17,3,3,78,1,NULL),(411,17,3,3,90,1,NULL),(412,17,3,3,95,1,NULL),(413,17,3,3,52,1,NULL),(414,17,3,3,91,1,NULL),(415,17,3,3,74,1,NULL),(416,17,3,3,83,1,NULL),(417,17,3,3,68,1,NULL),(418,17,3,3,80,1,NULL),(419,17,3,3,63,1,NULL),(420,17,3,3,69,1,NULL),(421,17,3,3,70,1,NULL),(422,17,3,3,66,1,NULL),(423,17,3,3,58,1,NULL),(424,17,3,3,77,1,NULL),(425,17,3,3,86,1,NULL),(426,17,3,3,57,1,NULL),(427,17,3,3,59,1,NULL),(428,20,3,3,72,1,NULL),(429,20,3,3,61,1,NULL),(430,20,3,3,59,1,NULL),(431,20,3,3,87,1,NULL),(432,20,3,3,85,1,NULL),(433,20,3,3,84,1,NULL),(434,20,3,3,54,1,NULL),(435,20,3,3,95,1,NULL),(436,20,3,3,52,1,NULL),(437,20,3,3,91,1,NULL),(438,20,3,3,83,1,NULL),(439,20,3,3,68,1,NULL),(440,20,3,3,80,1,NULL),(441,20,3,3,63,1,NULL),(442,20,3,3,69,1,NULL),(443,20,3,3,70,1,NULL),(444,20,2,3,53,1,NULL),(445,20,2,3,92,1,NULL),(446,20,2,3,61,1,NULL),(447,20,2,3,59,1,NULL),(448,20,2,3,85,1,NULL),(449,20,2,3,54,1,NULL),(450,20,2,3,84,1,NULL),(451,20,2,3,52,1,NULL),(452,20,2,3,95,1,NULL),(453,20,2,3,91,1,NULL),(454,19,2,3,62,1,NULL),(455,19,2,3,53,1,NULL),(456,19,2,3,92,1,NULL),(457,19,2,3,61,1,NULL),(458,19,2,3,59,1,NULL),(459,19,2,3,87,1,NULL),(460,19,2,3,85,1,NULL),(461,19,2,3,54,1,NULL),(462,19,2,3,84,1,NULL),(463,19,2,3,52,1,NULL),(464,19,2,3,95,1,NULL),(465,19,2,3,91,1,NULL),(466,19,2,3,73,1,NULL),(467,19,2,3,71,1,NULL),(468,19,2,3,68,1,NULL),(469,19,2,3,74,1,NULL),(470,19,2,3,83,1,NULL),(471,19,2,3,80,1,NULL),(472,19,2,3,60,1,NULL),(473,19,3,3,62,1,NULL),(474,19,3,3,72,1,NULL),(475,19,3,3,53,1,NULL),(476,19,3,3,61,1,NULL),(477,19,3,3,92,1,NULL),(478,19,3,3,87,1,NULL),(479,19,3,3,81,1,NULL),(480,19,3,3,89,1,NULL),(481,19,3,3,85,1,NULL),(482,19,3,3,84,1,NULL),(483,19,3,3,54,1,NULL),(484,19,3,3,78,1,NULL),(485,19,3,3,90,1,NULL),(486,19,3,3,95,1,NULL),(487,19,3,3,52,1,NULL),(488,19,3,3,91,1,NULL),(489,19,3,3,74,1,NULL),(490,19,3,3,83,1,NULL),(491,19,3,3,68,1,NULL),(492,19,3,3,80,1,NULL),(493,19,3,3,63,1,NULL),(494,19,3,3,69,1,NULL),(495,19,3,3,70,1,NULL),(496,19,3,3,66,1,NULL),(497,19,3,3,58,1,NULL),(498,19,3,3,77,1,NULL),(499,19,3,3,86,1,NULL),(500,19,3,3,57,1,NULL),(501,19,3,3,59,1,NULL),(502,13,1,3,53,1,NULL),(503,13,1,3,92,1,NULL),(504,13,1,3,61,1,NULL),(505,13,1,3,85,1,NULL),(506,13,1,3,54,1,NULL),(507,13,1,3,95,1,NULL),(508,13,1,3,91,1,NULL),(509,13,3,3,85,1,NULL),(510,13,3,3,67,1,NULL),(511,13,3,3,54,1,NULL),(512,13,3,3,79,1,NULL),(513,13,3,3,95,1,NULL),(514,13,3,3,56,1,NULL),(515,18,NULL,5,61,NULL,NULL),(516,18,NULL,5,92,NULL,NULL),(517,18,NULL,5,59,NULL,NULL),(518,18,NULL,5,87,NULL,NULL),(519,18,NULL,5,85,NULL,NULL),(520,18,NULL,5,54,NULL,NULL),(521,13,2,3,53,1,NULL),(522,13,2,3,92,1,NULL),(523,13,2,3,61,1,NULL),(524,13,2,3,85,1,NULL),(525,13,2,3,54,1,NULL),(526,13,2,3,95,1,NULL),(527,13,2,3,91,1,NULL),(528,13,2,3,83,1,NULL),(529,13,3,3,62,1,NULL),(530,13,3,3,72,1,NULL),(531,13,3,3,53,1,NULL),(532,13,3,3,61,1,NULL),(533,13,3,3,92,1,NULL),(534,18,NULL,3,106,NULL,NULL),(535,22,NULL,3,96,NULL,6),(536,22,NULL,3,99,NULL,6),(537,22,NULL,3,102,NULL,6),(538,22,NULL,3,110,NULL,6),(539,22,NULL,3,105,NULL,6),(540,22,NULL,3,108,NULL,6),(541,22,NULL,3,96,NULL,5),(542,22,NULL,3,99,NULL,5),(543,22,NULL,3,102,NULL,5),(544,22,NULL,3,110,NULL,5),(545,22,NULL,3,105,NULL,5),(546,16,NULL,3,100,NULL,NULL),(547,16,NULL,3,96,NULL,NULL),(548,16,NULL,3,99,NULL,NULL),(549,16,NULL,3,102,NULL,NULL),(550,16,NULL,3,110,NULL,NULL),(551,16,NULL,3,107,NULL,NULL),(552,16,NULL,3,108,NULL,NULL),(553,16,NULL,3,103,NULL,NULL),(554,16,NULL,3,97,NULL,NULL),(555,16,1,3,100,1,NULL),(556,16,1,3,99,1,NULL),(557,16,1,3,102,1,NULL),(558,16,1,3,101,1,NULL),(559,16,1,3,110,1,NULL),(560,16,1,3,107,1,NULL),(561,16,1,3,105,1,NULL),(562,16,2,3,99,1,NULL),(563,16,2,3,102,1,NULL),(564,16,2,3,101,1,NULL),(565,16,2,3,110,1,NULL),(566,16,2,3,107,1,NULL),(567,16,2,3,105,1,NULL),(568,16,2,3,109,1,NULL),(569,16,2,3,103,1,NULL),(570,15,1,3,100,1,NULL),(571,15,1,3,99,1,NULL),(572,15,1,3,102,1,NULL),(573,15,1,3,101,1,NULL),(574,15,1,3,110,1,NULL),(575,15,1,3,107,1,NULL),(576,15,1,3,105,1,NULL),(577,15,2,3,99,1,NULL),(578,15,2,3,102,1,NULL),(579,15,2,3,101,1,NULL),(580,15,2,3,110,1,NULL),(581,15,2,3,107,1,NULL),(582,15,2,3,105,1,NULL),(583,15,2,3,109,1,NULL),(584,15,2,3,103,1,NULL),(585,14,NULL,4,100,NULL,NULL),(586,14,NULL,4,98,NULL,NULL),(587,14,NULL,4,99,NULL,NULL),(588,14,NULL,4,102,NULL,NULL),(589,14,NULL,4,101,NULL,NULL),(590,14,NULL,4,110,NULL,NULL),(591,14,NULL,4,107,NULL,NULL),(592,14,NULL,4,105,NULL,NULL),(593,14,NULL,4,108,NULL,NULL),(594,14,NULL,4,103,NULL,NULL),(595,14,4,3,98,1,NULL),(596,14,4,3,99,1,NULL),(597,14,4,3,102,1,NULL),(598,14,4,3,101,1,NULL),(599,14,4,3,110,1,NULL),(600,14,4,3,107,1,NULL),(601,14,4,3,105,1,NULL),(602,14,2,3,98,1,NULL),(603,14,2,3,99,1,NULL),(604,14,2,3,102,1,NULL),(605,14,2,3,101,1,NULL),(606,14,2,3,110,1,NULL),(607,14,2,3,107,1,NULL),(608,14,2,3,105,1,NULL),(609,14,2,3,109,1,NULL),(610,14,2,3,108,1,NULL),(611,14,2,3,103,1,NULL),(612,17,NULL,3,96,NULL,NULL),(613,17,NULL,3,102,NULL,NULL),(614,17,NULL,3,110,NULL,NULL),(615,17,NULL,3,107,NULL,NULL),(616,17,NULL,3,105,NULL,NULL),(617,17,NULL,3,109,NULL,NULL),(618,17,NULL,3,108,NULL,NULL),(619,17,NULL,3,103,NULL,NULL),(620,17,NULL,3,97,NULL,NULL),(621,17,1,3,102,1,NULL),(622,17,1,3,101,1,NULL),(623,17,1,3,110,1,NULL),(624,17,1,3,107,1,NULL),(625,17,1,3,105,1,NULL),(626,17,1,3,108,1,NULL),(627,17,1,3,104,1,NULL),(628,17,1,3,97,1,NULL),(629,17,2,3,102,1,NULL),(630,17,2,3,101,1,NULL),(631,17,2,3,110,1,NULL),(632,17,2,3,107,1,NULL),(633,17,2,3,105,1,NULL),(634,17,2,3,109,1,NULL),(635,17,2,3,108,1,NULL),(636,17,2,3,103,1,NULL),(637,19,NULL,3,96,NULL,NULL),(638,19,NULL,3,99,NULL,NULL),(639,19,NULL,3,102,NULL,NULL),(640,19,NULL,3,110,NULL,NULL),(641,19,NULL,3,107,NULL,NULL),(642,19,NULL,3,105,NULL,NULL),(643,19,NULL,3,108,NULL,NULL),(644,19,NULL,3,103,NULL,NULL),(645,19,NULL,3,97,NULL,NULL),(646,19,1,3,98,1,NULL),(647,19,1,3,102,1,NULL),(648,19,1,3,101,1,NULL),(649,19,1,3,110,1,NULL),(650,19,1,3,105,1,NULL),(651,19,1,3,109,1,NULL),(652,19,1,3,108,1,NULL),(653,19,1,3,103,1,NULL),(654,19,1,3,104,1,NULL),(655,19,2,3,98,1,NULL),(656,19,2,3,102,1,NULL),(657,19,2,3,101,1,NULL),(658,19,2,3,110,1,NULL),(659,19,2,3,105,1,NULL),(660,19,2,3,109,1,NULL),(661,19,2,3,104,1,NULL),(662,18,NULL,3,96,NULL,NULL),(663,18,1,3,98,1,NULL),(664,18,1,3,101,1,NULL),(665,18,1,3,110,1,NULL),(666,18,1,3,107,1,NULL),(667,18,1,3,105,1,NULL),(668,18,1,3,109,1,NULL),(669,18,1,3,108,1,NULL),(670,18,2,3,98,1,NULL),(671,18,2,3,101,1,NULL),(672,18,2,3,110,1,NULL),(673,18,2,3,105,1,NULL),(674,18,2,3,109,1,NULL),(675,18,2,3,103,1,NULL),(676,18,2,3,104,1,NULL),(677,18,2,3,97,1,NULL),(678,18,NULL,5,99,NULL,NULL),(679,18,NULL,5,102,NULL,NULL),(680,18,NULL,5,101,NULL,NULL),(681,18,NULL,5,110,NULL,NULL),(682,18,NULL,5,107,NULL,NULL),(683,13,NULL,3,96,NULL,NULL),(684,13,NULL,3,99,NULL,NULL),(685,13,NULL,3,102,NULL,NULL),(686,13,NULL,3,110,NULL,NULL),(687,13,NULL,3,105,NULL,NULL),(688,13,NULL,3,108,NULL,NULL),(689,13,1,3,101,1,NULL),(690,13,1,3,107,1,NULL),(691,13,1,3,105,1,NULL),(692,13,1,3,108,1,NULL),(693,23,NULL,3,96,NULL,NULL),(694,23,NULL,3,99,NULL,NULL),(695,23,NULL,3,102,NULL,NULL),(696,23,NULL,3,110,NULL,NULL),(697,23,NULL,3,105,NULL,NULL),(698,23,NULL,3,108,NULL,NULL);
/*!40000 ALTER TABLE `item_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `invoice_number` int(11) NOT NULL,
  `PO_number` varchar(45) DEFAULT NULL,
  `promised_date` date NOT NULL,
  `order_date` date NOT NULL,
  `referral` varchar(45) DEFAULT NULL,
  `status` varchar(45) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `invoice_number` (`invoice_number`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `order_cb24373b` (`customer_id`),
  CONSTRAINT `order_customer_id_7c4cf14470c858e1_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` decimal(10,5) NOT NULL,
  `retail_amount` varchar(45) DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `order_item_82bfda79` (`item_id`),
  KEY `order_item_69dfcb07` (`order_id`),
  CONSTRAINT `order_item_item_id_1c302241ed3b8313_fk_item_id` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  CONSTRAINT `order_item_order_id_4e8f5875d6398d43_fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=556 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pack`
--

DROP TABLE IF EXISTS `pack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pack_quantity` int(11) NOT NULL DEFAULT '1',
  `item_recipe_id` int(11) DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_pack_item_recipe1_idx` (`item_recipe_id`),
  KEY `fk_pack_item1_idx` (`item_id`),
  CONSTRAINT `fk_pack_item1` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_pack_item_recipe1` FOREIGN KEY (`item_recipe_id`) REFERENCES `item_recipe` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pack`
--

LOCK TABLES `pack` WRITE;
/*!40000 ALTER TABLE `pack` DISABLE KEYS */;
INSERT INTO `pack` VALUES (1,4,16,361),(2,4,17,362),(3,3,18,363),(4,3,19,364),(5,4,20,365),(6,4,21,366),(7,3,22,367),(8,3,23,368),(9,4,24,369),(10,3,25,370),(11,3,26,371),(12,4,27,372),(13,3,28,373),(14,4,29,374),(15,3,30,375),(16,4,31,376),(17,3,32,377),(18,3,33,378),(19,4,34,379),(20,3,35,380),(21,4,36,381),(22,3,37,382),(23,4,38,383),(24,3,39,384),(25,3,40,385),(26,4,41,386),(27,3,42,387),(28,4,43,388),(29,4,44,389);
/*!40000 ALTER TABLE `pack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panel_depth`
--

DROP TABLE IF EXISTS `panel_depth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `panel_depth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `measurement` decimal(10,5) NOT NULL,
  `unit_of_measurement` enum('in','cm','mm') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panel_depth`
--

LOCK TABLES `panel_depth` WRITE;
/*!40000 ALTER TABLE `panel_depth` DISABLE KEYS */;
INSERT INTO `panel_depth` VALUES (3,0.12500,'in'),(4,0.37500,'in'),(5,0.25000,'in');
/*!40000 ALTER TABLE `panel_depth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_cut_wip`
--

DROP TABLE IF EXISTS `retail_cut_wip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_cut_wip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `is_cradled` tinyint(1) NOT NULL,
  `coating_id` int(11) NOT NULL,
  `retail_size_id` int(11) NOT NULL,
  `panel_depth_id` int(11) NOT NULL,
  `type` enum('Daily','Adjustment','Loss','Beginning of Period Inventory') NOT NULL,
  `retail_cutting_sheet_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_retail_cut_wip_coating1_idx` (`coating_id`),
  KEY `fk_retail_cut_wip_retail_size1_idx` (`retail_size_id`),
  KEY `fk_retail_cut_wip_panel_depth1_idx` (`panel_depth_id`),
  KEY `fk_retail_cut_wip_retail_cutting_sheet1_idx` (`retail_cutting_sheet_id`),
  CONSTRAINT `fk_retail_cut_wip_coating1` FOREIGN KEY (`coating_id`) REFERENCES `coating` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_retail_cut_wip_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_retail_cut_wip_retail_cutting_sheet1` FOREIGN KEY (`retail_cutting_sheet_id`) REFERENCES `retail_cutting_sheet` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_retail_cut_wip_retail_size1` FOREIGN KEY (`retail_size_id`) REFERENCES `retail_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_cut_wip`
--

LOCK TABLES `retail_cut_wip` WRITE;
/*!40000 ALTER TABLE `retail_cut_wip` DISABLE KEYS */;
/*!40000 ALTER TABLE `retail_cut_wip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_cutting_pattern`
--

DROP TABLE IF EXISTS `retail_cutting_pattern`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_cutting_pattern` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cutting_instructions` longtext,
  `is_for_cradle` tinyint(1) NOT NULL,
  `grade` varchar(8) DEFAULT NULL,
  `coating_size_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_retail_cutting_pattern_coating_size1_idx` (`coating_size_id`),
  CONSTRAINT `fk_retail_cutting_pattern_coating_size1` FOREIGN KEY (`coating_size_id`) REFERENCES `coating_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_cutting_pattern`
--

LOCK TABLES `retail_cutting_pattern` WRITE;
/*!40000 ALTER TABLE `retail_cutting_pattern` DISABLE KEYS */;
INSERT INTO `retail_cutting_pattern` VALUES (1,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'48',1),(2,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'36',1),(3,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'48',1),(4,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'48',1),(5,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'48',1),(6,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'48',1),(7,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'48',1),(8,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'36',1),(9,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'36',1),(10,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'30',1),(11,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'30',1),(12,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'30',1),(13,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'30',1),(14,'A47.5 I36 I12, A38.5 I36, A38.5 I12Q3',1,'30',1);
/*!40000 ALTER TABLE `retail_cutting_pattern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_cutting_pattern_output`
--

DROP TABLE IF EXISTS `retail_cutting_pattern_output`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_cutting_pattern_output` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) NOT NULL,
  `retail_cutting_pattern_id` int(11) NOT NULL,
  `retail_size_id` int(11) NOT NULL,
  `is_primary` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `retail_cutting_pattern_output_58407811` (`retail_cutting_pattern_id`),
  KEY `fk_retail_cutting_pattern_output_retail_size1_idx` (`retail_size_id`),
  CONSTRAINT `e873b35952bdcd62447c1188ce7d9109` FOREIGN KEY (`retail_cutting_pattern_id`) REFERENCES `retail_cutting_pattern` (`id`),
  CONSTRAINT `fk_retail_cutting_pattern_output_retail_size1` FOREIGN KEY (`retail_size_id`) REFERENCES `retail_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_cutting_pattern_output`
--

LOCK TABLES `retail_cutting_pattern_output` WRITE;
/*!40000 ALTER TABLE `retail_cutting_pattern_output` DISABLE KEYS */;
INSERT INTO `retail_cutting_pattern_output` VALUES (1,1,1,70,1),(2,1,2,69,1),(3,4,2,59,0),(4,1,3,69,1),(5,3,3,54,0),(6,1,4,69,1),(7,4,4,59,0),(8,1,5,69,1),(9,1,5,78,0),(10,1,5,54,0),(11,1,6,69,1),(12,1,6,90,0),(13,1,7,69,1),(14,1,7,78,0),(15,2,7,66,0),(16,1,8,69,1),(17,12,8,53,0),(18,1,9,69,1),(19,12,9,53,0),(20,1,10,60,1),(21,6,10,59,0),(22,1,11,60,1),(23,3,11,59,0),(24,3,11,59,0),(25,1,12,80,1),(26,6,12,59,0),(27,1,12,77,0),(28,1,13,80,1),(29,6,13,59,0),(30,4,13,53,0),(31,1,14,80,1),(32,6,14,59,0),(33,2,14,53,0);
/*!40000 ALTER TABLE `retail_cutting_pattern_output` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_cutting_sheet`
--

DROP TABLE IF EXISTS `retail_cutting_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_cutting_sheet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `int_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_cutting_sheet`
--

LOCK TABLES `retail_cutting_sheet` WRITE;
/*!40000 ALTER TABLE `retail_cutting_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `retail_cutting_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_cutting_sheet_entry`
--

DROP TABLE IF EXISTS `retail_cutting_sheet_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_cutting_sheet_entry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `is_cradled` tinyint(1) NOT NULL,
  `coating_id` int(11) NOT NULL,
  `panel_depth_id` int(11) NOT NULL,
  `retail_cutting_sheet_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_retail_cutting_sheet_entry_coating1_idx` (`coating_id`),
  KEY `fk_retail_cutting_sheet_entry_panel_depth1_idx` (`panel_depth_id`),
  KEY `fk_retail_cutting_sheet_entry_retail_cutting_sheet1_idx` (`retail_cutting_sheet_id`),
  CONSTRAINT `fk_retail_cutting_sheet_entry_coating1` FOREIGN KEY (`coating_id`) REFERENCES `coating` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_retail_cutting_sheet_entry_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_retail_cutting_sheet_entry_retail_cutting_sheet1` FOREIGN KEY (`retail_cutting_sheet_id`) REFERENCES `retail_cutting_sheet` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_cutting_sheet_entry`
--

LOCK TABLES `retail_cutting_sheet_entry` WRITE;
/*!40000 ALTER TABLE `retail_cutting_sheet_entry` DISABLE KEYS */;
/*!40000 ALTER TABLE `retail_cutting_sheet_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_cutting_sheet_instruction`
--

DROP TABLE IF EXISTS `retail_cutting_sheet_instruction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_cutting_sheet_instruction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `output_string` varchar(90) NOT NULL,
  `quantity` int(11) NOT NULL DEFAULT '1',
  `retail_cutting_sheet_entry_id` int(11) NOT NULL,
  `retail_cutting_pattern_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_retail_cutting_pattern_instructions_retail_cutting_sheet_idx` (`retail_cutting_sheet_entry_id`),
  KEY `fk_retail_cutting_pattern_instructions_retail_cutting_patte_idx` (`retail_cutting_pattern_id`),
  CONSTRAINT `fk_retail_cutting_pattern_instructions_retail_cutting_pattern1` FOREIGN KEY (`retail_cutting_pattern_id`) REFERENCES `retail_cutting_pattern` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_retail_cutting_pattern_instructions_retail_cutting_sheet_e1` FOREIGN KEY (`retail_cutting_sheet_entry_id`) REFERENCES `retail_cutting_sheet_entry` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_cutting_sheet_instruction`
--

LOCK TABLES `retail_cutting_sheet_instruction` WRITE;
/*!40000 ALTER TABLE `retail_cutting_sheet_instruction` DISABLE KEYS */;
/*!40000 ALTER TABLE `retail_cutting_sheet_instruction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retail_size`
--

DROP TABLE IF EXISTS `retail_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `retail_size` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `length` decimal(10,5) NOT NULL,
  `width` decimal(10,5) NOT NULL,
  `unit_of_measurement` enum('in','cm') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retail_size`
--

LOCK TABLES `retail_size` WRITE;
/*!40000 ALTER TABLE `retail_size` DISABLE KEYS */;
INSERT INTO `retail_size` VALUES (52,16.00000,16.00000,'in'),(53,6.00000,6.00000,'in'),(54,12.00000,12.00000,'in'),(55,28.00000,22.00000,'in'),(56,30.00000,22.00000,'in'),(57,24.00000,8.00000,'in'),(58,18.00000,6.00000,'in'),(59,12.00000,9.00000,'in'),(60,36.00000,30.00000,'in'),(61,10.00000,8.00000,'in'),(62,5.00000,5.00000,'in'),(63,40.00000,30.00000,'in'),(64,36.00000,18.00000,'in'),(65,4.00000,4.00000,'in'),(66,12.00000,6.00000,'in'),(67,15.00000,11.00000,'in'),(68,24.00000,24.00000,'in'),(69,36.00000,36.00000,'in'),(70,48.00000,36.00000,'in'),(71,30.00000,20.00000,'in'),(72,8.00000,6.00000,'in'),(73,24.00000,20.00000,'in'),(74,30.00000,24.00000,'in'),(75,6.00000,4.00000,'in'),(76,20.00000,20.00000,'in'),(77,24.00000,6.00000,'in'),(78,24.00000,12.00000,'in'),(79,22.00000,15.00000,'in'),(80,30.00000,30.00000,'in'),(81,20.00000,10.00000,'in'),(82,7.00000,5.00000,'in'),(83,36.00000,24.00000,'in'),(84,16.00000,12.00000,'in'),(85,14.00000,11.00000,'in'),(86,16.00000,8.00000,'in'),(87,10.00000,10.00000,'in'),(88,18.00000,14.00000,'in'),(89,30.00000,10.00000,'in'),(90,36.00000,12.00000,'in'),(91,24.00000,18.00000,'in'),(92,8.00000,8.00000,'in'),(93,18.00000,18.00000,'in'),(94,48.00000,12.00000,'in'),(95,20.00000,16.00000,'in'),(96,18.00000,13.00000,'cm'),(97,70.00000,50.00000,'cm'),(98,30.00000,15.00000,'cm'),(99,24.00000,18.00000,'cm'),(100,10.00000,10.00000,'cm'),(101,30.00000,20.00000,'cm'),(102,20.00000,20.00000,'cm'),(103,60.00000,40.00000,'cm'),(104,50.00000,50.00000,'cm'),(105,40.00000,30.00000,'cm'),(106,7.00000,5.00000,'cm'),(107,30.00000,30.00000,'cm'),(108,50.00000,40.00000,'cm'),(109,40.00000,40.00000,'cm'),(110,30.00000,24.00000,'cm');
/*!40000 ALTER TABLE `retail_size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spray_color`
--

DROP TABLE IF EXISTS `spray_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spray_color` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `color` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `option` (`color`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spray_color`
--

LOCK TABLES `spray_color` WRITE;
/*!40000 ALTER TABLE `spray_color` DISABLE KEYS */;
INSERT INTO `spray_color` VALUES (6,'gray'),(7,'green'),(8,'sand'),(5,'white');
/*!40000 ALTER TABLE `spray_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sprayed_wip`
--

DROP TABLE IF EXISTS `sprayed_wip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sprayed_wip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `retail_size_id` int(11) NOT NULL,
  `panel_depth_id` int(11) NOT NULL,
  `spray_color_id` int(11) NOT NULL,
  `type` enum('Daily','Adjustment','Loss','Beginning of Period Inventory') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_sprayed_wip_retail_size1_idx` (`retail_size_id`),
  KEY `fk_sprayed_wip_panel_depth1_idx` (`panel_depth_id`),
  KEY `fk_sprayed_wip_spray_color1_idx` (`spray_color_id`),
  CONSTRAINT `fk_sprayed_wip_panel_depth1` FOREIGN KEY (`panel_depth_id`) REFERENCES `panel_depth` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_sprayed_wip_retail_size1` FOREIGN KEY (`retail_size_id`) REFERENCES `retail_size` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_sprayed_wip_spray_color1` FOREIGN KEY (`spray_color_id`) REFERENCES `spray_color` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sprayed_wip`
--

LOCK TABLES `sprayed_wip` WRITE;
/*!40000 ALTER TABLE `sprayed_wip` DISABLE KEYS */;
/*!40000 ALTER TABLE `sprayed_wip` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-11 11:23:31
