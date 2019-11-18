//https://paragonie.com/blog/2016/05/how-generate-secure-random-numbers-in-various-programming-languages#c-csprng
#include "sodium.h"
int foo() {
    char myString[32];
    uint32_t myInt;
    
    randombytes_buf(myString, 32);
    /* myString will be an array of 32 random bytes, not null-terminated */
    myInt = randombytes_uniform(10);
    /* myInt will be a random number between 0 and 9 */
    return 0;
}

// C
#include <time.h>
#include <stdlib.h>


int foo2() {
    srand(time(NULL));   // Initialization, should only be called once.
    int r = rand();      // Returns a pseudo-random integer between 0 and RAND_MAX.
    return 0;
}

//C++
#include <cstdlib>
#include <iostream>
#include <ctime>
 
int foo2() 
{
    std::srand(std::time(0)); //use current time as seed for random generator
    int random_variable = std::rand();
    std::cout << "Random value on [0 " << RAND_MAX << "]: " 
              << random_variable << '\n';
    
    return 0;
}