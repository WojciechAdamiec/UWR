#include <fstream>
#include <iostream>
#include <memory>

using namespace std;

class line_writer {
    ofstream *file;

public:
    line_writer(string path){
        file = new ofstream(path, ios::out);
    }
    
    // Konstruktor kopiujący
    line_writer(const line_writer &);
    ~line_writer() { delete file; cout << "Obiekt zniszczony \n";}

    void write(string line) 
    {
        *file << line << '\n'; 
        cout << line << " \n";
    }
};

int main() {
    shared_ptr<line_writer> a = make_shared<line_writer>("file.txt");
    shared_ptr<line_writer> b(a);
    weak_ptr<line_writer> weak(a);

    if (auto copy = weak.lock()) {
        cout << "'weak pointer' wskazuje na obiekt \n";
    } else
        cout << "'weak pointer' na nic nie wskazuje \n";

    a->write("test a1");
    a->write("test a2");
    a->write("test a3");
    a->write("");
    a.reset();

    if (auto copy = weak.lock()) {
        cout << "'weak pointer' wskazuje na obiekt \n";
    } else
        cout << "'weak pointer' na nic nie wskazuje \n";

    b->write("test b1");
    b->write("test b2");
    b->write("test b3");
    b->write("");
    b.reset();

    if (auto copy = weak.lock()) {
        cout << "'weak pointer' wskazuje na obiekt \n";
    } else
        cout << "'weak pointer' na nic nie wskazuje \n";
    return 0;
}