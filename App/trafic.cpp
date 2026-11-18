#include <iostream>
#include <string.h>
using namespace std;
int main()
{
  string color;
  cout<<"";
  cin>>color;
  if(color == "RED" || color == "red")
  {
    printf("STOP!");
  }
  else if(color == "YELLOW" || color == "yellow")
  {
    printf("READY!");
  }
  else if(color == "GREEN" || color == "green")
  {
    printf("GO!");
  }
  else
  {
    printf("INVALID CHOICE!!!");
  }

}