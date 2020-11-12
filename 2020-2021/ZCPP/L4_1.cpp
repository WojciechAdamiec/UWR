#include <iostream>
#include <list>
#include <set>
#include <vector>

using namespace std;

// Wypisz Elementy
template <typename Container>
void printElements(const Container &c) {
    int i = 0;
    for(auto it = c.begin(); it != c.end(); i++, it++)
        cout << "[" << i << "] =\t" << *it << '\n';
}

// Z1
template <typename Container>
void printIfInRange(const Container &c,
                    const typename Container::value_type &a,
                    const typename Container::value_type &b) {
    auto lambda = [&](auto x) {
        if(x > a && x < b)
            cout << '\t' << x << '\n';
    };
    for_each(c.begin(), c.end(), lambda);
}

// Z2
template <typename Container>
// Wypisz co k-ty od p-tej
void printKth(const Container &c, const int &k, const int &p) {
    // Przesuń iterator it o n miejsc
    auto lambda = [&](auto it, auto n) {
        for(auto j = 0; j < n; j++) {
            if(it == c.end())
                return it;
            it++;
        }
        return it;
    };

    for(auto i = lambda(c.begin(), p); i != c.end(); i = lambda(i, k))
        cout << '\t' << *i << '\n';
}

// Z3
template <typename Container>
void getMean(const Container &c) {
    using cv = typename Container::value_type;
    cv sum = cv();
    auto lambda = [&](auto it) {
        sum += *it;
        return ++it;
    };

    for(auto i = c.begin(); i != c.end(); i = lambda(i))
        continue;
    cout << "\tMean: " << sum / static_cast<cv>(c.size()) << '\n';
}

// Z4
template <typename Container>
auto getMinMax(const Container &c) {
    auto min = c.begin();
    auto max = c.begin();
    auto lambda = [&](auto it) {
        if(*min > *it)
            min = it;
        if(*max < *it)
            max = it;
        return ++it;
    };

    for(auto i = c.begin(); i != c.end(); i = lambda(i))
        continue;
    return make_pair(min, max);
}

// Z5
template <typename Container>
auto getSum(const Container &c) {
    using cv = typename Container::value_type;
    cv sum = cv();
    auto lambda = [&](auto it) {
        sum += *it;
        return ++it;
    };

    for(auto i = c.begin(); i != c.end(); i = lambda(i))
        continue;
    return sum;
}


int main() {

    // Initialization
    vector<double> doubleVector;
    list<string> stringList;
    set<int> intSet;

    doubleVector.push_back(6.54);
    doubleVector.push_back(2.74);
    doubleVector.push_back(-9.27);
    doubleVector.push_back(7.11);

    stringList.push_back("abcdef");
    stringList.push_back("faeaef");
    stringList.push_back("apoilk");
    stringList.push_back("mn,nm,");

    intSet.insert(2);
    intSet.insert(7);
    intSet.insert(13);
    intSet.insert(-6);

    // Elements
    cout << "\n======== Elementy ========\n";
    cout << "==========================\n";
    cout << "doubleVector:\n";
    printElements(doubleVector);
    cout << "\nstringList:\n";
    printElements(stringList);
    cout << "\nintSet:\n";
    printElements(intSet);
    cout << "==========================\n";

    // Z1
    
    cout << "== Wypisz z przedziału ===\n";
    cout << "==========================\n";
    cout << "doubleVector:\n";
    printIfInRange(doubleVector, -2, 7);
    cout << "stringList:\n";
    printIfInRange(stringList, "bbbb", "nnnn");
    cout << "intSet:\n";
    printIfInRange(intSet, -5, 10);
    cout << "==========================\n";

    // Z2
    cout << "= Wypisz co k-tą od p-tej \n";
    cout << "==========================\n";
    cout << "doubleVector:\n";
    printKth(doubleVector, 2, 1);
    cout << "stringList:\n";
    printKth(stringList, 2, 1);
    cout << "intSet:\n";
    printKth(intSet, 2, 1);
    cout << "==========================\n";

    // Z3
    cout << "===== Wypisz średnią =====\n";
    cout << "==========================\n";
    cout << "doubleVector:\n";
    getMean(doubleVector);
    cout << "intSet:\n";
    getMean(intSet);
    cout << "==========================\n";

    // Z4
    cout << "===== Wypisz min/max =====\n";
    cout << "==========================\n";
    cout << "doubleVector:\n";
    auto dvp = getMinMax(doubleVector);
    cout << "Min: " << *dvp.first << "\tMax: " << *dvp.second << '\n';
    cout << "stringList:\n";
    auto slp = getMinMax(stringList);
    cout << "Min: " << *slp.first << "\tMax: " << *slp.second << '\n';
    cout << "intSet:\n";
    auto isp = getMinMax(intSet);
    cout << "Min: " << *isp.first << "\tMax: " << *isp.second << '\n';
    cout << "==========================\n";

    // Z5
    cout << "======= Wypisz sumę ======\n";
    cout << "==========================\n";
    cout << "doubleVector:\n";
    cout << getSum(doubleVector) << '\n';
    cout << "stringList:\n";
    cout << getSum(stringList) << '\n';
    cout << "intSet:\n";
    cout << getSum(intSet) << '\n';
    cout << "==========================\n";

    return 0;
}
