/*import my_table (
  id,
  email,
  company,
  title,
  education,
  yearsExp,
  baseSalary,
  bonuses,
  gender,
  race
) csv data (‘nodelocal://2/Users/april/Desktop/user_data_ex.csv’);
*/

/* Example data entries */


CREATE TABLE user_table (
	id int primary key,
	email varchar(100) not null,
	company varchar(100) not null,
	title varchar(100) not null,
	education varchar(100) not null,
	yearsExp int default 0,
	baseSalary int default 0,
	bonuses int default 0,
	gender varchar(15) not null,
	race varchar(50) not null
);

INSERT INTO user_table (id, email, company, title, education, yearsExp, baseSalary, bonuses, gender, race)
VALUES(1,	'a@g.mail',	'NASA JPL','Associate Software Engineer',	'Bachelors',	2,	90000,	20000,	'female',	'asian'),
      (2,	'b@g.mail',	'SpaceX',  'Senior Software Engineer',	  'Bachelors',	10,	190000,	45000,	'male',  	'white'),
      (3,	'c@g.mail',	'Rescale', 'Data Scientist', 	            'Masters',    5,	130000,	35000,	'male',	  'black/afr'),
      (4,	'd@g.mail',	'Google',	 'Associate Software Engineer',	'Bachelors',	3,	120000,	15000,	'male',	  'asian'),
      (5,	'e@g.mail',	'Google',	 'Associate Software Engineer',	'Bachelors',	4,	120000,	10000,	'female',	'amerInd/alaskaNat'),
      (6,	'f@g.mail',	'SpaceX',	 'Associate Software Engineer',	'Bachelors',	3,	140000, 23000,	'male',	  'black/afr'),
      (7,	'g@g.mail',	'SpaceX',	 'HR Recruiter',	              'Bachelors',	3,	90000,	15000,	'male',	  'white'),
      (8,	'h@g.mail',	'SpaceX',	 'Software Engineer',	          'Bachelors',	5,	165000,	20000,	'male',	  'natHawaii/pacIsland'),
      (9,	'i@g.mail',	'NASA JPL','Associate Software Engineer',	'Bachelors',	2,	92000,	20000,	'male',	  'asian'),
      (10,'j@g.mail',	'Google',	 'Software Engineer',	          'Bachelors',	5,	145000,	25000,	'female',	'black/afr');
