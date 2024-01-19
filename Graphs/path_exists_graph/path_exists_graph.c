#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void mergeSets(int set1, int set2, int roots[]) {
    int root1 = findRoot(set1, roots);
    int root2 = findRoot(set2, roots);
    if (root1 != root2) {
        roots[root1] = root2;
    }
}

int findRoot(int element, int roots[]) {
    int root = element;
    while (root != roots[root]) {
        roots[root] = roots[roots[root]];
        root = roots[root];
    }
    return root;
}

bool validPath(int totalNodes, int** connectivity, int numEdges, int startPoint, int endPoint) {
    int roots[totalNodes];
    for (int i = 0; i < totalNodes; i++) {
        roots[i] = i;
    }

    for (int i = 0; i < numEdges; i++) {
        mergeSets(connectivity[i][0], connectivity[i][1], roots);
    }

    return findRoot(startPoint, roots) == findRoot(endPoint, roots);
}

int main(){
  int totalNodes;
  int startPoint;
  int endPoint;
  int numEdges;

  printf("Enter the number of nodes: ");
  scanf("%d", &totalNodes);

  printf("Enter the number of edges: ");
  scanf("%d", &numEdges);

  int** connectivity = malloc(numEdges * sizeof(int*));
    for (int i = 0; i < numEdges; i++) {
        connectivity[i] = malloc(2 * sizeof(int));

        printf("Enter the %d edge: ", i + 1);
        scanf("%d %d", &connectivity[i][0], &connectivity[i][1]);
    }

  printf("Enter the starting point: ");
  scanf("%d", &startPoint);

  printf("Enter the end point: ");
  scanf("%d", &endPoint);

  int center = validPath(totalNodes, connectivity, numEdges, startPoint, endPoint);
  if (center == true){
    printf("True\n");
  } else {
    printf("False\n");
  }
  for (int i = 0; i < numEdges; i++) {
        free(connectivity[i]);
    }
    free(connectivity);

    return 0;
}
