#include <stdio.h>
#include <stack>
#include <vector>
#include <algorithm>
#include <unordered_map>

int size;

std::stack<int> stack;
std::unordered_map<int, std::vector<int>> map;

short **data;
int *history;
bool *visited;

int DFS() {
    while (!stack.empty()){
        int index = stack.top();
        stack.pop();
        visited[index] = true;
        int last = data[index][2];
        if(map.count(last)){
            for(int i : map[last]){
                if(!visited[i] && last == data[i][0]){
                    history[i] = index;
                    if(data[i][2] == 0){
                        return i;
                    }
                    stack.push(i);
                }
            }
        }
    }
    return -1;
}

int main (){

    scanf("%d", &size);

    data = new short*[size];
    for(int i=0; i < size; i++){
        data[i] = new short[3];
    }

    history = new int[size];
    visited = new bool[size];
    
    // Declare and initialize visited array

    for(int i=0; i < size; i++){
        visited[i] = false;
    }

    // Declare and initialize history array

    for(int i=0; i < size; i++){
        history[i] = -1;
    }

    // Declare and initialize data array

    for(int i=0; i < size; i++){
        for(int j=0; j < 3; j++){
            scanf("%hd", &data[i][j]);
        }
    }

    for(int i=0; i < size; i++){
        int j = data[i][0];
        if(map.count(j)){
            map[j].push_back(i);
        }
        else{
            map[j] = std::vector{i};
        }
    }

    // Declare and initialize stack

    for(int i=0; i < size; i++){
        if (data[i][0] == 0){
            stack.push(i);
        }
    }

    // Print all the data:
    /*
    for(int i=0; i < size; i++){
        printf("\n");
        for(int j=0; j < 3; j++){
            printf("%d ", data[i][j]);
        }
    }
    */

   std::vector<int> path;

   int finish = DFS();
   if (finish == -1){
       printf("BRAK");
   }
   else{
       int index = finish;
       while (data[index][0] != 0){
           path.push_back(index);
           index = history[index];
       }
       path.push_back(index);
       std::reverse(path.begin(), path.end());
       printf("%ld \n", path.size());
       for(int i : path){
           printf("%hd %hd %hd \n", data[i][0], data[i][1], data[i][2]);
       }

   }
    
}
