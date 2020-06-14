-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2020 年 06 月 14 日 13:36
-- 服务器版本: 5.5.20
-- PHP 版本: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `library`
--

-- --------------------------------------------------------

--
-- 表的结构 `books`
--

CREATE TABLE IF NOT EXISTS `books` (
  `bookname` varchar(26) CHARACTER SET utf8 NOT NULL,
  `place` varchar(26) CHARACTER SET utf8 NOT NULL,
  `state1` int(1) NOT NULL,
  `state2` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `books`
--

INSERT INTO `books` (`bookname`, `place`, `state1`, `state2`) VALUES
('红楼梦', '01-01-01', 1, 1),
('三国演义', '01-01-02', 0, 1),
('老人与海', '01-01-01', 1, 1),
('水浒传', '01-01-02', 1, 0),
('活着', '02-01-01', 1, 0),
('高等数学', '02-01-01', 0, 1),
('西游记', '01-01-03', 1, 1),
('大学物理', '03-03-03', 0, 1),
('汤家凤1800', '03-01-01', 1, 1),
('红楼梦', '01-01-01', 1, 1),
('三国演义', '01-01-02', 0, 1),
('老人与海', '01-01-01', 1, 1),
('水浒传', '01-01-02', 1, 0),
('活着', '02-01-01', 1, 0),
('高等数学', '02-01-01', 0, 1),
('西游记', '01-01-03', 1, 1),
('大学物理', '03-03-03', 0, 1),
('汤家凤1800', '03-01-01', 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `borrowed_books`
--

CREATE TABLE IF NOT EXISTS `borrowed_books` (
  `bookname` varchar(26) CHARACTER SET utf8 NOT NULL,
  `borrower` varchar(26) CHARACTER SET utf8 NOT NULL,
  `state1` int(1) NOT NULL,
  `state2` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `borrowed_books`
--

INSERT INTO `borrowed_books` (`bookname`, `borrower`, `state1`, `state2`) VALUES
('三国演义', 'test', 0, 1),
('高等数学', 'test', 0, 1),
('大学物理', 'test', 0, 1),
('三国演义', 'test', 0, 1),
('高等数学', 'test', 0, 1),
('大学物理', 'test', 0, 1);

-- --------------------------------------------------------

--
-- 表的结构 `lost_books`
--

CREATE TABLE IF NOT EXISTS `lost_books` (
  `bookname` varchar(26) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `lost_books`
--

INSERT INTO `lost_books` (`bookname`) VALUES
('水浒传'),
('活着'),
('水浒传'),
('活着');

-- --------------------------------------------------------

--
-- 表的结构 `manage`
--

CREATE TABLE IF NOT EXISTS `manage` (
  `password` varchar(32) NOT NULL COMMENT '密码'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `manage`
--

INSERT INTO `manage` (`password`) VALUES
('12345678'),
('12345678');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `number` varchar(26) NOT NULL,
  `name` varchar(26) CHARACTER SET utf8 NOT NULL,
  `password` varchar(26) NOT NULL,
  `borrowlimit` int(26) NOT NULL DEFAULT '3'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`number`, `name`, `password`, `borrowlimit`) VALUES
('20171587', '王宇斌', '123456', 3),
('20171542', '贾帅杰', '111111', 3),
('1', 'test', '1', 3),
('1111', 'aaa', '111111', 3),
('20171587', '王宇斌', '123456', 3),
('20171542', '贾帅杰', '111111', 3),
('1', 'test', '1', 3),
('1111', 'aaa', '111111', 3);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
