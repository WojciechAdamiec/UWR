#include <chrono>
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main(int argc, char *argv[]) {
    if(argc < 2)
        return 1;

    for(int i = 1; i < argc; i++) {
        fs::path p{ argv[i] };
        if(fs::exists(p)) {
            if (!fs::is_directory(p)){
                std::cout << "File: " << p << " exists. Details:\n"
                          << "Size: " << fs::file_size(p) << '\n'
                          << "Path: " << fs::canonical(p) << '\n';
            }
            else{
                std::cout << "Directory: " << p << " exists. Details:\n"

                          << "Path: " << fs::canonical(p) << '\n';
            }
            
        } else {
            std::cout << "File: " << p << " does not exist.\n";
        }
    }

    return 0;
}
