// Creating object with accessors
wizard = {
    staff: "Red",

    display: () => {console.log("Zapp!")},

    get get_staff(){
        return this.staff;
    },

    set set_staff(new_Staff){
        this.staff = new_Staff;
    } 
}

wizard.display();

// Using accessors
console.log(wizard.get_staff);
wizard.set_staff = "Blue";
console.log(wizard.get_staff);

// Adding new attribute:
wizard.cape = "Black";
console.log(wizard.cape);

// Adding new method:
wizard.spell = () => {console.log("Boom!")};
wizard.spell();

// Adding new property:
Object.defineProperty(wizard, 'wand', {
    get() {return this.wand_name;},
    set(new_name) {this.wand_name = new_name;},
});

console.log(wizard.wand);

wizard.wand = "Life";
console.log(wizard.wand);

wizard.wand = "Death";
console.log(wizard.wand);

// You can do add attributes, methods and properties without using Object.defineProperty 
// This method allows these extra details to be changed from their defaults.