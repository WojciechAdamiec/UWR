#include <cstdio>
#include <cstdlib>
#include <algorithm>


int main(){
    
    const int MAX = 1000001;

    // Array with pairs: difference - maximal sum
    int *Diff = new int[MAX];

    // Just to optimize algorithm
    int *Keys = new int[MAX];
    int KeysSize = 1;
    int KeysAux = 1;

    // Initialize with 0s - CPP problem
    for(int x = 0; x < MAX; x++){
        Keys[x] = 0;
    }

    // We will need a copy of main array Diff
    int *Aux;

    // Initialize Diff with -1 to keep track of active differences
    for (int x = 0; x < MAX; x++){
        Diff[x] = -1;         
    }

    Diff[0] = 0;

    // Read number of blocks
    int size, ele, d, s, ss;
    int minimalBlock = MAX;

    scanf("%d", &size);

    // For every block
    for (int i = 0; i < size; i++){
        
        // Read and store block
        scanf("%d", &ele);

        if (ele < minimalBlock){
            minimalBlock = ele;
        }

        // Copy main array
        Aux = new int[MAX];
        std::copy(Diff, Diff + MAX, Aux);

        KeysAux = KeysSize;
        // For every active pair in Diff
        for(int j = 0; j < KeysAux; j++){
            
            
            // Store elements of this pair
            d = Keys[j];
            s = Diff[Keys[j]];
            
            // Store new sum
            ss = s + ele;

            // Update new differences with possibly bigger sums
            // If difference is new we need to activate it
            if (Aux[abs(d - ele)] < ss){
                if (Aux[abs(d - ele)] == -1){
                    Keys[KeysSize] = abs(d - ele);
                    KeysSize += 1;
                }
                Aux[abs(d - ele)] = ss;
                
            }
            
            if (Aux[abs(d + ele)] < ss){
                if (Aux[abs(d + ele)] == -1){
                    Keys[KeysSize] = abs(d + ele);
                    KeysSize += 1;
                }
                Aux[abs(d + ele)] = ss;
            }
        }

        // Store modified copy of an array into original one
        // Free unused memory
        delete[] Diff;
        Diff = Aux;
    }
    
    // If diff 0 (equal towers) consists of some blocks (sum > 0)
    if (Diff[0] != 0){
        printf("TAK\n");

        // Height of a tower is a half of the sum of the two towers
        printf("%d", Diff[0] / 2);
        return 0;
    }

    printf("NIE\n");
    for (int w = 1; w < MAX; w++){
        if (Diff[w] != -1 && Diff[w] > minimalBlock){
            printf("%d", w);
            return 0;
        }
    }

    return 0;
}
