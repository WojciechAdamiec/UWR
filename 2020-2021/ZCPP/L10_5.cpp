#include <cstdint>
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

long dsize(fs::path path) {
    long size = 0;
    for (auto &p : fs::recursive_directory_iterator(path)){
        if (fs::is_regular_file(p)){
            size += fs::file_size(p);
        }
    }
    return size;
}

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

    auto size = dsize(p);

    std::cout << "Total size of directory: " << size << '\n';

    return 0;
}
