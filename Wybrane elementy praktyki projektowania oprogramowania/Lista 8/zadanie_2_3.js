var mssql = require('mssql');

class PersonRepository {
    constructor(conn) {
        this.conn = conn;
    }

    async retrieve(name = null) {
        try {
            var req = new mssql.Request(this.conn);
            if (name) req.input('Name', name);
            var res = await req.query('select * from PERSON' + (name ? 'where Name=@name' : '') );
            return name ? res.recordset[0] : res.recordset;
        }
        catch (err) {
            console.log(err);
            return [];
        }
    }

    async insert(newPerson) {
        if (!newPerson) return;
        try {
            var req = new mssql.Request(this.conn);
            req.input("Name", newPerson.Name);
            var res = await req.query('insert into PERSON (Name)values(@Name) select scope_identity() as id');
            return res.recordset[0].id;
        }
        catch (err) {
            console.log(err);
            throw err;
        }
    }

    async update(newPerson) {
        if (!newPerson || !newPerson.ID) return;
        try {
            var req = new mssql.Request(this.conn);
            req.input("ID", newPerson.ID);
            req.input("Name", newPerson.Name);
            var ret = await req.query('update PERSON set Name=@Name where ID=@ID');
            return ret.rowsAffected[0];
        }
        catch (err) {
            console.log(err);
            throw err;
        }
    }

    async delete(name) {
        try {
            var req = new mssql.Request(this.conn);
            req.input("Name", name);
            var ret = await req.query('delete from PERSON where Name=@Name');
            return ret.rowsAffected[0];
        }
        catch (err) {
            console.log(err);
            throw err;
        }
    }
}

async function main() {
    var conn = new
        mssql.ConnectionPool('server=localhost,1433;database=Zadanie1;user id=foo; password=foo');

    try {
        await conn.connect();

        var repo = new PersonRepository(conn);

        // pobierz wszystkie rekordy
        var items = await repo.retrieve();

        items.forEach(e => {
            console.log(JSON.stringify(e));
        });
        
        // dodaj nowy rekord
        var item1 = {Name : 'Janusz'};
        var id = await repo.insert(item1);

        console.log(`identyfikator nowo wstawionego rekordu ${id}`);

        // zmodyfikuj istniejący rekord
        var item2 = {Name : 'Lucyfer', ID : 1};
        var rowsAffected = await repo.update(item2);

        console.log(`zmodyfikowano ${rowsAffected} rekordów`);

        // usuń istniejący rekord
        var rows = await repo.delete('Jadwiga');
        console.log(`usunięto ${rows} rekordów`);
    }
    catch (err) {
        if (conn.connected)
            conn.close();
        console.log(err);
    }
}

main();
