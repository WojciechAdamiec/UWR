/*
Uzasadnienie typów:
Dla 'Name' i 'Surname' wybrałem nvarchar(20), bo to najwygodniejszy typ dla stringa długości co najwyżej 20 znakowej.
Dla 'Sex' wybrałem nchar(1), konwencja jest taka, że 'F' oznacza female i 'M' oznacza male.
Dla 'Age' wybrałem tinyint, bo przedział 0-255 jest najmniejszym znalezielonym przeze mnie przedziałem spełniającym wymagania kolumny.
*/

/* 1) */

CREATE SEQUENCE [dbo].[Sequence1] 
 AS [bigint]
 START WITH 1
 INCREMENT BY 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 CACHE 


CREATE TABLE [dbo].[PERSON1](
	[ID] [bigint] NOT NULL,
	[Name] [nvarchar](20) NOT NULL,
	[Surname] [nvarchar](20) NOT NULL,
	[Sex] [nchar](1) NOT NULL,
	[Age] [tinyint] NOT NULL,
 CONSTRAINT [PK_PERSON1] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]


INSERT INTO PERSON1 VALUES (NEXT VALUE FOR Sequence1, 'Wojciech', 'Adamiec', 'M', 21)

/* 2) */

CREATE TABLE [dbo].[PERSON](
	[Name] [nvarchar](20) NOT NULL,
	[Surname] [nvarchar](20) NOT NULL,
	[Sex] [nchar](1) NOT NULL,
	[Age] [tinyint] NOT NULL,
	[ID] [int] IDENTITY(1,1) NOT NULL,
 CONSTRAINT [PK_PERSON] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

/* Insert */

insert into PERSON
(Name, Surname, Sex, Age)
values
('Wojciech', 'Adamiec', 'M', 21),
('Alfred', 'Nobel', 'M', 188),
('Angela', 'Merkel', 'F', 66),
('Jadwiga', 'Emilewicz', 'F', 46)

/* Select */

select * from PERSON

select Name, Surname from PERSON