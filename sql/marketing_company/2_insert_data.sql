-- Asignación de empleados al departamento de Marketing
INSERT INTO employee_department (id, employee_id, department_id, role, effective_date) VALUES
(1, 1, 1, 'Manager', '2021-01-10'), 
(2, 2, 1, 'Worker', '2021-02-15'),  
(3, 3, 1, 'Worker', '2021-03-20'),  
(4, 4, 1, 'Worker', '2021-04-05'),  
(5, 5, 1, 'Worker', '2021-05-12'),  
(6, 6, 1, 'Worker', '2021-06-18'),  
(7, 7, 1, 'Worker', '2021-07-22');

-- Asignación de empleados al departamento de Sales
INSERT INTO employee_department (id, employee_id, department_id, role, effective_date) VALUES
(8, 8, 2, 'Manager', '2020-05-20'),  
(9, 9, 2, 'Worker', '2020-06-15'),   
(10, 10, 2, 'Worker', '2020-07-10'), 
(11, 11, 2, 'Worker', '2020-08-01'), 
(12, 12, 2, 'Worker', '2020-09-10'), 
(13, 13, 2, 'Worker', '2020-10-20'), 
(14, 14, 2, 'Worker', '2020-11-15');
-- Asignación de empleados al departamento de Human Resources
INSERT INTO employee_department (id, employee_id, department_id, role, effective_date) VALUES
(15, 15, 3, 'Manager', '2019-03-25'), 
(16, 16, 3, 'Worker', '2019-04-30'),  
(17, 17, 3, 'Worker', '2019-05-10'),  
(18, 18, 3, 'Worker', '2019-06-01'),  
(19, 19, 3, 'Worker', '2019-07-12'),  
(20, 20, 3, 'Worker', '2019-08-20');  


-- Competencias para el departamento de Marketing
INSERT INTO competency_level (id, competency_id, department_id, required_level, num_workers) VALUES
(1, 1, 1, 'Advanced', 1),   
(2, 2, 1, 'Intermediate', 3),
(3, 3, 1, 'Advanced', 1),   
(4, 5, 1, 'Beginner', 2);   

-- Competencias para el departamento de Sales
INSERT INTO competency_level (id, competency_id, department_id, required_level, num_workers) VALUES
(5, 7, 2, 'Expert', 1),      
(6, 3, 2, 'Advanced', 2),    
(7, 9, 2, 'Intermediate', 3);

-- Competencias para el departamento de Human Resources (HR)
INSERT INTO competency_level (id, competency_id, department_id, required_level, num_workers) VALUES
(8, 1, 3, 'Advanced', 1),     
(9, 10, 3, 'Intermediate', 3),
(10, 6, 3, 'Intermediate', 2);



