
#include <iostream>
#include <cstdint>
#include <set>
#include <cmath> 

enum Names : uint16_t {Joanna, Tomasz, Jakub};
void info(std::string komunikat, enum Names imie)
{
    switch (imie)
    {
        case Names::Joanna:
            std::cout << komunikat << " to Joanna \n";
            break;
        case Names::Tomasz:
            std::cout << komunikat << " to Tomasz \n";
            break;
        case Names::Jakub:
            std::cout << komunikat << " to Jakub \n";
            break;
        default:
            std::cout << "Error";
            break;
    }
}

auto lucas(uint32_t num){
    if (num == 0){
        return 2;
    }
    if (num == 1){
        return 1;
    }
    return lucas(num - 2) + lucas(num - 1);
}

void delta(float a, float b, float c){
    if (float result = b * b - 4 * a * c; result > 0){
        float x1 = (-b - std::sqrt(result))/(2 * a);
        float x2 = (-b + std::sqrt(result))/(2 * a);
        std::cout << "Miejsca zerowe: " << x1 << " i "<< x2 << "\n";
    }
    else if (result == 0){
        float x = -b / (2 * a);
        std::cout << "Miejsce zerowe: " << x << "\n";
    }
    else{
        std::cout << "Brak miejsca zerowego! \n";
    }
}

void calendar(std::string data){
    switch (int month = std::stoi(data.substr(3, 2)), day = std::stoi(data.substr(0, 2)), year = std::stoi(data.substr(6, 4)); month) 
   { 
        case 1:
            std::cout<<day<<" "<< "stycznia "<<year<<"\n"; 
            break; 
        case 2:
            std::cout<<day<<" "<< "lutego "<<year<<"\n"; 
            break; 
        case 3:
            std::cout<<day<<" "<< "marca "<<year<<"\n"; 
            break;
        case 4:
            std::cout<<day<<" "<< "kwietnia "<<year<<"\n"; 
            break; 
        case 5:
            std::cout<<day<<" "<< "maja "<<year<<"\n"; 
            break; 
        case 6:
            std::cout<<day<<" "<< "czerwca "<<year<<"\n"; 
            break; 
        case 7:
            std::cout<<day<<" "<< "lipca "<<year<<"\n"; 
            break; 
        case 8:
            std::cout<<day<<" "<< "sierpnia "<<year<<"\n"; 
            break; 
        case 9:
            std::cout<<day<<" "<< "września "<<year<<"\n"; 
            break;
        case 10:
            std::cout<<day<<" "<< "października "<<year<<"\n"; 
            break; 
        case 11:
            std::cout<<day<<" "<< "listopada "<<year<<"\n"; 
            break; 
        case 12:
            std::cout<<day<<" "<< "grudnia "<<year<<"\n"; 
            break; 
        default: 
            std::cout<<"Error, wrong month"; 
            break;   
   } 
}

int main() {
    std::cout << "Zadanie 1 \n";
    std::cout << "Trigraphs works if I use flag -trigraphs \n";
    std::cout << "An example: ??-";

    std::cout << "\n\n\n";

    std::cout << "Zadanie 2 \n";
    std::string a = R"(Instytut Informatyki Uniwersytetu Wrocławskiego
Fryderyka Joliot-Curie 15
50-383, Wrocław)";
    std::cout << a << "\n";

    std::string b = R"^(C:\Program Files (x86))^";
    std::cout << b << "\n";

    std::string c = R"^^^(""")".?\_")(#)#)#)#$_|)^^^";
    std::cout << c << "\n \n";

    std::cout << "Zadanie 3 \n";

    using sset = std::set<std::string>;
    sset zmienna{"abc, def, ghi"};

    for(auto var : zmienna){
        std::cout << var << "\n";
    }

    std::cout << "\n";
    std::cout << "Zadanie 4 \n";

    info("Jest dzisiaj czwartek", Names::Tomasz);

    std::cout << "\n";
    std::cout << "Zadanie 5 \n";
    
    std::cout << "Lukas sequence values for indexes: 0, 1, 2, 4 \n";
    std::cout << lucas(0) <<" "<< lucas(1) <<" "<< lucas(2) <<" "<< lucas(4);

    std::cout << "\n \n";
    std::cout << "Zadanie 6 \n";
    
    std::cout << "x^2 + 2x + 1: \n";
    delta(1, 2, 1);

    std::cout << "x^2 + 4x + 3: \n";
    delta(1, 4, 3);

    std::cout << "x^2 + 1: \n";
    delta(1, 0, 1);

    std::cout << "\n";
    std::cout << "Zadanie 7 \n";

    calendar("15 10 1999");
    calendar("10 04 2010");

    return 0;
}