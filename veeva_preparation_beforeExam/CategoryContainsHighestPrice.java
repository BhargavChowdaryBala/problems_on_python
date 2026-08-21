import java.util.ArrayList;
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

public class CategoryContainsHighestPrice {

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
        List<Product> airConditioners = new ArrayList<>();
        airConditioners.add(new Product(103, 90000, "Whirlpool"));
        airConditioners.add(new Product(104, 100000, "LG"));
        hm.put("Air-Conditioner", airConditioners);
        
        String s=null;
        int res=0;
        for(String category:hm.keySet())
        {
            List<Product> products=hm.get(category);
            for(Product p:products)
            {
                if(res<p.getPrice())
                {
                    res=p.getPrice();
                    s=category;
                }
            }
        }
        System.out.println("category with highest price is"+ s);
        System.out.println("Price is : " + res);

    }
}