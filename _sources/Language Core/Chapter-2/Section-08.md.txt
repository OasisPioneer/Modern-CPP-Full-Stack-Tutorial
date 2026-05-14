# 控制结构

在 C++ 中，代码默认按照“从上到下”的顺序依次执行，这种执行方式称为顺序结构。

但在实际开发中，我们往往需要根据条件做出判断，或者重复执行某些代码，这时就需要使用控制结构来改变程序的执行流程。

常见的控制结构主要包括：

- 条件语句（if / else / switch）
- 循环语句（for / while / do-while）
- 跳转语句（break / continue / return）

## 条件语句

条件语句用于根据条件进行判断接下来所应该执行的代码。

### if 语句

if 语句又叫如果语句，当条件成立的时候会执行代码如果条件不成立则不会执行。

基本语法:

```CPP
if (条件表达式) {
    // 当条件表达式的条件成立时执行此处代码
}
```

代码示例:

```CPP
int age{18};        // 定义 age 变量并初始化值为 18

if (age >= 18) {    // 如果 age 大于等于 18 则执行下方代码
    std::cout << "小明已经成年了" << std::endl;
}
```

#### 现代 if 语句

自 C++17 起，if 语句支持在条件判断前进行变量初始化，用于限制变量作用域并提升代码可读性。

基本语法:

```CPP
if (初始化语句; 条件表达式) {
    // 条件成立执行
}
```

代码演示:

```CPP
if (int x{10}; x > 5) {
    std::cout << x << std::endl;
}
```

作用域说明:

```CPP
if (int x{10}; x > 5) {
    std::cout << x << std::endl;
}

std::cout << x; // 错误：x 在 if 外部不可用
```

```{attention}
if 初始化中的变量只在 if / else 语句内部有效，出了作用域将无法访问。
```

#### if / else 语句

当 if 语句中的条件不成立时则执行 else 中的代码。

基本语法:

```CPP
if (条件表达式) {
    // 当条件表达式的条件成立时执行此处代码
} else {
    // 当条件表达式的条件不成立时执行此处代码
}
```

代码示例:

```CPP
int age{16};

if (age >= 18) {    // 如果条件成立则执行下方代码
    std::cout << "小明已经成年了" << std::endl;
} else {            // 否则执行下方代码
    std::cout << "小明还没有成年" << std::endl;
}
```

#### if / else if / else

用于处理多个条件分支

基本语法:

```CPP
if (条件表达式1) {
    // 条件表达式1成立
} else if (条件表达式2) {
    // 条件表达式2成立
} else {
    // 以上条件表达式都不成立
}
```

代码示例:

```CPP
int score{85};

if (score >= 90) {
    std::cout << "优秀" << std::endl;
} else if (score >= 60) {
    std::cout << "及格" << std::endl;
} else {
    std::cout << "努力" << std::endl;
}
```

```{important}
多个条件是从上到下依次判断的，一旦某个条件成立，后续条件将不会再执行。
```

#### 嵌套 if 语句

在 if 语句中嵌套 if 语句可以进行更精确的条件判断

代码示例:

```CPP
int age{35};
bool is_employee{true};

if (is_employee) {
    if (age >= 35) {
        std::cout << "高级员工" << std::endl;
    } else if (age >= 30) {
        std::cout << "中级员工" << std::endl;
    } else {
        std::cout << "初级员工" << std::endl;
    }
}
```

```{attention}
如果嵌套过多会降低代码可读性，因此在使用 if 语句时应尽量避免深层嵌套。
```

```{important}
if 语句中的条件表达式必须是布尔类型或可以转换为布尔类型的表达式。
例如：0 表示 false，非 0 表示 true。
```

### 条件运算符

条件运算符是一种用于根据条件选择不同结果的运算符，也称为三元运算符。

它是 if / else 的简化写法，适用于简单的条件判断。

基本语法:

```CPP
条件表达式 ? 表达式1 : 表达式2;
```

执行逻辑:
- 如果条件表达式为 true → 返回 表达式1
- 如果条件表达式为 false → 返回 表达式2

代码演示:

```CPP
int a{10};
int b{20};

int max{ (a > b) ? a : b }; // 取较大值
```

等价写法:

```CPP
int max;

if (a > b) {
    max = a;
} else {
    max = b;
}
```

条件运算符本质是一个表达式，可以直接参与赋值或运算。

代码演示:

```CPP
int x{5};

int result{ (x > 0) ? x : -x }; // 取绝对值
```

```{attention}
条件运算符的两个结果（表达式1 和 表达式2）必须是相同类型或可以转换为同一类型。
```

### switch 语句

switch 语句用于处理“一个变量对应多个固定值”的情况。

基本语法:

```CPP
switch (表达式) {
    case 常量1:
        // 执行代码
        break;
    case 常量2:
        // 执行代码
        break;
    default:
        // 默认执行
}
```

