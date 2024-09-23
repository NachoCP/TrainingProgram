-- Asignación de empleados al departamento de Marketing
INSERT INTO employee_department (id, employee_id, department_id) VALUES
(1, 1, 1), 
(2, 2, 1),  
(3, 3, 1),  
(4, 4, 1),  
(5, 5, 1),  
(6, 6, 1),  
(7, 7, 1);

-- Asignación de empleados al departamento de Sales
INSERT INTO employee_department (id, employee_id, department_id) VALUES
(8, 8, 2),  
(9, 9, 2),   
(10, 10, 2), 
(11, 11, 2), 
(12, 12, 2), 
(13, 13, 2), 
(14, 14, 2);
-- Asignación de empleados al departamento de Human Resources
INSERT INTO employee_department (id, employee_id, department_id) VALUES
(15, 15, 3), 
(16, 16, 3),  
(17, 17, 3),  
(18, 18, 3),  
(19, 19, 3),  
(20, 20, 3);  


-- Competencias para el departamento de Marketing
INSERT INTO competency_level (id, competency_id, department_id, required_level, num_workers) VALUES
(1, 1, 1, 'advanced', 1),   
(2, 2, 1, 'intermediate', 3),
(3, 3, 1, 'advanced', 1),   
(4, 5, 1, 'basic', 2);   

-- Competencias para el departamento de Sales
INSERT INTO competency_level (id, competency_id, department_id, required_level, num_workers) VALUES
(5, 7, 2, 'expert', 1),      
(6, 3, 2, 'advanced', 2),    
(7, 9, 2, 'intermediate', 3);

-- Competencias para el departamento de Human Resources (HR)
INSERT INTO competency_level (id, competency_id, department_id, required_level, num_workers) VALUES
(8, 1, 3, 'advanced', 1),     
(9, 10, 3, 'intermediate', 3),
(10, 6, 3, 'intermediate', 2);



