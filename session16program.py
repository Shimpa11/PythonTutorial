cppProgram="""
#include <iostream>

using namespace std;

int main()
{
    cout<<"Hello World";

    return 0;
}
"""

javaProgram="""class main{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
"""

dartProgram="""
void main() {
  
  print('Hello');
   
}

"""

goProgram="""

package main
import "fmt"
func main() {
    fmt.Println("hello world")
}
"""

javascriptProgram="""


<html>

<body>

  <p>Before the script...</p>

  <script>
    alert( 'Hello, world!' );
  </script>

  <p>...After the script.</p>

</body>

</html>

"""

print(cppProgram)
print("&&&&&&&&&&&&&&&&&&&&&&&&")


print(javaProgram)
print("&&&&&&&&&&&&&&&&&&&&&&&&")

print(goProgram)
print("&&&&&&&&&&&&&&&&&&&&&&&&")

print(javascriptProgram)
print("&&&&&&&&&&&&&&&&&&&&&&&&")

file1=open("C:\Java_Introduction\Myapp.cpp","w")
file1.write(cppProgram)
file1.close()

file2=open("C:\Java_Introduction\MyApp.java","w")
file2.write(javaProgram)
file2.close()


file3=open("C:\Java_Introduction\MyApp.dart","w")
file3.write(dartProgram)
file3.close()

file4=open("C:\Java_Introduction\helloworld.go","w")
file4.write(goProgram)
file4.close()




file5=open("C:\Java_Introduction\hello.js","w")
file5.write(javascriptProgram)
file5.close()


print("PROGRAMS CREATED")

