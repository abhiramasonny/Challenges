#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define SIZE 200000000000

struct DataItem {
   int data;   
   int key;
};

struct DataItem* hashArray[SIZE]; 
struct DataItem* dummyItem;
struct DataItem* item;

int hashCode(int key) {
   return key % SIZE;
}

struct DataItem *search(int key) {
   int hashIndex = hashCode(key);  
	
   while(hashArray[hashIndex] != NULL) {
	
      if(hashArray[hashIndex]->key == key)
         return hashArray[hashIndex]; 
      ++hashIndex;
      hashIndex %= SIZE;
   }        
	
   return NULL;        
}

void insert(int key,int data) {

   struct DataItem *item = (struct DataItem*) malloc(sizeof(struct DataItem));
   item->data = data;  
   item->key = key;
   int hashIndex = hashCode(key);

   while(hashArray[hashIndex] != NULL && hashArray[hashIndex]->key != -1) {
      ++hashIndex;
		
      hashIndex %= SIZE;
   }
	
   hashArray[hashIndex] = item;
}

struct DataItem* delete(struct DataItem* item) {
   int key = item->key;

   int hashIndex = hashCode(key);

   while(hashArray[hashIndex] != NULL) {
	
      if(hashArray[hashIndex]->key == key) {
         struct DataItem* temp = hashArray[hashIndex]; 
			
         hashArray[hashIndex] = dummyItem; 
         return temp;
      }
		
      ++hashIndex;
		
      hashIndex %= SIZE;
   }      
	
   return NULL;        
}

void display() {
   int i = 0;
	
   for(i = 0; i<SIZE; i++) {
	
      if(hashArray[i] != NULL)
         printf(" (%d,%d)",hashArray[i]->key,hashArray[i]->data);
      else
         printf("");
   }
	
   printf("\n");
}



int fib(int n){
    item = search(n);
    if (n == 0) return  0;
    else if (n == 1) return 1;
    else if (n == 2) return 1;
    else if (item != NULL){
      return item->data;
    } else {
        int ans = fib(n - 1) + fib(n - 2);
        insert(n,ans );
        printf("Storing %d to hash. \n", ans);
        return ans;
    }
}

int main(){
   dummyItem = (struct DataItem*) malloc(sizeof(struct DataItem));
   dummyItem->data = -1;  
   dummyItem->key = -1; 
   int i = 0;
   while (true){
        int ans = fib(i);
        printf("%d\n", ans);
        i++;
   }
}
