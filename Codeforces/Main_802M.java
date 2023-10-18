import java.util.*;
import java.util.stream.Collectors;

public class Main_802M {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int k = Integer.parseInt(line.split(" ")[1]);
        line = sc.nextLine();
        List<Integer> list = Arrays.stream(line.split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        list.sort(Comparator.naturalOrder());
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += list.get(i);
        }
        System.out.println(sum);
    }
}