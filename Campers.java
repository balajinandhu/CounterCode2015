import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Campers {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        HashMap<Integer,Integer> campers = new HashMap<Integer, Integer>();
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[K];
        for(int i=0;i<K;i++) {
            arr[i] = sc.nextInt();
            campers.put(arr[i], i + 1);
            //campers.put(arr[i], i - 1);
        }
        for(int i=1;i<=N;i++){

            if((campers.containsKey(i+1)||campers.containsKey(i-1)||campers.containsKey(i)))
                continue;
            else {
                campers.put(i, i + 1);
              //  campers.put(i,i-1);
            }
        }
        System.out.print(campers.keySet().size());



    }
}