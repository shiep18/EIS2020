-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2020 年 06 月 15 日 08:44
-- 服务器版本: 5.5.20
-- PHP 版本: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `basketball`
--

-- --------------------------------------------------------

--
-- 表的结构 `basketball`
--

CREATE TABLE IF NOT EXISTS `basketball` (
  `grade` int(111) NOT NULL,
  `class` int(111) NOT NULL,
  `number` int(111) NOT NULL,
  `name` varchar(12) NOT NULL,
  `borrow_count` int(11) NOT NULL,
  `pic` longblob NOT NULL,
  `rest` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `basketball`
--

INSERT INTO `basketball` (`grade`, `class`, `number`, `name`, `borrow_count`, `pic`, `rest`) VALUES
(2017, 72, 1589, 'wzy', 0, 0x30, 15);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
