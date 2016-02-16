#include <stdio.h>
#include <stdlib.h>

// call the same function two recursively
// pass address allocated for an local (stack) variable inside first call to the function to second call to the same function
// allocate a another local variable inside second call 
// check if addresses for pass variable from stack from function call one and local variable in function call two
// if first one < second one stack is growing upward. 0000.......stack_top........function_2......function_1....stack_starting_point
// else growing downward. stack_starting_point....function_1....function_2.....stack_top.......0000

void func(int *p) {
    int i;
    if (!p)
        func(&i);

    else if (p < &i)
    {
        printf("Stack grows upward\n");
        printf("address of p: 0x%x\n", p);
    	printf("address of i: 0x%x\n", &i);
    }

    else
    {
        printf("Stack grows downward\n");
        printf("address of p: 0x%x\n", p);
    	printf("address of i: 0x%x\n", &i);
    }

}


int main()
{
	func(NULL);
}