INSERT INTO employee_competency (id, employee_id, competency_id, current_level) VALUES
('1', '1', '1', 'intermediate')
,('2', '1', '2', 'intermediate')
,('3', '1', '3', 'expert')
,('4', '1', '4', 'basic')
,('5', '1', '5', 'intermediate')
,('6', '1', '6', 'advanced')
,('7', '1', '7', 'basic')
,('8', '1', '8', 'intermediate')
,('9', '1', '9', 'intermediate')
,('10', '1', '10', 'expert')
,('11', '2', '1', 'basic')
,('12', '2', '2', 'intermediate')
,('13', '2', '3', 'expert')
,('14', '2', '4', 'advanced')
,('15', '2', '5', 'expert')
,('16', '2', '6', 'expert')
,('17', '2', '7', 'intermediate')
,('18', '2', '8', 'expert')
,('19', '2', '9', 'basic')
,('20', '2', '10', 'expert')
,('21', '3', '1', 'advanced')
,('22', '3', '2', 'advanced')
,('23', '3', '3', 'basic')
,('24', '3', '4', 'intermediate')
,('25', '3', '5', 'expert')
,('26', '3', '6', 'basic')
,('27', '3', '7', 'advanced')
,('28', '3', '8', 'intermediate')
,('29', '3', '9', 'basic')
,('30', '3', '10', 'expert')
,('31', '4', '1', 'basic')
,('32', '4', '2', 'intermediate')
,('33', '4', '3', 'intermediate')
,('34', '4', '4', 'expert')
,('35', '4', '5', 'advanced')
,('36', '4', '6', 'expert')
,('37', '4', '7', 'advanced')
,('38', '4', '8', 'basic')
,('39', '4', '9', 'intermediate')
,('40', '4', '10', 'advanced')
,('41', '5', '1', 'expert')
,('42', '5', '2', 'basic')
,('43', '5', '3', 'expert')
,('44', '5', '4', 'intermediate')
,('45', '5', '5', 'expert')
,('46', '5', '6', 'expert')
,('47', '5', '7', 'basic')
,('48', '5', '8', 'basic')
,('49', '5', '9', 'expert')
,('50', '5', '10', 'intermediate')
,('51', '6', '1', 'advanced')
,('52', '6', '2', 'intermediate')
,('53', '6', '3', 'basic')
,('54', '6', '4', 'basic')
,('55', '6', '5', 'intermediate')
,('56', '6', '6', 'expert')
,('57', '6', '7', 'basic')
,('58', '6', '8', 'expert')
,('59', '6', '9', 'advanced')
,('60', '6', '10', 'advanced')
,('61', '7', '1', 'expert')
,('62', '7', '2', 'advanced')
,('63', '7', '3', 'advanced')
,('64', '7', '4', 'advanced')
,('65', '7', '5', 'intermediate')
,('66', '7', '6', 'intermediate')
,('67', '7', '7', 'expert')
,('68', '7', '8', 'advanced')
,('69', '7', '9', 'expert')
,('70', '7', '10', 'basic')
,('71', '8', '1', 'expert')
,('72', '8', '2', 'advanced')
,('73', '8', '3', 'expert')
,('74', '8', '4', 'expert')
,('75', '8', '5', 'intermediate')
,('76', '8', '6', 'basic')
,('77', '8', '7', 'advanced')
,('78', '8', '8', 'advanced')
,('79', '8', '9', 'basic')
,('80', '8', '10', 'intermediate')
,('81', '9', '1', 'intermediate')
,('82', '9', '2', 'expert')
,('83', '9', '3', 'advanced')
,('84', '9', '4', 'expert')
,('85', '9', '5', 'intermediate')
,('86', '9', '6', 'expert')
,('87', '9', '7', 'intermediate')
,('88', '9', '8', 'intermediate')
,('89', '9', '9', 'basic')
,('90', '9', '10', 'advanced')
,('91', '10', '1', 'advanced')
,('92', '10', '2', 'advanced')
,('93', '10', '3', 'advanced')
,('94', '10', '4', 'intermediate')
,('95', '10', '5', 'basic')
,('96', '10', '6', 'basic')
,('97', '10', '7', 'advanced')
,('98', '10', '8', 'expert')
,('99', '10', '9', 'advanced')
,('100', '10', '10', 'basic')
,('101', '11', '1', 'advanced')
,('102', '11', '2', 'basic')
,('103', '11', '3', 'advanced')
,('104', '11', '4', 'expert')
,('105', '11', '5', 'expert')
,('106', '11', '6', 'expert')
,('107', '11', '7', 'intermediate')
,('108', '11', '8', 'intermediate')
,('109', '11', '9', 'advanced')
,('110', '11', '10', 'basic')
,('111', '12', '1', 'advanced')
,('112', '12', '2', 'intermediate')
,('113', '12', '3', 'advanced')
,('114', '12', '4', 'expert')
,('115', '12', '5', 'expert')
,('116', '12', '6', 'intermediate')
,('117', '12', '7', 'intermediate')
,('118', '12', '8', 'expert')
,('119', '12', '9', 'expert')
,('120', '12', '10', 'expert')
,('121', '13', '1', 'expert')
,('122', '13', '2', 'expert')
,('123', '13', '3', 'intermediate')
,('124', '13', '4', 'intermediate')
,('125', '13', '5', 'expert')
,('126', '13', '6', 'advanced')
,('127', '13', '7', 'expert')
,('128', '13', '8', 'expert')
,('129', '13', '9', 'basic')
,('130', '13', '10', 'basic')
,('131', '14', '1', 'basic')
,('132', '14', '2', 'advanced')
,('133', '14', '3', 'intermediate')
,('134', '14', '4', 'basic')
,('135', '14', '5', 'intermediate')
,('136', '14', '6', 'basic')
,('137', '14', '7', 'basic')
,('138', '14', '8', 'basic')
,('139', '14', '9', 'intermediate')
,('140', '14', '10', 'advanced')
,('141', '15', '1', 'intermediate')
,('142', '15', '2', 'advanced')
,('143', '15', '3', 'expert')
,('144', '15', '4', 'basic')
,('145', '15', '5', 'intermediate')
,('146', '15', '6', 'basic')
,('147', '15', '7', 'advanced')
,('148', '15', '8', 'advanced')
,('149', '15', '9', 'intermediate')
,('150', '15', '10', 'expert')
,('151', '16', '1', 'advanced')
,('152', '16', '2', 'intermediate')
,('153', '16', '3', 'basic')
,('154', '16', '4', 'basic')
,('155', '16', '5', 'basic')
,('156', '16', '6', 'advanced')
,('157', '16', '7', 'expert')
,('158', '16', '8', 'intermediate')
,('159', '16', '9', 'basic')
,('160', '16', '10', 'intermediate')
,('161', '17', '1', 'basic')
,('162', '17', '2', 'advanced')
,('163', '17', '3', 'advanced')
,('164', '17', '4', 'advanced')
,('165', '17', '5', 'basic')
,('166', '17', '6', 'expert')
,('167', '17', '7', 'basic')
,('168', '17', '8', 'basic')
,('169', '17', '9', 'expert')
,('170', '17', '10', 'basic')
,('171', '18', '1', 'advanced')
,('172', '18', '2', 'intermediate')
,('173', '18', '3', 'basic')
,('174', '18', '4', 'basic')
,('175', '18', '5', 'basic')
,('176', '18', '6', 'advanced')
,('177', '18', '7', 'advanced')
,('178', '18', '8', 'basic')
,('179', '18', '9', 'basic')
,('180', '18', '10', 'basic')
,('181', '19', '1', 'expert')
,('182', '19', '2', 'intermediate')
,('183', '19', '3', 'basic')
,('184', '19', '4', 'expert')
,('185', '19', '5', 'intermediate')
,('186', '19', '6', 'expert')
,('187', '19', '7', 'advanced')
,('188', '19', '8', 'basic')
,('189', '19', '9', 'intermediate')
,('190', '19', '10', 'intermediate')
,('191', '20', '1', 'advanced')
,('192', '20', '2', 'advanced')
,('193', '20', '3', 'advanced')
,('194', '20', '4', 'basic')
,('195', '20', '5', 'expert')
,('196', '20', '6', 'advanced')
,('197', '20', '7', 'advanced')
,('198', '20', '8', 'advanced')
,('199', '20', '9', 'expert')
,('200', '20', '10', 'basic');
