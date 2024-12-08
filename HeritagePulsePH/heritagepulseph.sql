-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2024 at 02:42 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `heritagepulseph`
--

-- --------------------------------------------------------

--
-- Table structure for table `dances`
--

CREATE TABLE `dances` (
  `dance_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `suite` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dances`
--

INSERT INTO `dances` (`dance_id`, `title`, `suite`) VALUES
(1, 'Futageh', 'Cordillera'),
(2, 'Jota Rizal', 'Western Influence'),
(3, 'Komintang', 'Western Influence'),
(4, 'Polka Sa Nayon', 'Rural'),
(5, 'Salakban', 'Rural'),
(6, 'Jota Vizcayana', 'Rural'),
(7, 'Infantes', 'Rural'),
(8, 'Pabayle Iloco', 'Rural'),
(9, 'Los Bailes De San Antonio', 'Rural'),
(10, 'Maral Dad Libun', 'Muslim');

-- --------------------------------------------------------

--
-- Table structure for table `suites`
--

CREATE TABLE `suites` (
  `suite_id` int(11) NOT NULL,
  `suite_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suites`
--

INSERT INTO `suites` (`suite_id`, `suite_name`) VALUES
(1, 'Cordillera'),
(2, 'Rural'),
(3, 'Muslim'),
(4, 'Western Influence');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `role`) VALUES
(5, 'Lewis', '143', 'Student'),
(6, 'tohru', 'password', 'Student'),
(7, 'Gabriel', '012805', 'Dancer'),
(8, 'Adryan', '456123', 'Choreographer'),
(9, 'Diwayanis', '0128', 'Dance Researcher'),
(10, 'Mhyco', 'mhyco28', 'Dancer'),
(11, 'Morpheus', '0128', 'Student'),
(12, 'Aidhen Montefiorre', '0978', 'Dancer'),
(13, 'Loren', '5678', 'Student'),
(14, 'Willmer', 'will34', 'Student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dances`
--
ALTER TABLE `dances`
  ADD PRIMARY KEY (`dance_id`);

--
-- Indexes for table `suites`
--
ALTER TABLE `suites`
  ADD PRIMARY KEY (`suite_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dances`
--
ALTER TABLE `dances`
  MODIFY `dance_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `suites`
--
ALTER TABLE `suites`
  MODIFY `suite_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