INSERT INTO employee_competency (id, employee_id, competency_id, current_level) VALUES
('1', '1', '1', 'Intermediate')
,('2', '1', '2', 'Intermediate')
,('3', '1', '3', 'Expert')
,('4', '1', '4', 'Basic')
,('5', '1', '5', 'Intermediate')
,('6', '1', '6', 'Advanced')
,('7', '1', '7', 'Basic')
,('8', '1', '8', 'Intermediate')
,('9', '1', '9', 'Intermediate')
,('10', '1', '10', 'Expert')
,('11', '2', '1', 'Basic')
,('12', '2', '2', 'Intermediate')
,('13', '2', '3', 'Expert')
,('14', '2', '4', 'Advanced')
,('15', '2', '5', 'Expert')
,('16', '2', '6', 'Expert')
,('17', '2', '7', 'Intermediate')
,('18', '2', '8', 'Expert')
,('19', '2', '9', 'Basic')
,('20', '2', '10', 'Expert')
,('21', '3', '1', 'Advanced')
,('22', '3', '2', 'Advanced')
,('23', '3', '3', 'Basic')
,('24', '3', '4', 'Intermediate')
,('25', '3', '5', 'Expert')
,('26', '3', '6', 'Basic')
,('27', '3', '7', 'Advanced')
,('28', '3', '8', 'Intermediate')
,('29', '3', '9', 'Basic')
,('30', '3', '10', 'Expert')
,('31', '4', '1', 'Basic')
,('32', '4', '2', 'Intermediate')
,('33', '4', '3', 'Intermediate')
,('34', '4', '4', 'Expert')
,('35', '4', '5', 'Advanced')
,('36', '4', '6', 'Expert')
,('37', '4', '7', 'Advanced')
,('38', '4', '8', 'Basic')
,('39', '4', '9', 'Intermediate')
,('40', '4', '10', 'Advanced')
,('41', '5', '1', 'Expert')
,('42', '5', '2', 'Basic')
,('43', '5', '3', 'Expert')
,('44', '5', '4', 'Intermediate')
,('45', '5', '5', 'Expert')
,('46', '5', '6', 'Expert')
,('47', '5', '7', 'Basic')
,('48', '5', '8', 'Basic')
,('49', '5', '9', 'Expert')
,('50', '5', '10', 'Intermediate')
,('51', '6', '1', 'Advanced')
,('52', '6', '2', 'Intermediate')
,('53', '6', '3', 'Basic')
,('54', '6', '4', 'Basic')
,('55', '6', '5', 'Intermediate')
,('56', '6', '6', 'Expert')
,('57', '6', '7', 'Basic')
,('58', '6', '8', 'Expert')
,('59', '6', '9', 'Advanced')
,('60', '6', '10', 'Advanced')
,('61', '7', '1', 'Expert')
,('62', '7', '2', 'Advanced')
,('63', '7', '3', 'Advanced')
,('64', '7', '4', 'Advanced')
,('65', '7', '5', 'Intermediate')
,('66', '7', '6', 'Intermediate')
,('67', '7', '7', 'Expert')
,('68', '7', '8', 'Advanced')
,('69', '7', '9', 'Expert')
,('70', '7', '10', 'Basic')
,('71', '8', '1', 'Expert')
,('72', '8', '2', 'Advanced')
,('73', '8', '3', 'Expert')
,('74', '8', '4', 'Expert')
,('75', '8', '5', 'Intermediate')
,('76', '8', '6', 'Basic')
,('77', '8', '7', 'Advanced')
,('78', '8', '8', 'Advanced')
,('79', '8', '9', 'Basic')
,('80', '8', '10', 'Intermediate')
,('81', '9', '1', 'Intermediate')
,('82', '9', '2', 'Expert')
,('83', '9', '3', 'Advanced')
,('84', '9', '4', 'Expert')
,('85', '9', '5', 'Intermediate')
,('86', '9', '6', 'Expert')
,('87', '9', '7', 'Intermediate')
,('88', '9', '8', 'Intermediate')
,('89', '9', '9', 'Basic')
,('90', '9', '10', 'Advanced')
,('91', '10', '1', 'Advanced')
,('92', '10', '2', 'Advanced')
,('93', '10', '3', 'Advanced')
,('94', '10', '4', 'Intermediate')
,('95', '10', '5', 'Basic')
,('96', '10', '6', 'Basic')
,('97', '10', '7', 'Advanced')
,('98', '10', '8', 'Expert')
,('99', '10', '9', 'Advanced')
,('100', '10', '10', 'Basic')
,('101', '11', '1', 'Advanced')
,('102', '11', '2', 'Basic')
,('103', '11', '3', 'Advanced')
,('104', '11', '4', 'Expert')
,('105', '11', '5', 'Expert')
,('106', '11', '6', 'Expert')
,('107', '11', '7', 'Intermediate')
,('108', '11', '8', 'Intermediate')
,('109', '11', '9', 'Advanced')
,('110', '11', '10', 'Basic')
,('111', '12', '1', 'Advanced')
,('112', '12', '2', 'Intermediate')
,('113', '12', '3', 'Advanced')
,('114', '12', '4', 'Expert')
,('115', '12', '5', 'Expert')
,('116', '12', '6', 'Intermediate')
,('117', '12', '7', 'Intermediate')
,('118', '12', '8', 'Expert')
,('119', '12', '9', 'Expert')
,('120', '12', '10', 'Expert')
,('121', '13', '1', 'Expert')
,('122', '13', '2', 'Expert')
,('123', '13', '3', 'Intermediate')
,('124', '13', '4', 'Intermediate')
,('125', '13', '5', 'Expert')
,('126', '13', '6', 'Advanced')
,('127', '13', '7', 'Expert')
,('128', '13', '8', 'Expert')
,('129', '13', '9', 'Basic')
,('130', '13', '10', 'Basic')
,('131', '14', '1', 'Basic')
,('132', '14', '2', 'Advanced')
,('133', '14', '3', 'Intermediate')
,('134', '14', '4', 'Basic')
,('135', '14', '5', 'Intermediate')
,('136', '14', '6', 'Basic')
,('137', '14', '7', 'Basic')
,('138', '14', '8', 'Basic')
,('139', '14', '9', 'Intermediate')
,('140', '14', '10', 'Advanced')
,('141', '15', '1', 'Intermediate')
,('142', '15', '2', 'Advanced')
,('143', '15', '3', 'Expert')
,('144', '15', '4', 'Basic')
,('145', '15', '5', 'Intermediate')
,('146', '15', '6', 'Basic')
,('147', '15', '7', 'Advanced')
,('148', '15', '8', 'Advanced')
,('149', '15', '9', 'Intermediate')
,('150', '15', '10', 'Expert')
,('151', '16', '1', 'Advanced')
,('152', '16', '2', 'Intermediate')
,('153', '16', '3', 'Basic')
,('154', '16', '4', 'Basic')
,('155', '16', '5', 'Basic')
,('156', '16', '6', 'Advanced')
,('157', '16', '7', 'Expert')
,('158', '16', '8', 'Intermediate')
,('159', '16', '9', 'Basic')
,('160', '16', '10', 'Intermediate')
,('161', '17', '1', 'Basic')
,('162', '17', '2', 'Advanced')
,('163', '17', '3', 'Advanced')
,('164', '17', '4', 'Advanced')
,('165', '17', '5', 'Basic')
,('166', '17', '6', 'Expert')
,('167', '17', '7', 'Basic')
,('168', '17', '8', 'Basic')
,('169', '17', '9', 'Expert')
,('170', '17', '10', 'Basic')
,('171', '18', '1', 'Advanced')
,('172', '18', '2', 'Intermediate')
,('173', '18', '3', 'Basic')
,('174', '18', '4', 'Basic')
,('175', '18', '5', 'Basic')
,('176', '18', '6', 'Advanced')
,('177', '18', '7', 'Advanced')
,('178', '18', '8', 'Basic')
,('179', '18', '9', 'Basic')
,('180', '18', '10', 'Basic')
,('181', '19', '1', 'Expert')
,('182', '19', '2', 'Intermediate')
,('183', '19', '3', 'Basic')
,('184', '19', '4', 'Expert')
,('185', '19', '5', 'Intermediate')
,('186', '19', '6', 'Expert')
,('187', '19', '7', 'Advanced')
,('188', '19', '8', 'Basic')
,('189', '19', '9', 'Intermediate')
,('190', '19', '10', 'Intermediate')
,('191', '20', '1', 'Advanced')
,('192', '20', '2', 'Advanced')
,('193', '20', '3', 'Advanced')
,('194', '20', '4', 'Basic')
,('195', '20', '5', 'Expert')
,('196', '20', '6', 'Advanced')
,('197', '20', '7', 'Advanced')
,('198', '20', '8', 'Advanced')
,('199', '20', '9', 'Expert')
,('200', '20', '10', 'Basic');
