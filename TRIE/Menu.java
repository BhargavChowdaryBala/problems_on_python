import java.util.Scanner;

class TrieNode {
    TrieNode child[];
    int c = 0;
    int endcount;
    boolean isLeaf;

    TrieNode() {
        child = new TrieNode[26];
        isLeaf = false;
        c = 0;
        endcount = 0;
    }
}

class Trie {
    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    void insert(String s) {
        TrieNode curr = root;
        for (char ch : s.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                curr.child[ch - 'a'] = new TrieNode();
            }
            curr.child[ch - 'a'].c++;
            curr = curr.child[ch - 'a'];
        }
        curr.isLeaf = true;
        curr.endcount++;
    }

    boolean search(String s) {
        TrieNode curr = root;
        for (char ch : s.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return false;
            }
            curr = curr.child[ch - 'a'];
        }
        return curr.isLeaf;
    }

    boolean prefixsearch(String s) {
        TrieNode curr = root;
        for (char ch : s.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return false;
            }
            curr = curr.child[ch - 'a'];
        }
        return true;
    }

    int StringCount(String s) {
        TrieNode curr = root;
        for (char ch : s.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return 0;
            }
            curr = curr.child[ch - 'a'];
        }

        if (curr.isLeaf)
            return curr.endcount;
        else
            return 0;
    }

    int PrefixCount(String s) {
        TrieNode curr = root;
        for (char ch : s.toCharArray()) {
            if (curr.child[ch - 'a'] == null) {
                return 0;
            }
            curr = curr.child[ch - 'a'];
        }

        return curr.c;
    }
}

public class Menu {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Trie trie = new Trie();

        while (true) {
            System.out.println("\n----- TRIE MENU -----");
            System.out.println("1. Insert a string");
            System.out.println("2. Search a string");
            System.out.println("3. Prefix search");
            System.out.println("4. Count occurrences of a string");
            System.out.println("5. Count strings with given prefix");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();
            sc.nextLine(); 

            switch (choice) {
                case 1:
                    System.out.print("Enter string to insert: ");
                    String insertStr = sc.nextLine().toLowerCase();
                    trie.insert(insertStr);
                    System.out.println("Inserted successfully.");
                    break;

                case 2:
                    System.out.print("Enter string to search: ");
                    String searchStr = sc.nextLine().toLowerCase();
                    if (trie.search(searchStr)) {
                        System.out.println("String found in Trie.");
                    } else {
                        System.out.println("String not found in Trie.");
                    }
                    break;

                case 3:
                    System.out.print("Enter prefix to search: ");
                    String prefixStr = sc.nextLine().toLowerCase();
                    if (trie.prefixsearch(prefixStr)) {
                        System.out.println("Prefix exists in Trie.");
                    } else {
                        System.out.println("Prefix does not exist in Trie.");
                    }
                    break;

                case 4:
                    System.out.print("Enter string to count occurrences: ");
                    String countStr = sc.nextLine().toLowerCase();
                    System.out.println("Occurrences of \"" + countStr + "\" = " + trie.StringCount(countStr));
                    break;

                case 5:
                    System.out.print("Enter prefix to count strings: ");
                    String prefixCountStr = sc.nextLine().toLowerCase();
                    System.out.println("Number of strings with prefix \"" + prefixCountStr + "\" = " + trie.PrefixCount(prefixCountStr));
                    break;

                case 6:
                    System.out.println("Exiting program...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}