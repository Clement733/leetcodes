#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
  return (*(int*)a - *(int*)b);
}

bool containsDuplicates(int* nums, int numsSize){
  qsort(nums, (size_t)numsSize, sizeof(int), cmp);
  for (int i = 1; i < numsSize; i++){
    if (nums[i] == nums[i - 1]){
      return true;
    }
  }
  return false;
}

int main(){
  int size;
  printf("Size of the array: ");
  scanf("%d", &size);

  int *arr = (int *)malloc((size_t)size * sizeof(int));
  for (int i = 0; i < size; i++){
    scanf("%d", &arr[i]);
  }
  if (containsDuplicates(arr, size)){
    printf("Duplicates!\n");
  } else {
    printf("No duplicates!\n");
  }
  free(arr);
  return 0;
}
