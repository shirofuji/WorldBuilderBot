-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 10, 2021 at 01:44 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `worldbuilderbot`
--
CREATE DATABASE IF NOT EXISTS `worldbuilderbot` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `worldbuilderbot`;

-- --------------------------------------------------------

--
-- Table structure for table `active_army`
--

CREATE TABLE `active_army` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) NOT NULL,
  `user_identifier` varchar(255) NOT NULL,
  `realm_identifier` varchar(255) NOT NULL,
  `army_identifier` varchar(255) NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `active_army`
--

INSERT INTO `active_army` (`id`, `guild_identifier`, `user_identifier`, `realm_identifier`, `army_identifier`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'Realm2', 'ARMY1', '2021-09-09 11:57:51', '2021-09-09 11:59:52'),
(2, '885106671427387392', '797279085889585214', 'realm1', 'army1', '2021-09-09 20:42:50', '2021-09-09 21:02:48'),
(3, '885106671427387392', '657695605367504906', 'Khitai', 'batallion', '2021-09-09 20:56:26', '2021-09-10 08:52:31'),
(4, '885106671427387392', '657695605367504906', 'RealmMuffin', 'ArmyM1', '2021-09-10 00:42:52', '2021-09-10 00:42:52'),
(5, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', '2021-09-10 07:33:45', '2021-09-10 07:54:25'),
(6, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', '2021-09-10 07:44:32', '2021-09-10 07:59:10'),
(7, '885106671427387392', '630629857348288512', 'apotheosis', 'edu_diaspora', '2021-09-10 12:01:19', '2021-09-10 12:01:19'),
(8, '885106671427387392', '797279085889585214', 'myRealm', 'myarmy', '2021-09-10 12:03:43', '2021-09-10 12:03:43'),
(9, '885106671427387392', '531176133744525313', 'marigold_round', 'knights_horse', '2021-09-10 12:31:29', '2021-09-10 12:31:29'),
(10, '885106671427387392', '790160755344277505', 'Anokis', 'sleepers', '2021-09-10 13:42:18', '2021-09-10 13:42:18'),
(11, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', '2021-09-10 19:40:04', '2021-09-10 19:40:04');

-- --------------------------------------------------------

--
-- Table structure for table `active_map`
--

CREATE TABLE `active_map` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) NOT NULL,
  `user_identifier` varchar(255) NOT NULL,
  `map_identifier` varchar(255) NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `active_map`
--

INSERT INTO `active_map` (`id`, `guild_identifier`, `user_identifier`, `map_identifier`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'testmap', '2021-09-10 00:45:35', '2021-09-10 10:15:35'),
(2, '885106671427387392', '657695605367504906', 'pangea', '2021-09-10 06:49:14', '2021-09-10 19:38:50'),
(3, '885106671427387392', '531176133744525313', 'five_star_mari', '2021-09-10 12:29:20', '2021-09-10 12:29:20'),
(4, '885106671427387392', '790160755344277505', 'eclipse', '2021-09-10 13:39:55', '2021-09-10 13:39:55');

-- --------------------------------------------------------

--
-- Table structure for table `active_realm`
--

CREATE TABLE `active_realm` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `user_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `realm_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `active_realm`
--

INSERT INTO `active_realm` (`id`, `guild_identifier`, `user_identifier`, `realm_identifier`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'realm1', '2021-09-08 22:47:56', '2021-09-10 14:29:35'),
(2, '885106671427387392', '657695605367504906', 'LightSide', '2021-09-08 22:56:52', '2021-09-10 19:44:37'),
(6, '885106671427387392', '223933640810299392', 'Arridon', '2021-09-10 07:35:46', '2021-09-10 08:25:34'),
(7, '885106671427387392', '630629857348288512', 'apotheosis', '2021-09-10 12:01:09', '2021-09-10 12:01:09'),
(8, '885106671427387392', '531176133744525313', 'marigold_round', '2021-09-10 12:30:11', '2021-09-10 12:30:11'),
(9, '885106671427387392', '790160755344277505', 'Anokis', '2021-09-10 13:41:01', '2021-09-10 13:41:01');

-- --------------------------------------------------------

--
-- Table structure for table `game_armies`
--

CREATE TABLE `game_armies` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `user_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `realm_identifier` varchar(255) CHARACTER SET utf8 NOT NULL,
  `identifier` varchar(255) CHARACTER SET utf8 NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `game_armies`
--

INSERT INTO `game_armies` (`id`, `guild_identifier`, `user_identifier`, `realm_identifier`, `identifier`, `date_added`, `date_updated`) VALUES
(2, '885106671427387392', '797279085889585214', 'myRealm', 'myArmy', '2021-09-08 21:18:22', '2021-09-08 21:18:22'),
(3, '885106671427387392', '797279085889585214', 'realm1', 'army1', '2021-09-08 21:20:11', '2021-09-08 21:20:11'),
(4, '885106671427387392', '797279085889585214', 'realm2', 'army1', '2021-09-08 21:54:18', '2021-09-08 21:54:18'),
(5, '885106671427387392', '657695605367504906', 'RealmMuffin', 'ArmyM1', '2021-09-08 22:01:53', '2021-09-08 22:01:53'),
(6, '885106671427387392', '657695605367504906', 'RealmMuffin', 'ArmyM2', '2021-09-08 23:02:54', '2021-09-08 23:02:54'),
(7, '885106671427387392', '797279085889585214', 'testrealm1', 'testarmy1', '2021-09-09 20:26:36', '2021-09-09 20:26:36'),
(8, '885106671427387392', '657695605367504906', 'Khitai', 'batallion', '2021-09-09 20:56:05', '2021-09-09 20:56:05'),
(9, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', '2021-09-10 00:48:53', '2021-09-10 00:48:53'),
(10, '885106671427387392', '657695605367504906', 'Khitai', 'first_batallion', '2021-09-10 06:50:47', '2021-09-10 06:50:47'),
(11, '885106671427387392', '657695605367504906', 'Khitai', 'MugglesFighters1', '2021-09-10 07:31:52', '2021-09-10 07:31:52'),
(12, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', '2021-09-10 07:32:31', '2021-09-10 07:32:31'),
(13, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', '2021-09-10 07:38:30', '2021-09-10 07:38:30'),
(14, '885106671427387392', '630629857348288512', 'apotheosis', 'edu_diaspora', '2021-09-10 12:01:19', '2021-09-10 12:01:19'),
(15, '885106671427387392', '531176133744525313', 'marigold_round', 'knights_horse', '2021-09-10 12:31:29', '2021-09-10 12:31:29'),
(16, '885106671427387392', '790160755344277505', 'Anokis', 'sleepers', '2021-09-10 13:42:18', '2021-09-10 13:42:18'),
(17, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', '2021-09-10 19:40:03', '2021-09-10 19:40:03');

-- --------------------------------------------------------

--
-- Table structure for table `game_maps`
--

CREATE TABLE `game_maps` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) NOT NULL,
  `user_identifier` varchar(255) NOT NULL,
  `map_identifier` varchar(255) NOT NULL,
  `x` bigint(20) NOT NULL,
  `y` bigint(20) NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `game_maps`
--

INSERT INTO `game_maps` (`id`, `guild_identifier`, `user_identifier`, `map_identifier`, `x`, `y`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'a99d9463-118c-11ec-88e9-4437e6655d5b', 100, 100, '2021-09-10 00:40:38', '2021-09-10 00:40:38'),
(2, '885106671427387392', '657695605367504906', '1bdc9afa-11c0-11ec-b71c-4437e6655d5b', 100, 100, '2021-09-10 06:48:54', '2021-09-10 06:48:54'),
(3, '885106671427387392', '657695605367504906', '3174b165-11c0-11ec-8ead-4437e6655d5b', 100, 100, '2021-09-10 06:49:30', '2021-09-10 06:49:30'),
(4, '885106671427387392', '797279085889585214', 'testmap', 50, 50, '2021-09-10 08:39:29', '2021-09-10 08:39:29'),
(5, '885106671427387392', '474921086405050379', '(Acropolis)', 100, 100, '2021-09-10 09:41:56', '2021-09-10 09:41:56'),
(6, '885106671427387392', '531176133744525313', 'five_star_mari', 100, 100, '2021-09-10 12:28:40', '2021-09-10 12:28:40'),
(7, '885106671427387392', '790160755344277505', 'eclipse', 100, 100, '2021-09-10 13:39:31', '2021-09-10 13:39:31'),
(8, '885106671427387392', '657695605367504906', 'pangea', 150, 150, '2021-09-10 19:38:28', '2021-09-10 19:38:28');

-- --------------------------------------------------------

--
-- Table structure for table `game_map_objects`
--

CREATE TABLE `game_map_objects` (
  `id` bigint(20) NOT NULL,
  `guild_identifier` varchar(255) NOT NULL,
  `user_identifier` varchar(255) NOT NULL,
  `map_identifier` varchar(255) NOT NULL,
  `object_identifier` varchar(255) NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `game_map_objects`
--

INSERT INTO `game_map_objects` (`id`, `guild_identifier`, `user_identifier`, `map_identifier`, `object_identifier`, `x`, `y`, `date_added`, `date_updated`) VALUES
(2, '885106671427387392', '797279085889585214', 'testmap', '2', 10, 10, '2021-09-10 14:04:49', '2021-09-10 14:04:49');

-- --------------------------------------------------------

--
-- Table structure for table `game_realms`
--

CREATE TABLE `game_realms` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `user_identifier` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `identifier` varchar(255) DEFAULT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `game_realms`
--

INSERT INTO `game_realms` (`id`, `guild_identifier`, `user_identifier`, `identifier`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'myRealm', '2021-09-08 20:50:13', '2021-09-08 20:50:13'),
(2, '885106671427387392', '797279085889585214', 'realm1', '2021-09-08 21:19:32', '2021-09-08 21:19:32'),
(3, '885106671427387392', '797279085889585214', 'realm2', '2021-09-08 21:54:06', '2021-09-08 21:54:06'),
(4, '885106671427387392', '657695605367504906', 'RealmMuffin', '2021-09-08 22:00:38', '2021-09-08 22:00:38'),
(5, '885106671427387392', '797279085889585214', 'insensitiverealm', '2021-09-08 23:05:39', '2021-09-08 23:05:39'),
(6, '885106671427387392', '797279085889585214', 'sensitiveRealm', '2021-09-08 23:05:49', '2021-09-08 23:05:49'),
(7, '885106671427387392', '657695605367504906', 'RealmMuffin2', '2021-09-08 23:47:58', '2021-09-08 23:47:58'),
(11, '885106671427387392', '657695605367504906', 'khitai', '2021-09-09 20:54:48', '2021-09-09 20:54:48'),
(12, '885106671427387392', '657695605367504906', 'Kirthan', '2021-09-10 06:50:13', '2021-09-10 06:50:13'),
(13, '885106671427387392', '223933640810299392', 'Arridon', '2021-09-10 07:28:05', '2021-09-10 07:28:05'),
(14, '885106671427387392', '657695605367504906', 'Muggles', '2021-09-10 07:31:23', '2021-09-10 07:31:23'),
(15, '885106671427387392', '630629857348288512', 'Apotheosis', '2021-09-10 11:51:22', '2021-09-10 11:51:22'),
(16, '885106671427387392', '630629857348288512', 'apotheosis_of_iron', '2021-09-10 11:52:02', '2021-09-10 11:52:02'),
(17, '885106671427387392', '531176133744525313', 'marigold_round', '2021-09-10 12:30:11', '2021-09-10 12:30:11'),
(18, '885106671427387392', '790160755344277505', 'Anokis', '2021-09-10 13:41:01', '2021-09-10 13:41:01'),
(19, '885106671427387392', '657695605367504906', 'DarkSide', '2021-09-10 19:39:35', '2021-09-10 19:39:35'),
(20, '885106671427387392', '657695605367504906', 'LightSide', '2021-09-10 19:44:37', '2021-09-10 19:44:37');

-- --------------------------------------------------------

--
-- Table structure for table `game_units`
--

CREATE TABLE `game_units` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `user_identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `realm_identifier` varchar(255) CHARACTER SET utf8 NOT NULL,
  `army_identifier` varchar(255) CHARACTER SET utf8 NOT NULL,
  `identifier` varchar(255) CHARACTER SET utf8 NOT NULL,
  `size` bigint(20) NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `game_units`
--

INSERT INTO `game_units` (`id`, `guild_identifier`, `user_identifier`, `realm_identifier`, `army_identifier`, `identifier`, `size`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'realm1', 'army1', 'archers1', 3000, '2021-09-08 21:37:39', '2021-09-08 21:37:39'),
(2, '885106671427387392', '797279085889585214', 'realm1', 'army1', 'cavalry1', 2000, '2021-09-08 21:43:12', '2021-09-08 21:43:12'),
(3, '885106671427387392', '797279085889585214', 'realm2', 'army1', 'archers1', 100, '2021-09-08 21:54:34', '2021-09-08 21:54:34'),
(4, '885106671427387392', '657695605367504906', 'RealmMuffin', 'ArmyM1', 'archers', 200, '2021-09-08 22:03:10', '2021-09-10 00:44:12'),
(5, '885106671427387392', '657695605367504906', 'RealmMuffin', 'ArmyM1', 'cavalry', 100, '2021-09-08 22:05:41', '2021-09-08 22:05:41'),
(6, '885106671427387392', '797279085889585214', 'realm2', 'army1', 'Heavy Infantry', 1000, '2021-09-08 22:16:06', '2021-09-08 22:16:06'),
(7, '885106671427387392', '657695605367504906', 'RealmMuffin', 'ArmyM1', 'Heavy Infantry', 200, '2021-09-08 22:16:56', '2021-09-08 22:16:56'),
(8, '885106671427387392', '797279085889585214', 'realm1', 'army1', 'foot soldier', 1000, '2021-09-09 21:50:29', '2021-09-09 22:19:51'),
(9, '885106671427387392', '797279085889585214', 'realm1', 'army1', 'archer2', 1000, '2021-09-09 22:14:31', '2021-09-09 22:19:38'),
(10, '885106671427387392', '657695605367504906', 'Khitai', 'batallion', 'footsoldiers', 100, '2021-09-10 00:48:29', '2021-09-10 00:48:29'),
(11, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Sheyleen squires', 300, '2021-09-10 00:49:40', '2021-09-10 00:50:49'),
(12, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Elite Kunoichis', 1500, '2021-09-10 00:51:54', '2021-09-10 00:51:54'),
(13, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Barefoot_Norse_Barbarian_Amazons', 100, '2021-09-10 06:51:54', '2021-09-10 06:51:54'),
(14, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Valkyries', 500, '2021-09-10 06:52:24', '2021-09-10 06:52:24'),
(15, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', 'Sawblade_Tank', 100, '2021-09-10 07:44:48', '2021-09-10 07:44:48'),
(16, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Doll Archers', 500, '2021-09-10 07:50:30', '2021-09-10 07:50:30'),
(17, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', 'Dryrott_Plaguethrower', 100, '2021-09-10 07:59:44', '2021-09-10 07:59:44'),
(18, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', 'Crazyhorse_Jouster', 200, '2021-09-10 08:29:50', '2021-09-10 08:29:50'),
(19, '885106671427387392', '630629857348288512', 'apotheosis', 'edu_diaspora', 'King_Elenxes', 1001, '2021-09-10 12:06:00', '2021-09-10 12:19:29'),
(20, '885106671427387392', '531176133744525313', 'marigold_round', 'knights_horse', 'witches', 100, '2021-09-10 12:32:28', '2021-09-10 12:32:28'),
(21, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Doll witches', 250, '2021-09-10 12:39:18', '2021-09-10 12:39:18'),
(23, '885106671427387392', '797279085889585214', 'myRealm', 'myarmy', 'pikemen', 100, '2021-09-10 12:53:02', '2021-09-10 12:53:02'),
(24, '885106671427387392', '790160755344277505', 'Anokis', 'sleepers', 'Sleepless Upholder', 100, '2021-09-10 13:44:42', '2021-09-10 13:44:42'),
(25, '885106671427387392', '790160755344277505', 'Anokis', 'sleepers', 'Awakened Defenders', 1600, '2021-09-10 13:46:14', '2021-09-10 13:46:30'),
(26, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Woke Warriors', 1500, '2021-09-10 13:46:41', '2021-09-10 13:46:41'),
(27, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', 'archers', 500, '2021-09-10 19:40:52', '2021-09-10 19:40:52'),
(28, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', 'pikemen', 100, '2021-09-10 19:41:30', '2021-09-10 19:41:30'),
(29, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', 'HeavyInfantry', 100, '2021-09-10 19:42:04', '2021-09-10 19:42:04'),
(30, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', 'LightInfantry', 400, '2021-09-10 19:42:39', '2021-09-10 19:42:39'),
(31, '885106671427387392', '657695605367504906', 'DarkSide', 'DarkArmy', 'cavalry', 200, '2021-09-10 19:43:02', '2021-09-10 19:43:02');

-- --------------------------------------------------------

--
-- Table structure for table `game_unit_attributes`
--

CREATE TABLE `game_unit_attributes` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) NOT NULL,
  `user_identifier` varchar(255) NOT NULL,
  `realm_identifier` varchar(255) NOT NULL,
  `army_identifier` varchar(255) NOT NULL,
  `unit_identifier` varchar(255) NOT NULL,
  `parameter` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `game_unit_attributes`
--

INSERT INTO `game_unit_attributes` (`id`, `guild_identifier`, `user_identifier`, `realm_identifier`, `army_identifier`, `unit_identifier`, `parameter`, `value`, `date_added`, `date_updated`) VALUES
(1, '885106671427387392', '797279085889585214', 'realm1', 'army1', 'archers1', 'race', 'high elf', '2021-09-09 22:28:39', '2021-09-09 22:28:39'),
(2, '885106671427387392', '797279085889585214', 'realm1', 'army1', 'archers1', 'speed', '30', '2021-09-09 22:29:21', '2021-09-09 22:29:21'),
(3, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Valkyries', 'race', 'Valhallan Demi-Goddesses', '2021-09-10 06:55:12', '2021-09-10 06:55:12'),
(4, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Valkyries', 'speed', '1000', '2021-09-10 06:55:47', '2021-09-10 06:55:47'),
(5, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Doll Archers', 'race', 'humanoid dolls with a soul and an attitude', '2021-09-10 07:52:45', '2021-09-10 07:52:45'),
(6, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Doll Archers', 'speed', '30', '2021-09-10 07:53:09', '2021-09-10 07:53:09'),
(7, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Doll Archers', 'range', 'a very long ranged attack', '2021-09-10 07:53:52', '2021-09-10 07:53:52'),
(8, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Sheyleen squires', 'race', 'Apparently flawless Human Asian women that could have been demonic angels', '2021-09-10 08:13:25', '2021-09-10 08:13:25'),
(9, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Sheyleen squires', 'class', 'Personal Kunoichis at work for her highness, Sheyleen herself, really deadly with all their ninja wepons', '2021-09-10 08:14:34', '2021-09-10 08:14:34'),
(10, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Sheyleen squires', 'speed', '1500', '2021-09-10 08:15:14', '2021-09-10 08:15:14'),
(11, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Sheyleen squires', 'Armor', 'Class', '2021-09-10 08:15:42', '2021-09-10 08:15:42'),
(12, '885106671427387392', '657695605367504906', 'Khitai', 'Kunoichis', 'Sheyleen squires', 'Armor Class Description', 'Their skin was hardened magically, still being soft at touch, but really impenetrable', '2021-09-10 08:16:56', '2021-09-10 08:16:56'),
(13, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', 'Dryrott_Plaguethrower', 'race', 'Possessed cyborgs who use diseases and corrosive weaponry', '2021-09-10 08:23:47', '2021-09-10 08:23:47'),
(14, '885106671427387392', '223933640810299392', 'Arridon', 'Sawblade_Talon', 'Crazyhorse_Jouster', 'race', 'Skeletal demons who ride magic motorcylcles and use spear rifles', '2021-09-10 08:31:33', '2021-09-10 08:31:33'),
(15, '885106671427387392', '630629857348288512', 'apotheosis', 'edu_diaspora', 'King_Elenxes', 'Flight', '', '2021-09-10 12:07:25', '2021-09-10 12:07:25'),
(16, '885106671427387392', '657695605367504906', 'Muggles', 'MugglesFighters1', 'Doll witches', 'type_of_magick', 'The type of Magick that will make blue flames become red', '2021-09-10 12:40:43', '2021-09-10 12:40:43'),
(17, '885106671427387392', '531176133744525313', 'marigold_round', 'knights_horse', 'witches', 'fireball_with_your_name_on_it', 'homes in on whoevers name is written on it', '2021-09-10 12:42:12', '2021-09-10 12:42:12'),
(18, '885106671427387392', '531176133744525313', 'marigold_round', 'knights_horse', 'witches', 'icey_skates', '60', '2021-09-10 12:44:52', '2021-09-10 12:44:52'),
(19, '885106671427387392', '531176133744525313', 'marigold_round', 'knights_horse', 'witches', 'thunderous_teleportation', 'a teleportation that causes a lightning strike both at the place you cane from, and in the background of the place you end up in', '2021-09-10 12:50:37', '2021-09-10 12:50:37'),
(21, '885106671427387392', '790160755344277505', 'Anokis', 'sleepers', 'Sleepless Upholder', 'Neut', 'a lot', '2021-09-10 13:51:14', '2021-09-10 13:51:14');

-- --------------------------------------------------------

--
-- Table structure for table `guilds`
--

CREATE TABLE `guilds` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `identifier` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `guilds`
--

INSERT INTO `guilds` (`id`, `identifier`, `date_added`, `date_updated`) VALUES
(2, '885106671427387392', '2021-09-08 20:17:37', '2021-09-08 20:17:37');

-- --------------------------------------------------------

--
-- Table structure for table `guild_prefixes`
--

CREATE TABLE `guild_prefixes` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `guild_identifier` varchar(255) NOT NULL,
  `prefixes` text NOT NULL,
  `date_added` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `active_army`
--
ALTER TABLE `active_army`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `active_map`
--
ALTER TABLE `active_map`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `active_realm`
--
ALTER TABLE `active_realm`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game_armies`
--
ALTER TABLE `game_armies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game_maps`
--
ALTER TABLE `game_maps`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game_map_objects`
--
ALTER TABLE `game_map_objects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game_realms`
--
ALTER TABLE `game_realms`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game_units`
--
ALTER TABLE `game_units`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `game_unit_attributes`
--
ALTER TABLE `game_unit_attributes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `guilds`
--
ALTER TABLE `guilds`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `guild_prefixes`
--
ALTER TABLE `guild_prefixes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `active_army`
--
ALTER TABLE `active_army`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `active_map`
--
ALTER TABLE `active_map`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `active_realm`
--
ALTER TABLE `active_realm`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `game_armies`
--
ALTER TABLE `game_armies`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `game_maps`
--
ALTER TABLE `game_maps`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `game_map_objects`
--
ALTER TABLE `game_map_objects`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `game_realms`
--
ALTER TABLE `game_realms`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `game_units`
--
ALTER TABLE `game_units`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `game_unit_attributes`
--
ALTER TABLE `game_unit_attributes`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `guilds`
--
ALTER TABLE `guilds`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `guild_prefixes`
--
ALTER TABLE `guild_prefixes`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
