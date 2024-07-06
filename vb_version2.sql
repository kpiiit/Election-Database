-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: VeriBallot
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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
-- Table structure for table BUDGET
--

DROP TABLE IF EXISTS BUDGET;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE BUDGET (
  BudgetID varchar(200) NOT NULL,
  Amount int DEFAULT NULL,
  Category varchar(200) NOT NULL,
  AllocationDate date NOT NULL,
  Expenditure varchar(200) NOT NULL,
  PartyID varchar(200) NOT NULL,
  ConstituencyID varchar(200) NOT NULL,
  ElectionID varchar(200) NOT NULL,
  PRIMARY KEY (BudgetID),
  KEY fkey1_budget (PartyID),
  KEY fkey2_budget (ConstituencyID),
  KEY fkey3_budget (ElectionID),
  CONSTRAINT fkey1_budget FOREIGN KEY (PartyID) REFERENCES PARTY (PartyID),
  CONSTRAINT fkey2_budget FOREIGN KEY (ConstituencyID) REFERENCES CONSTITUENCY (ConstituencyID),
  CONSTRAINT fkey3_budget FOREIGN KEY (ElectionID) REFERENCES ELECTIONS (ElectionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Insert data into the BUDGET table
INSERT INTO BUDGET (BudgetID, Amount, Category, AllocationDate, Expenditure, PartyID, ConstituencyID, ElectionID)
VALUES
  ('Bud_BJP_GEN_2019', 500000, 'Campaign', '2023-12-02', 'Advertising', 'AAP', 'Del_02', 'GEN_2019'),
  ('Bud_AITC_GEN_2019', 700000, 'Campaign', '2023-12-02', 'Rallies', 'AITC', 'Kan_02', 'GEN_2019'),
  ('Bud_BJP_GEN_2014', 1000000, 'Infrastructure', '2023-12-02', 'Office expenses', 'BJP', 'Mum_02', 'GEN_2014'),
  ('Bud_BRS_GEN_2009', 800000, 'Campaign', '2023-12-02', 'Printed materials', 'BRS', 'Guj_01', 'GEN_2009'),
  ('Bud_INC_GEN_2019', 600000, 'Campaign', '2023-12-02', 'Online promotion', 'INC', 'Pun_01', 'GEN_2019'),
  -- Add more rows as needed

  ('Bud_AAP_GEN_2019', 550000, 'Campaign', '2023-12-02', 'Social media ads', 'AAP', 'Del_02', 'GEN_2019'),
  ('Bud_AITC_GEN_2009', 750000, 'Campaign', '2023-12-02', 'Public events', 'AITC', 'Kan_02', 'GEN_2009'),
  ('Bud_BJP_GEN_2009', 1200000, 'Infrastructure', '2023-12-02', 'Headquarters construction', 'BJP', 'Mum_02', 'GEN_2009'),
  ('Bud_BRS_GEN_2014', 850000, 'Campaign', '2023-12-02', 'Radio advertisements', 'BRS', 'Guj_01', 'GEN_2014'),
  ('Bud_INC_GEN_2009', 650000, 'Campaign', '2023-12-02', 'Billboard placements', 'INC', 'Pun_01', 'GEN_2009');
  -- Add more rows as needed

--
-- Dumping data for table BUDGET
--

LOCK TABLES BUDGET WRITE;
/*!40000 ALTER TABLE BUDGET DISABLE KEYS */;
/*!40000 ALTER TABLE BUDGET ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table CANDIDATE
--

DROP TABLE IF EXISTS CANDIDATE;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE CANDIDATE (
  CandidateID varchar(100) NOT NULL,
  CasteStatus varchar(100) DEFAULT NULL,
  Age int DEFAULT NULL,
  Gender varchar(20) DEFAULT NULL,
  Name varchar(200) NOT NULL,
  TotalFinancialAssets int DEFAULT NULL,
  PartyID varchar(200) DEFAULT NULL,
  ContesterID varchar(100) DEFAULT NULL,
  PRIMARY KEY (CandidateID),
  KEY fkey2_cand (ContesterID),
  KEY fkey1_cand (PartyID),
  CONSTRAINT fkey1_cand FOREIGN KEY (PartyID) REFERENCES PARTY (PartyID),
  CONSTRAINT fkey2_cand FOREIGN KEY (ContesterID) REFERENCES CANDIDATE (CandidateID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40000 ALTER TABLE CANDIDATE ENABLE KEYS */;

--
-- Dumping data for table CANDIDATE
--

LOCK TABLES CANDIDATE WRITE;
/*!40000 ALTER TABLE CANDIDATE DISABLE KEYS */;
INSERT INTO CANDIDATE VALUES ('MM_AITC','GEN',49,'F','Mahua Moitra',1000000,'AITC',NULL),('NKS_IND','ST',54,'M','Naba Kumar Sarania',1100000,NULL,NULL),('NM_BJP','GEN',73,'M','Narendra Modi',1500000,'BJP',NULL),('RG_INC','GEN',53,'M','Rahul Gandhi',1400000,'INC',NULL),('TS_BJP','GEN',49,'M','Tejasvi Surya',700000,'BJP',NULL),('YA_BJP','GEN',40,'M','Yogi Adityanath',33000,'BJP',NULL);
UNLOCK TABLES;

--
-- Table structure for table COALITION
--


DROP TABLE IF EXISTS COALITION;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE COALITION (
  CoalitionID varchar(100) NOT NULL,
  CoalitionName varchar(100) NOT NULL,
  PoliticalPosition varchar(100) DEFAULT NULL,
  PRIMARY KEY (CoalitionID,CoalitionName)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table COALITION
--

LOCK TABLES COALITION WRITE;
/*!40000 ALTER TABLE COALITION DISABLE KEYS */;
INSERT INTO COALITION VALUES ('INDIA','Indian National Developmental Inclusive Alliance','Left'),('NDA','National Democratic Alliance','Right');
/*!40000 ALTER TABLE COALITION ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table COALITION_MEMBERS
--

DROP TABLE IF EXISTS COALITION_MEMBERS;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE COALITION_MEMBERS (
  CoalitionID varchar(100) NOT NULL,
  PartyID varchar(200) NOT NULL,
  ElectionID varchar(200) NOT NULL,
  PRIMARY KEY (CoalitionID,PartyID,ElectionID),
  KEY fkey2_cm (PartyID),
  KEY fkey1_ed (ElectionID),
  CONSTRAINT fkey1_cm FOREIGN KEY (CoalitionID) REFERENCES COALITION (CoalitionID),
  CONSTRAINT fkey2_cm FOREIGN KEY (PartyID) REFERENCES PARTY (PartyID),
  CONSTRAINT fkey3_cm FOREIGN KEY (ElectionID) REFERENCES ELECTIONS (ElectionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table COALITION_MEMBERS
--

LOCK TABLES COALITION_MEMBERS WRITE;
/*!40000 ALTER TABLE COALITION_MEMBERS DISABLE KEYS */;
INSERT INTO COALITION_MEMBERS VALUES ('INDIA','AAP','GEN_2024'),('INDIA','AITC','GEN_2024'),('NDA','BJP','GEN_2019'),('INDIA','INC','GEN_2024');
/*!40000 ALTER TABLE COALITION_MEMBERS ENABLE KEYS */;
UNLOCK TABLES;
--
-- Table structure for table CONSTITUENCY
--

DROP TABLE IF EXISTS CONSTITUENCY;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE CONSTITUENCY (
  ConstituencyID varchar(200) NOT NULL,
  ConstituencyName varchar(200) NOT NULL,
  State varchar(200) NOT NULL,
  ReservedStatus varchar(10) NOT NULL,
  Population int DEFAULT NULL,
  Area int DEFAULT NULL,
  ConstituencyType varchar(100) DEFAULT NULL,
  IncumbentCandidate varchar(100) DEFAULT NULL,
  NumPollBooth int DEFAULT NULL,
  PRIMARY KEY (ConstituencyID),
  KEY fkey1_const (IncumbentCandidate),
  CONSTRAINT fkey1_const FOREIGN KEY (IncumbentCandidate) REFERENCES CANDIDATE (CandidateID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO CONSTITUENCY (ConstituencyID, ConstituencyName, State, ReservedStatus, Population, Area, ConstituencyType, IncumbentCandidate, NumPollBooth)
VALUES
  ('Del_02', 'Delhi 2', 'Delhi', 'No', 10000000, 20000, 'Urban', 'NM_BJP', 50),
  ('Kan_02', 'Kanpur 2', 'UP', 'Yes', 150000, 300, 'Rural', 'YA_BJP', 75),
  ('Mum_02', 'Mumbai 1', 'State 3', 'No', 120000, 250, 'Urban', 'TS_BJP', 60),
  ('Guj_01', 'Mumbai 1', 'State 3', 'No', 120000, 250, 'Urban', 'RG_INC', 60),
  ('Pun_01', 'Mumbai 1', 'State 3', 'No', 120000, 250, 'Urban', 'MM_AITC', 60)
  -- Add more rows as needed
  ;


--
-- Dumping data for table CONSTITUENCY
--

LOCK TABLES CONSTITUENCY WRITE;
/*!40000 ALTER TABLE CONSTITUENCY DISABLE KEYS */;
/*!40000 ALTER TABLE CONSTITUENCY ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table CONTEST
--

DROP TABLE IF EXISTS CONTEST;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE CONTEST (
  CandidateID varchar(100) DEFAULT NULL,
  ConstituencyID varchar(200) DEFAULT NULL,
  ElectionID varchar(200) DEFAULT NULL,
  KEY fkey1_contest (CandidateID),
  KEY fkey2_contest (ConstituencyID),
  KEY fkey3_contest (ElectionID),
  CONSTRAINT fkey1_contest FOREIGN KEY (CandidateID) REFERENCES CANDIDATE (CandidateID),
  CONSTRAINT fkey2_contest FOREIGN KEY (ConstituencyID) REFERENCES CONSTITUENCY (ConstituencyID),
  CONSTRAINT fkey3_contest FOREIGN KEY (ElectionID) REFERENCES ELECTIONS (ElectionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


INSERT INTO CONTEST (CandidateID, ConstituencyID, ElectionID)
VALUES
  ('NM_BJP', 'Del_02', 'GEN_2019'),
  ('YA_BJP', 'Kan_02', 'GEN_2024'),
  ('TS_BJP', 'Mum_02', 'GEN_2014'),
  ('RG_INC', 'Guj_01', 'GEN_2014'),
  ('MM_AITC', 'Pun_01', 'GEN_2019')
  -- Add more rows as needed
  ;
--
-- Dumping data for table CONTEST
--

LOCK TABLES CONTEST WRITE;
/*!40000 ALTER TABLE CONTEST DISABLE KEYS */;
/*!40000 ALTER TABLE CONTEST ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table CRIMINAL_RECORDS
--

DROP TABLE IF EXISTS CRIMINAL_RECORDS;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE CRIMINAL_RECORDS (
  CandidateID varchar(100) NOT NULL,
  CriminalRecord varchar(200) NOT NULL,
  PRIMARY KEY (CandidateID,CriminalRecord),
  CONSTRAINT fkey1_criminal FOREIGN KEY (CandidateID) REFERENCES CANDIDATE (CandidateID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO CRIMINAL_RECORDS (CandidateID, CriminalRecord)
VALUES
  ('NM_BJP', 'CLEAN'),
  ('RG_INC', 'DEFEMATION'),
  ('MM_AITC', 'DEFEMATION'),
  ('TS_BJP', 'MONEY LAUNDERING'),
  ('NKS_IND', 'ATTEMPT TO MURDER')
  -- Add more rows as needed
  ;

--
-- Dumping data for table CRIMINAL_RECORDS
--

LOCK TABLES CRIMINAL_RECORDS WRITE;
/*!40000 ALTER TABLE CRIMINAL_RECORDS DISABLE KEYS */;
/*!40000 ALTER TABLE CRIMINAL_RECORDS ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table EDUCATIONAL_QUALIFICATIONS
--

DROP TABLE IF EXISTS EDUCATIONAL_QUALIFICATIONS;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE EDUCATIONAL_QUALIFICATIONS (
  CandidateID varchar(100) NOT NULL,
  EducationalQualification varchar(200) NOT NULL,
  PRIMARY KEY (CandidateID,EducationalQualification),
  CONSTRAINT fkey1_education FOREIGN KEY (CandidateID) REFERENCES CANDIDATE (CandidateID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO EDUCATIONAL_QUALIFICATIONS (CandidateID, EducationalQualification)
VALUES
  ('NM_BJP', 'METRIC PASS'),
  ('RG_INC', 'BACHELOR OF ARTS'),
  ('MM_AITC', 'GRADUATE'),
  ('TS_BJP', 'POST GRADUATE'),
  ('NKS_IND', 'NONE')
  -- Add more rows as needed
  ;
--
-- Dumping data for table EDUCATIONAL_QUALIFICATIONS
--

LOCK TABLES EDUCATIONAL_QUALIFICATIONS WRITE;
/*!40000 ALTER TABLE EDUCATIONAL_QUALIFICATIONS DISABLE KEYS */;
/*!40000 ALTER TABLE EDUCATIONAL_QUALIFICATIONS ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table ELECTIONS
--

DROP TABLE IF EXISTS ELECTIONS;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE ELECTIONS (
  ElectionID varchar(200) NOT NULL,
  ElectionResult varchar(300) DEFAULT NULL,
  ElectionType varchar(200) NOT NULL,
  PRIMARY KEY (ElectionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table ELECTIONS
--

LOCK TABLES ELECTIONS WRITE;
/*!40000 ALTER TABLE ELECTIONS DISABLE KEYS */;
INSERT INTO ELECTIONS VALUES ('GEN_2019','NDA victory','General'),('GEN_2024',NULL,'General'),('GEN_2014','NDA victory','General'),('GEN_2009','INC victory','General'),('DEL_GEN_2009','AAP victory','General');
/*!40000 ALTER TABLE ELECTIONS ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table ELECTION_DATES
--

DROP TABLE IF EXISTS ELECTION_DATES;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE ELECTION_DATES (
  ElectionID varchar(200) NOT NULL,
  ElectionDate date NOT NULL,
  PRIMARY KEY (ElectionID,ElectionDate),
  CONSTRAINT fkey1_ed FOREIGN KEY (ElectionID) REFERENCES ELECTIONS (ElectionID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table ELECTION_DATES
--

LOCK TABLES ELECTION_DATES WRITE;
/*!40000 ALTER TABLE ELECTION_DATES DISABLE KEYS */;
/*!40000 ALTER TABLE ELECTION_DATES ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table ELECTION_IN_CONSTITUENCY
--

DROP TABLE IF EXISTS ELECTION_IN_CONSTITUENCY;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE ELECTION_IN_CONSTITUENCY (
  ConstituencyID varchar(200) DEFAULT NULL,
  ElectionID varchar(200) DEFAULT NULL,
  KEY fkey1_eic (ElectionID),
  KEY fkey2_eic (ConstituencyID),
  CONSTRAINT fkey1_eic FOREIGN KEY (ElectionID) REFERENCES ELECTIONS (ElectionID),
  CONSTRAINT fkey2_eic FOREIGN KEY (ConstituencyID) REFERENCES CONSTITUENCY (ConstituencyID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO ELECTION_IN_CONSTITUENCY (ConstituencyID, ElectionID)
VALUES
  ('Del_02', 'GEN_2019'),
  ('Kan_02', 'GEN_2019'),
  ('Mum_02', 'GEN_2014'),
  ('Guj_01', 'GEN_2009'),
  ('Pun_01', 'GEN_2019')
  -- Add more rows as needed
  ;

--
-- Dumping data for table ELECTION_IN_CONSTITUENCY
--

LOCK TABLES ELECTION_IN_CONSTITUENCY WRITE;
/*!40000 ALTER TABLE ELECTION_IN_CONSTITUENCY DISABLE KEYS */;
/*!40000 ALTER TABLE ELECTION_IN_CONSTITUENCY ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table PARTY
--

DROP TABLE IF EXISTS PARTY;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE PARTY (
  PartyID varchar(200) NOT NULL,
  PartyName varchar(200) NOT NULL,
  PartyMembership int DEFAULT NULL,
  PartySymbol varchar(200) DEFAULT NULL,
  PoliticalPosition varchar(100) DEFAULT NULL,
  PRIMARY KEY (PartyID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table PARTY
--

LOCK TABLES PARTY WRITE;
/*!40000 ALTER TABLE PARTY DISABLE KEYS */;
INSERT INTO PARTY VALUES ('AAP','Aam Admi Party',8000,'Broom','Centre'),('AITC','All India Trinamool Congress',5000,'Flower','Left'),('BJP','Bharatiya Janata Party',10000,'Lotus','Right'),('BRS','Bharat Rashtra Samiti',3000,'Car','Centre'),('INC','Indian National Congress',7000,'Hand','Centre');
/*!40000 ALTER TABLE PARTY ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table VOTE
--

DROP TABLE IF EXISTS VOTE;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE VOTE (
  VoteID varchar(200) NOT NULL,
  VoterID varchar(100) NOT NULL,
  ElectionID varchar(200) NOT NULL,
  CandidateID varchar(100) NOT NULL,
  PRIMARY KEY (VoteID),
  KEY fkey1_vote (VoterID),
  KEY fkey2_vote (ElectionID),
  KEY fkey3_vote (CandidateID),
  CONSTRAINT fkey1_vote FOREIGN KEY (VoterID) REFERENCES VOTER (VoterID),
  CONSTRAINT fkey2_vote FOREIGN KEY (ElectionID) REFERENCES ELECTIONS (ElectionID),
  CONSTRAINT fkey3_vote FOREIGN KEY (CandidateID) REFERENCES CANDIDATE (CandidateID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO VOTE (VoteID, VoterID, ElectionID, CandidateID)
VALUES
  ('TaGu_19', 'TaGu_19', 'GEN_2019', 'NM_BJP'),
  ('SaSr', 'SaSr_30', 'GEN_2019', 'NM_BJP'),
  ('BiGa', 'BiGa_22', 'GEN_2009', 'RG_INC'),
  ('MaCh', 'MaCh_30', 'DEL_GEN_2022', 'TS_BJP'),
  ('ArBa', 'ArBa_22', 'GEN_2019', 'NM_BJP')
  ;
--
-- Dumping data for table VOTE
--

LOCK TABLES VOTE WRITE;
/*!40000 ALTER TABLE VOTE DISABLE KEYS */;
/*!40000 ALTER TABLE VOTE ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table VOTER
--

DROP TABLE IF EXISTS VOTER;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE VOTER (
  VoterID varchar(100) NOT NULL,
  Name varchar(100) DEFAULT NULL,
  Age int DEFAULT NULL,
  Gender varchar(20) DEFAULT NULL,
  ConstituencyID varchar(200) DEFAULT NULL,
  PRIMARY KEY (VoterID),
  KEY fkey1_voter (ConstituencyID),
  CONSTRAINT fkey1_voter FOREIGN KEY (ConstituencyID) REFERENCES CONSTITUENCY (ConstituencyID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

INSERT INTO VOTER (VoterID, Name, Age, Gender, ConstituencyID)
VALUES
  ('TaGu_19', 'Tanish Gupta', 19, 'Male', 'Pun_01'),
  ('SaSr_30', 'Samarth Srikar', 30, 'Female', 'Guj_01'),
  ('BiGa_22', 'Bipasha Garg', 22, 'Male', 'Kan_02'),
  ('MaCh_30', 'Manan Chichra', 30, 'Female', 'Del_02'),
  ('ArBa_22', 'Aryaman Bahl', 22, 'Male', 'Mum_02')
  -- Add more rows as needed
  ;

--
-- Dumping data for table VOTER
--

LOCK TABLES VOTER WRITE;
/*!40000 ALTER TABLE VOTER DISABLE KEYS */;
/*!40000 ALTER TABLE VOTER ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02 16:51:34
