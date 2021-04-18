#include <stdio.h>
#include <cinttypes>
#include <utility>


void pushDown(std::pair<uint64_t, uint64_t> arr[], uint64_t n, uint64_t i){
    uint64_t k = i;
    uint64_t j = k;
    do {
        j = k;
        if (2 * j <= n && arr[2 * j].first < arr[k].first){
            k = 2 * j;
        }
        if (2 * j < n && arr[2 * j + 1].first < arr[k].first){
            k = 2 * j + 1;
        }
        std::swap(arr[j], arr[k]);
    }
    while(j != k);
}


void pushUp(std::pair<uint64_t, uint64_t> arr[], uint64_t i){
    uint64_t k = i;
    uint64_t j = k;
    do {
        j = k;
        if (j > 1 && arr[j / 2].first > arr[k].first){
            k = j / 2;
        }
        std::swap(arr[j], arr[k]);
    }
    while(j != k);
}


void build_heap(std::pair<uint64_t, uint64_t> arr[], uint64_t n) 
{ 
    for (uint64_t i = n / 2; i >= 1; i--){
        pushDown(arr, n, i);
    }
}


void deleteMin(std::pair<uint64_t, uint64_t> arr[], uint64_t& n) 
{ 
    arr[1] = arr[n];
    n = n - 1;

    uint64_t k = 1;
    uint64_t j = k;

    do {
        j = k;
        if (2 * j <= n){
            k = 2 * j;
        }
        if (2 * j < n && arr[2 * j + 1].first < arr[2 * j].first){
            k = 2 * j + 1;
        }
        std::swap(arr[j], arr[k]);
    }
    while(j != k);
    
    pushUp(arr, k);
} 


std::pair<uint64_t, uint64_t> findMin(std::pair<uint64_t, uint64_t> arr[]) 
{ 
    std::pair<uint64_t, uint64_t> min = arr[1];
    return min;
}


void insertNode(std::pair<uint64_t, uint64_t> arr[], uint64_t &n, std::pair<uint64_t, uint64_t> Key) 
{ 
    arr[n + 1] = Key;
    n = n + 1;
    pushUp(arr, n);
}


bool isEmpty(uint64_t size){
    return (size < 1);
}


int main(){
    uint64_t size, aux_size, a, b;
    std::pair<uint64_t, uint64_t> p;
    scanf("%lu", &size);
    aux_size = 0;
    
    std::pair<uint64_t, uint64_t> *main_heap = new std::pair<uint64_t, uint64_t>[size + 1];
    std::pair<uint64_t, uint64_t> *aux_heap = new std::pair<uint64_t, uint64_t>[size + 1];

    for (uint64_t i=1; i <= size; i++){
        scanf("%lu", &a);
        scanf("%lu", &b);
        p = std::make_pair(a, b);
        
        main_heap[i] = p;
    }

    build_heap(main_heap, size);
    
    uint64_t ropes = 0;
    int parity;
    
    while(!isEmpty(size)){
        
        auto root = findMin(main_heap);

        if (!isEmpty(aux_size)){
            auto top = findMin(aux_heap);
            if (top.first == root.first){
                insertNode(aux_heap, aux_size, std::make_pair(root.first * 2, (root.second + top.second) / 2));
                deleteMin(main_heap, size);
                deleteMin(aux_heap, aux_size);
                parity = (root.second + top.second) % 2;
            }
            else if(top.first < root.first){
                deleteMin(aux_heap, aux_size);
                if (top.second > 1)
                    insertNode(aux_heap, aux_size, std::make_pair(top.first * 2, top.second / 2));
                parity = top.second % 2;
            }
            else{
                deleteMin(main_heap, size);
                if (root.second > 1)
                    insertNode(aux_heap, aux_size, std::make_pair(root.first * 2, root.second / 2));
                parity = root.second % 2;
            }
        }
        else{
            deleteMin(main_heap, size);
            if (root.second > 1)
                insertNode(aux_heap, aux_size, std::make_pair(root.first * 2, root.second / 2));
            parity = root.second % 2;
        }
        if (parity == 1){
            ropes++;
        }
    }
    
    while(!isEmpty(aux_size)){

        std::pair<uint64_t, uint64_t> root = findMin(aux_heap);
        deleteMin(aux_heap, aux_size);

        if (root.second > 1){
            insertNode(aux_heap, aux_size, std::make_pair(root.first * 2, root.second / 2));
        }
        if (root.second % 2 == 1){
            ropes++;
        }

    }
    
    printf("%lu", ropes);
    
    return 0;
}