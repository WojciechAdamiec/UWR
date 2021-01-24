/*
Tutaj dowód na to, że faktycznie utworzyłem wymagane tabele

CREATE TABLE [dbo].[PERSON](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](20) NOT NULL,
	[ID_WORKPLACE] [int] NULL,
 CONSTRAINT [PK_PERSON] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[PERSON]  WITH CHECK ADD  CONSTRAINT [FK_PERSON_WORKPLACE] FOREIGN KEY([ID_WORKPLACE])
REFERENCES [dbo].[WORKPLACE] ([ID])
GO

ALTER TABLE [dbo].[PERSON] CHECK CONSTRAINT [FK_PERSON_WORKPLACE]
GO

CREATE TABLE [dbo].[WORKPLACE](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[NAME] [nvarchar](20) NOT NULL,
 CONSTRAINT [PK_WORKPLACE] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
*/

var mssql = require('mssql');

class PersonRepository {
    constructor(conn) {
        this.conn = conn;
    }

    /*
    Tutaj zaimplenetowałem scenariusz dodania jednego 'procesu biznesowego'
    */

    async add(item) {
        try{
            var req = new mssql.Request(this.conn);
            req.input("Name", item.WorkplaceName);
            
            var res1 = await req.query('insert into WORKPLACE (Name)values(@Name) select scope_identity() as id');
            var id = res1.recordset[0].id;
            
            var req = new mssql.Request(this.conn);
            req.input("Name", item.PersonName);
            req.input("ID", id);
            var res2 = await req.query('insert into PERSON (Name, ID_WORKPLACE)values(@Name, @ID)');
        }
        catch (err) {
            console.log(err);
            throw err;
        }
    }
}

async function main() {
    var conn = new
        mssql.ConnectionPool('server=localhost,1433;database=Zadanie4;user id=foo; password=foo');

    try {
        await conn.connect();

        var repo = new PersonRepository(conn);
        item = {WorkplaceName : 'Air Force One', PersonName : 'Steward'};
        repo.add(item);

    }
    catch (err) {
        if (conn.connected)
            conn.close();
        console.log(err);
    }
}

main();

/*
Tabele w bazie po wykonaniu programu wyglądają tak:
Biorąc pod uwagę, że wcześniejsze wiersze są efektem moich testów uznaje zadanie za wykonane.

WORKPLACE
ID	NAME
1	Huta Silesia
2	Nokia
3	Kopalnia Wujek
4	Air Force One

ID	Name	ID_WORKPLACE
3	Janusz	1
4	Bohdan	2
5	Michal	2
6	Steward	4
*/



