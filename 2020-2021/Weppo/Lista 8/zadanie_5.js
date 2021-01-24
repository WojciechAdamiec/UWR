/*
Tutaj dowód na to, że faktycznie utworzyłem wymagane tabele

CREATE TABLE [dbo].[PERSON](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](20) NOT NULL,
 CONSTRAINT [PK_PERSON] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[WORKPLACE](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](20) NOT NULL,
 CONSTRAINT [PK_WORKPLACE] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]

CREATE TABLE [dbo].[PERSONWORKPLACE](
	[ID_PERSON] [int] NOT NULL,
	[ID_WORKPLACE] [int] NOT NULL,
 CONSTRAINT [PK_PERSONWORKPLACE_1] PRIMARY KEY CLUSTERED 
(
	[ID_PERSON] ASC,
	[ID_WORKPLACE] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[PERSONWORKPLACE]  WITH CHECK ADD  CONSTRAINT [FK_PERSONWORKPLACE_PERSON] FOREIGN KEY([ID_PERSON])
REFERENCES [dbo].[PERSON] ([ID])
GO

ALTER TABLE [dbo].[PERSONWORKPLACE] CHECK CONSTRAINT [FK_PERSONWORKPLACE_PERSON]
GO

ALTER TABLE [dbo].[PERSONWORKPLACE]  WITH CHECK ADD  CONSTRAINT [FK_PERSONWORKPLACE_WORKPLACE] FOREIGN KEY([ID_WORKPLACE])
REFERENCES [dbo].[WORKPLACE] ([ID])
GO

ALTER TABLE [dbo].[PERSONWORKPLACE] CHECK CONSTRAINT [FK_PERSONWORKPLACE_WORKPLACE]
GO
*/

var mssql = require('mssql');

class PersonRepository {
    constructor(conn) {
        this.conn = conn;
    }

    /*
    Tutaj zaimplenetowałem podgląd bazy danych:
    Wypisuje wszystkie pary: Person.Name i Workplace.Name (takie, że Person pracuje w Workplace)
    */

    async retrieve() {
        try {
            var req = new mssql.Request(this.conn);
            var res = await req.query(
                    'SELECT PERSON.Name, WORKPLACE.Name FROM PERSON INNER JOIN PERSONWORKPLACE ON PERSON.ID = PERSONWORKPLACE.ID_PERSON INNER JOIN WORKPLACE ON PERSONWORKPLACE.ID_WORKPLACE = WORKPLACE.ID'
                );
            return res.recordset;
        }
        catch (err) {
            console.log(err);
            return [];
        }
    }

    /*
    Tutaj zaimplenetowałem scenariusz dodania jednego 'procesu biznesowego'.
    Jest to lekka modyfikacja tego z poprzedniego zadania.
    */
    async add(item) {
        try{
            var req = new mssql.Request(this.conn);
            req.input("Name", item.WorkplaceName);
            
            var res1 = await req.query('insert into WORKPLACE (Name)values(@Name) select scope_identity() as id');
            var workplace_id = res1.recordset[0].id;
            
            var req = new mssql.Request(this.conn);
            req.input("Name", item.PersonName);
            var res2 = await req.query('insert into PERSON (Name)values(@Name) select scope_identity() as id');
            var person_id = res2.recordset[0].id;
            
            req.input("person_id", person_id);
            req.input("workplace_id", workplace_id);
            var res3 = await req.query('insert into PERSONWORKPLACE (ID_PERSON, ID_WORKPLACE)values(@person_id, @workplace_id)')
        }
        catch (err) {
            console.log(err);
            throw err;
        }
    }
}

async function main() {
    var conn = new
        mssql.ConnectionPool('server=localhost,1433;database=Zadanie5;user id=foo; password=foo');

    try {
        await conn.connect();

        var repo = new PersonRepository(conn);

        // pobierz wszystkie rekordy
        var items = await repo.retrieve();

        items.forEach(e => {
            console.log(JSON.stringify(e));
        });

        item = {WorkplaceName : 'Air Force One', PersonName : 'Steward'};
        repo.add(item);

        console.log('Added new entry');
    }
    catch (err) {
        if (conn.connected)
            conn.close();
        console.log(err);
    }
}

main();

/*
Tabele PRZED:

PERSON
ID	Name
1	Janusz
2	Maciej
3	Wulfgang

WORKPLACE
ID	Name
1	Huta Silesia
2	Port Lotniczy

PERSONWORKPLACE
ID_PERSON	ID_WORKPLACE
1	        1
2	        1
3	        1
3	        2

Tabele PO:

PERSON
ID	Name
1	Janusz
2	Maciej
3	Wulfgang
4   Steward

WORKPLACE
ID	Name
1	Huta Silesia
2	Port Lotniczy
3   Air Force One

PERSONWORKPLACE
ID_PERSON	ID_WORKPLACE
1	        1
2	        1
3	        1
3	        2
4           3
*/
