// gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c

// -fPIC: Position-Independent Code
// -shared: 生成动态链接库

//-Wl选项告诉编译器将后面的参数传递给链接器。
// -soname则指定了动态库的soname(简单共享名，Short for shared object name)

// -m32 生成32位程序

#include <stdio.h>


struct ST {
    int a;
    char b[30];
    void *p;
};

int add_int(int,int);
float add_float(float,float);


int add_int(int num1,int num2)
{
    return num1 + num2;
}
float add_float(float num1, float num2)
{
    return num1 + num2;
}

struct ST get_struct_res() 
{
    struct ST st = {
        .a = 20,
        .b = "this is a buffer",
        .p = (void *)0xffff,
    };
    return st;
}
