#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main(int argc, char *argv[]) {
    if(argc != 2) {
        std::cout << "Wrong ammount of arguments.\n";
        return 1;
    }

    fs::path p{ argv[1] };
    if(!fs::exists(p)) {
        std::cout << "Directory: " << p << " doesn't exist.\n";
        return 2;
    }

    if(!fs::is_directory(p)) {
        std::cout << "File: " << p << " is not a directory.\n";
        return 3;
    }

    for(auto &p : fs::directory_iterator(p))
        std::cout << p.path() << '\n';

    return 0;
}
