
import java.util.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

class User {
    String user_id;
    int time_stamp;

    User(String user_id, int time_stamp) {
        this.user_id = user_id;
        this.time_stamp = time_stamp;
    }
}

class Document {
    String doc_id;

    Document(String doc_id) {
        this.doc_id = doc_id;
    }
}

public class DocumentLockManager {
    HashMap<String, User> document = new HashMap<>();

    boolean requestLock(String user_id, String doc_id, int time_stamp) {
        if (document.containsKey(doc_id)) {
            for (String temp : document.keySet()) {
                if (temp.equals(doc_id)) {
                    if (document.get(doc_id) != null) {
                        return false;
                    } else {
                        User u1 = new User(user_id, time_stamp);
                        document.put(doc_id, u1);
                    }
                }
            }
        } else {
            User u1 = new User(user_id, time_stamp);
            document.put(doc_id, u1);
        }
        return true;
    }

    boolean releaseLock(String user_id, String doc_id) {
        if (!document.containsKey(doc_id)) {
            System.out.println("document not found");
            return false;
        }
        for (String temp : document.keySet()) {
            if (temp.equals(doc_id)) {
                if (document.get(doc_id).user_id.equals(user_id)) {
                    document.put(temp, null);
                    System.out.println("Document Lock successfully removed");
                    return true;
                } else {
                    System.out.println("Access Denied ! " + user_id + " has no access to lock the document");
                    return false;
                }
            }
        }
        return true;
    }

    void cleanExpiredLocks(int time_stamp, int duration) {
        for (String temp : document.keySet()) {
            if (document.get(temp) != null) {
                int prev = document.get(temp).time_stamp;
                int prevYear = prev / 10000;
                int prevMonth = (prev / 100) % 100;
                int currentYear = time_stamp / 10000;
                int currentMonth = (time_stamp / 100) % 100;
                int months = 0;
                while (prevYear < currentYear || (prevYear == currentYear && prevMonth < currentMonth)) {
                    prevMonth++;
                    months++;
                    if (prevMonth > 12) {
                        prevMonth = 1;
                        prevYear++;
                    }
                }
                if (months >= duration) {
                    System.out.println("The duration for the document :" + temp + " has experied ");
                    System.out.println("Removing lock for the document :" + temp);
                    document.put(temp, null);
                }
            }
        }
    }

    public static void main(String[] args) {
        String user_id, doc_id;
        Scanner sc = new Scanner(System.in);
        LocalDate today = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");
        int time_stamp = Integer.parseInt(today.format(formatter));
        DocumentLockManager d = new DocumentLockManager();
        User u1 = new User("101", 20260701);
        d.document.put("1011", u1);
        while (true) {
            System.out.println("1.request Lock");
            System.out.println("2.release lock");
            System.out.println("3.Clear the locks for duration expired documents");
            System.out.println("4.exit");
            int ch = sc.nextInt();
            switch (ch) {
                case 1:
                    System.out.println("Enter user_id");
                    user_id = sc.next();
                    System.out.println("Enter doc_id");
                    doc_id = sc.next();
                    boolean check = d.requestLock(user_id, doc_id, time_stamp);
                    if (check)
                        System.out.println("Document locked for user : " + user_id + " at " + time_stamp);
                    else
                        System.out.println("Another user locked document " + doc_id);
                    break;
                case 2:
                    System.out.println("Enter user_id");
                    user_id = sc.next();
                    System.out.println("Enter doc_id");
                    doc_id = sc.next();
                    boolean check1 = d.releaseLock(user_id, doc_id);
                    break;
                case 3:
                    System.out.println("Enter duration to clear the documents locks(in months)");
                    int n = sc.nextInt();
                    d.cleanExpiredLocks(time_stamp, n);
                    System.out.println("Document locks cleared for the documents which has more than the duration of "
                            + n + " months");
                    break;
                case 4:
                    System.out.println("Exiting...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
