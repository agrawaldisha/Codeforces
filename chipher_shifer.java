// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int test=sc.nextInt();
        while(test-->0)
        {
            int n=sc.nextInt();
            String str=sc.next();
            String ans="";
            for(int i=0;i<str.length();i++){
                ans+=str.charAt(i);
                i=str.indexOf(str.charAt(i),i+1);
            }
        System.out.println(ans);
        }
    }
}
