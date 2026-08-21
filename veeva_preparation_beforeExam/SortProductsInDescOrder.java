import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

class Product {

     int p_code;
     int price;
     String company;
    Product(int p_code, int price, String company) {
        this.p_code = p_code;
        this.price = price;
        this.company = company;
    }
    public int getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "Product Code = " + p_code +
               ", Price = " + price +
               ", Company = " + company;
    }
}

public class SortProductsInDescOrder {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Category -> List of Products
        HashMap<String, List<Product>> hm = new HashMap<>();

        // Laptops Category
        List<Product> laptops = new ArrayList<>();

        laptops.add(new Product(108, 300000, "HP"));
        laptops.add(new Product(101, 35000, "Samsung"));
        laptops.add(new Product(102, 50000, "Lenovo"));
        laptops.add(new Product(105, 75000, "Dell"));
        hm.put("Laptops", laptops);
        // Air Conditioner Category
        List<Product> airConditioners = new ArrayList<>();
        airConditioners.add(new Product(103, 90000, "Whirlpool"));
        airConditioners.add(new Product(104, 100000, "LG"));
        hm.put("Air-Conditioner", airConditioners);
        while (true) {

            System.out.print("Enter category to view products (exit to quit): ");

            String category = sc.next();

            if (category.equalsIgnoreCase("exit")) {
                System.out.println("Program terminated.");
                break;
            }

            if (!hm.containsKey(category)) {
                System.out.println("Category not available.\n");
                continue;
            }
            List<Product> products = hm.get(category);

            
            Collections.sort(products,(a,b)->b.getPrice()-a.getPrice());

            System.out.println("category is " + category);

            for(Product product1:hm.get(category))
            {
                System.out.println(product1);
            }


        
        }

    }
}