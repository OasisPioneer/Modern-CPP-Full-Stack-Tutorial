# 函数

函数（Function）是一个用于完成特定功能且可重复使用的代码块。

函数特性:

- 提高代码复用性
- 降低复杂度
- 提高可读性和可维护性

函数由以下部分组成：

- 返回类型
- 函数名称
- 参数列表
- 函数体

## 定义函数

基本语法:

```CPP
返回类型 函数名称(参数列表) {
    // 函数体
    return 返回值;
}
```

代码演示:

```CPP
int Addition(int a, int b) {
    return a + b;
}
```

当调用该函数时，需要提供对应参数，函数执行完后会返回结果。

```{attention}
如果函数返回类型为 void，则表示不返回任何数据，此时可以省略 return 语句。
```

## 调用函数

```CPP
int Addition(int a, int b) {
    return a + b;
}

int main() {
    // 调用我们定义的函数并输出返回的结果
    std::cout << Addition(10, 5) << std::endl;
}
```

## 声明函数

函数可以先声明，后定义。

声明用于告诉编译器该函数是存在的，定义才是具体实现。

一个函数可以在不同的位置多次声明，但只能定义一次。

基本语法:

```CPP
返回类型 函数名称(参数列表);
```

代码演示:

```CPP
int Addition(int a, int b);
```

```{attention}
在同一个代码文件中如果没有在顶部声明函数则函数只能被后方代码调用，如果希望函数能够在当前文件中的任意位置调用则需要在代码文件的顶部进行声明
```

代码演示:

```CPP
int Addition(int a, int b); // 声明函数 确保下方所有位置都能调用

int main() {
    // 如果 Addition 函数没有在当前函数上方声明则此处无法调用
    std::cout << Addition(10, 5) << std::endl;
}

int Addition (int a, int b) {
    return a + b;
}
```

## 参数传递

### 值传递

值传递的本质就是将数据拷贝一个副本传递给函数，在函数中无论做什么都不会影响原始数据。

代码演示:

```CPP
void Swap(int num1, int num2);

int main() {
    int A{15};
    int B{30};

    Swap(A, B);

    std << "A: " << A << std::endl;
    std << "B: " << B << std::endl;
}

void Swap(int A, int B)
{
	int Temp = A;
	A = B;
    B = Temp;

    std::cout << "Swap A: " << A << std::endl;
    std::cout << "Swap B: " << B << std::endl;
}
```

### 引用传递

函数接收对原始变量的引用，当你对引用传递的参数做任何修改时都会影响原始变量。

基本语法:

```CPP
返回类型 函数名称(数据类型 & 参数名称);
```

通过 & 符号连接数据类型与参数名称则为引用参数。

代码演示:

```CPP
void Swap(int& a, int& b) {
    int temp{a};
    a = b;
    b = temp;
}
```

### 常量引用传递

代码演示:

```CPP
void Print(const std::string& s) {
    std::cout << s << std::endl;
}
```

主要作用:防止函数修改数据和避免拷贝（提高性能）

## 作用域

在函数内定义的任何变量或常量被称之为局部变量和局部常量，当它们一旦离开该函数则会被立即销毁。

代码演示:

```CPP
void foo() {
    int x{10}; // 仅在函数内部有效
}

int main() {
    x = 15; // 错误：x 未定义（作用域问题）
}
```

## 函数重载

在 C++ 中当相同的函数名接收不同的参数时即为函数重载。

代码演示:

```CPP
int add(int a, int b);
double add(double a, double b);
```

```{attention}
如果是返回类型不同时则不能构成重载。
```

## 默认参数

当函数的参数列表中的参数定义了默认数据时在调用这个函数的时候这个位置可空。

代码演示:

```CPP
int Addition(int a, int b = 10) {
    return a + b;
}

Addition(5); // 等价于 Addition(5, 10)
```

```{attention}
默认参数必须从右往左连续定义，不能跳跃。
```

## 内联函数 (inline)

inline 是一种用于建议编译器将函数调用展开为函数体代码的关键字，其主要目的是减少函数调用开销，提高性能。

基本语法:

```CPP
inline 返回类型 函数名称(参数列表) {
    // 函数体
}
```

```{important}
在现代 C++ 中 inline 的核心作用是：

允许函数在多个文件中重复定义（解决 ODR 问题）。

编译器可以忽略 inline，这只是一个优化提示而不是强制行为。
```

## Lambda 表达式

Lambda 表达式是 C++11 引入的一种 **匿名函数（无名函数）** 机制，用于在需要函数的地方快速定义一段可执行代码。

Lambda 表达式的本质其实就是一个可以捕获外部变量的临时函数对象。

基本语法:

```CPP
[捕获列表](参数列表) -> 返回类型 {
    函数体
};
```

常见写法:

```CPP
[捕获列表](参数列表) {
    函数体
};
```

代码演示:

```CPP
auto add = [](int a, int b) {
    return a + b;
};

int result{add(10, 20)}; // result = 30
```