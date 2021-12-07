#create database quizdb ;
use quizdb;
CREATE TABLE IF NOT EXISTS `qpaper` (
  `qpid` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `userno` int(11) NOT NULL DEFAULT 0,
  `quesid` int(11) unsigned NOT NULL DEFAULT 0 COMMENT 'question paper collection id',
  `qpdate` datetime NOT NULL DEFAULT current_timestamp(),
  `qusid` int(11) unsigned NOT NULL,
  `question` text NOT NULL,
  `opt1` text NOT NULL,
  `opt2` text NOT NULL,
  `opt3` text NOT NULL,
  `opt4` text NOT NULL,
  `ansrep` text NOT NULL  COMMENT 'ans selected',
  `qstart` timestamp NULL DEFAULT NULL,
  `qend` timestamp NULL DEFAULT NULL,
  `marks` tinyint(4) NOT NULL DEFAULT 0,
  `status` enum('Y','N') NOT NULL DEFAULT 'N',
  PRIMARY KEY (`qpid`) USING BTREE,
  UNIQUE KEY `u_usrdt` (`userno`,`qpdate`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Random question selected from the question pool';

-- Data exporting was unselected.

-- Dumping structure for table quizdb.questions
CREATE TABLE IF NOT EXISTS `questions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `catagory` tinytext NOT NULL  COMMENT 'question catagory',
  `question` text NOT NULL,
  `answerok` text NOT NULL,
  `ansopt1` text DEFAULT NULL,
  `ansopt2` text DEFAULT NULL,
  `ansopt3` text DEFAULT NULL,
  `ansopt4` text DEFAULT NULL,
  `ansopt5` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ID_question` (`question`(20)) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8206 DEFAULT CHARSET=utf8mb3 COMMENT='Question table with first correct and 5 options';

-- Data exporting was unselected.

-- Dumping structure for table quizdb.users
CREATE TABLE IF NOT EXISTS `users` (
  `userno` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `usruid` varchar(16) NOT NULL,
  `pword` varchar(10) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `gender` enum('M','F') DEFAULT 'M',
  `role` enum('U','A') DEFAULT 'U',
  PRIMARY KEY (`userno`),
  UNIQUE KEY `UC_user` (`usruid`,`role`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COMMENT='USER table with role defined';