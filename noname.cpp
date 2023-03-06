#include <iostream>
#include <string>
#include <cstdlib>

void print(std::string s)
{std::cout<< s << "\n";}

int input(){
    int x;
    std::cin>>x;
    return x;
    std::cout<< "\n" ;
    }


int main()
{
 print("RULES : ") ;
 print("1. Enter A random Number Between 1 and 5.") ;
 print("2. The Computer Will Return A random Number In Return") ;
 print("3. If The Number Picked By You And The Computer Are Equal, The Game Ends . Otherwise The Number Picked By You Is Added To The Score \n") ;
 int score=0 ;
 while (1) {
     int i= input() ;
     int random= rand() % 5 + 1;
     if (0<i && i<6) {
         print(std::to_string(random) + "\n") ;
         if (i==random){
             print("->GAME OVER \n  SCORE : "+ std::to_string(score) + "\n") ;
             break ;}
         else {
             score+=i ;
             print("> SCORE : "+ std::to_string(score) +"\n") ;
            }
     }
 	else{
         print("Invalid Number. Number must be an integer between 1 and 5 \n") ; 
 	}
 }
return 0;}
