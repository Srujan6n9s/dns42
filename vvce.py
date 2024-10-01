// Online C compiler to run C program online
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#define MAX 5
#define high 7

void DFS(int adj[][MAX],int visited[],int start){
    int stack[MAX];
    int top=-1;
    for(int k=0;k<MAX;k++){
        visited[k]=0;}
        stack[++top]=start;
        visited[start]=1;
        while(top!=-1){
            start=stack[top--];
            printf("%d\t",start);
            for(int i=0;i<MAX;i++){
                if(adj[start][i]&&visited[i]==0){
                    stack[++top]=i;
                    visited[i]=1;
                    break;
                    
                }
            }
        }}
 void BFS(int adj[][MAX],int visited[],int start) {
     int queue[MAX];
     int rear=-1;int front=-1;
     for(int k=0;k<MAX;k++){
         visited[k]=0;
         
     }
     queue[++rear]=start;
     ++front;
     visited[start]=1;
     while(rear>=front){
         start=queue[front++];
         printf("%d\t",start);
         for(int i=0;i<MAX;i++){
             if(adj[start][i]&&visited[i]==0){
                 queue[++rear]=i;
                 visited[i]=1;
             }
         }
     }
 } 

int main() {
  int adj[MAX][MAX];
  int visited[MAX]={0};
  int option;
  while(true){
      printf("enter an option:");
          scanf("%d",&option);
          switch(option){
              case 1:
              printf("enter the adjacency matrix:\n");
              for(int i=0;i<MAX;i++){
                  for(int j=0;j<MAX;j++){
                      scanf("%d",&adj[i][j]);
                  }
              }
              break;
              case 2:
              DFS(adj,visited,0);
              break;
              case 3:
              BFS(adj,visited,0);
              break;
              case 4:
              exit(0);
              break;
              case 5:
              printf("the adjacency matrix is:\n");
              for(int i=0;i<MAX;i++){
                  for(int j=0;j<MAX;j++){
                      printf("%d\t",adj[i][j]);
                      
                  }
                  printf("\n");
                 
              }
               break;
              default:
              printf("invalid choice");
              
          }
      }
      return 0;
  }
  