代码演示:

```CPP
int day{3};

switch (day) {
    case 1:
        std::cout << "今天是星期一" << std::endl;
        break;
    case 2:
        std::cout << "今天是星期二" << std::endl;
        break;
    case 3:
        std::cout << "今天是星期三" << std::endl;
        break;
    default:
        std::cout << "未知日期" << std::endl;
}
```

```{attention}
switch 不支持字符串（std::string）或浮点数（float / double），只能用于整数类型或枚举类型。

break 的作用是终止当前 case 并跳出 switch 语句，如果不写 break switch 则会发生“穿透”继续执行后续 case。
```

在 switch 语句中，如果没有 break，程序会继续执行下一个 case，这种行为称为穿透（fallthrough）。

代码演示:

```CPP
int x{1};

switch (x) {
    case 1:
        std::cout << "1" << std::endl;
    case 2:
        std::cout << "2" << std::endl;
}
```

输出结果:

```Bash
1
2
```

如果忘记写 break，switch 会发生“穿透”，这往往是最常见的逻辑错误。

#### 显式 fallthrough（C++17）

自 C++17 开始可以使用：```[[fallthrough]];``` 来明确表示“这里是有意穿透”。

代码演示:

```CPP
int x{1};

switch (x) {
    case 1:
        std::cout << "1" << std::endl;
        [[fallthrough]];
    case 2:
        std::cout << "2" << std::endl;
        break;
}
```

[[fallthrough]] 用于告诉编译器：这里的穿透是“有意的”，不是错误。

- 不建议依赖隐式穿透（容易产生 bug）
- 如果必须穿透，推荐使用 [[fallthrough]]
- 每个 case 默认都应写 break，除非有明确设计

## 循环语句

用于根据条件表达式重复执行某段代码

### while 循环

基本语法:

```CPP
while (条件表达式) {
    // 当条件表达式成立时重复执行此处代码
}
```

代码演示:

```CPP
int i{0};

// 当 i 小于 5 时 重复执行 i 的自增操作
while (i < 5) {
    std::cout << i << std::endl;
    i++;
}
```

```{warning}
如果条件表达式始终为 true，while 循环将成为死循环，应确保循环中有改变条件的逻辑。
```

### do-while 循环

do-while 的特点是先执行代码然后再判断条件，do-while 中的代码至少会被执行一次。

基本语法:

```CPP
do {
    // 执行代码
} while (条件表达式);
```

代码演示:

```CPP
int i{0};

do {
    i++;
} while (i < 5);
```

### for 循环

最常用的循环语句

基本语法:

```CPP
for (初始化表达式; 条件表达式; 更新表达式) {
    // 循环体
}
```

```{attention}
for 循环中的表达式，要用分号进行分隔

当每次循环体中的代码结束后会自动执行一次更新表达式
```

代码演示:

```CPP
for (int i{0}; i < 5; i++) {
    // 执行 5 次
}

// 逻辑等价于下方代码：

int i{0};

while (i < 5) {
    // 代码
    i++;
}
```

for 循环适合“已知循环次数”的场景。

```{warning}
for(;;) 与 while(true) 在效果上完全一致，都是无限循环。

通常需要在循环内部通过 break 等方式手动退出，否则将一直执行。
```

#### 范围 for 循环

范围 for 循环是 C++11 引入的一种循环语法，用于简化对数组或容器的遍历操作。

基本语法:

```CPP
for (数据类型 变量名 : 容器) {
    // 循环体
}
```

代码演示:

```CPP
int arr[]{1, 2, 3, 4, 5};
// 依次输出数组中的每个元素
for (int value : arr) {
    std::cout << value << std::endl;
}
```

```{important}
范围 for 循环会依次遍历每个元素，适合用于读取数据。
```

## 跳转语句

跳转语句用于改变代码的执行流程。

### break

终止循环或 switch

代码演示:

```CPP
while (true) {
    break; // 直接退出循环
}
```

- 出现在switch条件语句中，作用是终止case并跳出switch
- 出现在循环语句中，作用是跳出当前的循环语句
- 出现在嵌套循环中，跳出最近的内层循环语句

### continue

continue 会跳过本次循环中剩余的代码，直接进入下一次循环判断。

代码演示:

```CPP
for (int i{0}; i < 5; i++) {
    if (i == 2) {
        continue; // 跳过本次循环直接进行下一次循环
    }
    std::cout << i << std::endl;
}
```

输出结果：0 1 3 4（2 被跳过）

### return

结束当前函数并返回结果

代码演示:

```CPP
int foo() {
    return 0;
}
```

如果在控制结构语句中使用同样会直接结束函数。

代码演示:

```CPP
int foo() {
    for (int i{0}; i < 5; i++){
        return 0; // return 会立即结束函数，后续代码将不会执行。
    }
}
```