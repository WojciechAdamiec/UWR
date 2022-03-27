#include <iostream>
#include <random>
#include <deque>
#include <algorithm>

using namespace std;


class Person{
    public:
        string name;
        string surname;
        int age;
        double weight;
        double height;
    
        Person(string name, string surname, int age, double weight, double height)
            : name{name}, surname{surname}, age{age}, weight{weight}, height{height}{}
        
        void info(){
            cout << "\nname: " << name << " surname: " << surname << " age: " << age << " weight: " << weight << " height: " << height;
        }
};

bool operator== (const Person &a, const Person &b){
            return (a.name == b.name && a.surname == b.surname);
        }

int main() {

    // Create Deck
    deque<Person> Deck{
        Person("Adam", "Kowalski", 17, 72, 174),
        Person("Jan", "Kowalski", 46, 88, 177),
        Person("Barbara", "Kowalska", 37, 52, 161),
        Person("Adam", "Nowak", 68, 72, 179),
        Person("Szymon", "Koniecpolski", 62, 82, 186),
        Person("Bartosz", "Braniecki", 24, 122, 191),
        Person("Joanna", "Kowalska", 26, 72, 159),
        Person("Katarzyna", "Szydło", 28, 91, 171),
        Person("Zuzanna", "Nowak", 52, 62, 162),
        Person("Mateusz", "Jackowski", 33, 56, 173),
        Person("Godfryd", "Duda", 37, 81, 172)
                    };


    // Show content of Deck
    cout << "================\n";
    cout << "Unmodified table\n";
    cout << "================\n";
    for_each(Deck.begin(), Deck.end(), [](auto p){p.info();});

    // A. Sort by BMI
    sort(Deck.begin(), Deck.end(), [](auto a, auto b)
        {return (a.weight/(a.height * a.height)) <= (b.weight/(b.height * b.height));});

    cout << "\n\n";

    // Show content of Deck
    cout << "================\n";
    cout << "Sorted by BMI table\n";
    cout << "================\n";
    for_each(Deck.begin(), Deck.end(), [](auto p){p.info();});

    // B. Apply diet
    for_each(Deck.begin(), Deck.end(), [&](auto &p){p.weight = p.weight * 0.9;});
    cout << "\n\n";

    // Show content of Deck
    cout << "================\n";
    cout << "Diet applied table\n",
    cout << "================\n";
    for_each(Deck.begin(), Deck.end(), [](auto p){p.info();});

    // C. Divide into groups
    cout << "\n\n";
    cout << "================\n";
    cout << "Divide into groups\n";
    cout << "================\n";
    deque<Person> H;
    deque<Person> L;
    copy_if (Deck.begin(), Deck.end(), back_inserter(H), [](auto p){return p.weight > 100;} );
    copy_if (Deck.begin(), Deck.end(), back_inserter(L), [](auto p){return p.weight <= 100;} );
    cout << "Heavy people:";
    for_each(H.begin(), H.end(), [&](auto p){p.info();});
    cout << "\nLight people:";
    for_each(L.begin(), L.end(), [&](auto p){p.info();});
                                            
    // D. Set average height person in the middle
    deque<Person> aux = Deck;
    nth_element(aux.begin(), aux.begin() + aux.size()/2, aux.end(), [](auto a, auto b){return a.height > b.height;});
    auto it = find(Deck.begin(), Deck.end(), aux.at(5));
    swap(Deck.at(5), *it);
    cout << "\n\n";

    // Show content of Deck
    cout << "================\n";
    cout << "Set average height person in the middle\n";
    cout << "================\n";

    for_each(Deck.begin(), Deck.end(), [](auto p){p.info();});

    // E. Randomly reshape people
    random_device rd;
    mt19937 g(rd());
    shuffle(Deck.begin(), Deck.begin() + 4, g);
    shuffle(Deck.begin() + 6, Deck.end(), g);
    cout << "\n\n";

    // Show content of Deck
    cout << "================\n";
    cout << "Randomly reshape people\n";
    cout << "================\n";
    for_each(Deck.begin(), Deck.end(), [](auto p){p.info();});

    // F. Print the youngest and the oldest
    cout << "\n\n";
    cout << "================\n";
    cout << "Print the youngest and the oldest\n";
    cout << "================\n";
    
    auto res = minmax_element(Deck.begin(), Deck.end(), [](Person a, Person b){return a.age < b.age;});
    (*res.first).info();
    (*res.second).info();

    return 0;
}