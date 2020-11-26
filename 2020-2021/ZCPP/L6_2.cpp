#include <iostream>
#include <list>
#include <algorithm>

using namespace std;


class Point{
    public:
        string name;
        double x;
        double y;
        double R;
        double G;
        double B;
    
        Point(string name, double x, double y, double R, double G, double B)
            : name{name}, x{x}, y{y}, R{R}, G{G}, B{B}{}
        
        void info(){
            cout << "\nname: " << name << " x: " << x << " y: " << y << " R: " << R << " G: " << G << " B: " << B;
        }
};

bool operator== (const Point &a, const Point &b){
            return (a.name == b.name);
        }

int main() {

    // Create Deck
    list<Point> points;
    points.push_back(Point("ab", -10, 5, 24, 62, 74));
    points.push_back(Point("bbb", 10, -5, 24, 62, 32));
    points.push_back(Point("abcfg", 10, 2, 24, 62, 16));
    points.push_back(Point("abdefg", -10, 5, 24, 62, 0));
    points.push_back(Point("acdefg", 0, 0, 24, 62, 255));
    points.push_back(Point("aefg", 10, 1, 24, 62, 255));
    points.push_back(Point("afg", 10, -1, 24, 62, 0));
    points.push_back(Point("abcdfsaefg", 5, -5, 24, 62, 10));
    points.push_back(Point("abg", 16, -1, 24, 62, 67));
    points.push_back(Point("abcfffg", -10, -5, 24, 62, 12));
    points.push_back(Point("abcdfsefg", -1, -1, 24, 62, 25));
    points.push_back(Point("abcdsfefg", 2, 2, 24, 62, 125));
    points.push_back(Point("abcdefg", 10, -3, 24, 62, 125));
    points.push_back(Point("aag", 7, -5, 24, 62, 210));
    points.push_back(Point("abfg", -2, -5, 24, 62, 15));
    points.push_back(Point("abcqfg", -10, -5, 24, 62, 11));
    points.push_back(Point("baefg", 0, -1, 24, 62, 61));

    // Show content of Deck
    cout << "================\n";
    cout << "Unmodified table\n";
    cout << "================\n";
    for_each(points.begin(), points.end(), [](auto p){p.info();});

    // A. Remove long name points
    points.remove_if([](auto &p){return p.name.length() > 5;});

    // Show content of Deck
    cout << "\n\n";
    cout << "================\n";
    cout << "Removed long names table\n";
    cout << "================\n";
    for_each(points.begin(), points.end(), [](auto p){p.info();});

    // B. Count points in quarters
    int pp, pn, np, nn = 0;
    for_each(points.begin(), points.end(), [&pp, &pn, &np, &nn](auto p)
    {
        if (p.x >= 0 && p.y >= 0)pp++;
        if (p.x >= 0 && p.y < 0)pn++;
        if (p.x < 0 && p.y >= 0)np++;
        if (p.x < 0 && p.y < 0)nn++;
    });

    // Show content of Deck
    cout << "\n\n";
    cout << "================\n";
    cout << "Counted points in quarters\n";
    cout << "================\n";
    cout << "top-right: " << pp << "\n";
    cout << "top-left: " << np << "\n";
    cout << "bot-right: " << pn << "\n";
    cout << "bot-left: " << nn;

    // C. Sort by luminance 
    points.sort([](auto a, auto b)
        {return (0.3 * a.R + 0.59 * a.G + 0.11 * a.B) <= (0.3 * b.R + 0.59 * b.G + 0.11 * b.B);});

    // Show content of Deck
    cout << "\n\n";
    cout << "================\n";
    cout << "Sorted by luminance\n";
    cout << "================\n";

    for_each(points.begin(), points.end(), [](auto p){p.info();});

    // D. Dark points 
    list<Point> darks;
    auto iter = partition(points.begin(), points.end(), [](auto p){return (0.3 * p.R + 0.59 * p.G + 0.11 * p.B) >= 64;});
    move(iter, points.end(), back_inserter(darks));

    // Show content of Deck
    cout << "\n\n";
    cout << "================\n";
    cout << "Dark points\n";
    cout << "================\n";

    for_each(darks.begin(), darks.end(), [](auto p){p.info();});

    return 0;
}