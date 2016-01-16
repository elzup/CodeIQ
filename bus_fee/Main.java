import java.lang.Integer;
import java.lang.Math;
import java.lang.System;
import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        Parser p = new Main.Parser(line);
        GroupFare groupFare = new Main.GroupFare(p.getPeoples());
        for (int price: p.getPrices()) {
            groupFare.addFare(price);
        }
        System.out.println(groupFare.pay());
    }

    static class Parser {
        private ArrayList<Integer> prices;
        private ArrayList<People> peoples;

        public ArrayList<Integer> getPrices() {
            return prices;
        }

        public ArrayList<People> getPeoples() {
            return peoples;
        }

        public Parser(String text) {
            String[] params = text.split(":");
            this.parsePrice(params[0]);
            this.parsePeopleNumber(params[1]);
        }

        private void parsePrice(String str) {
            this.prices = new ArrayList<>();
            for (String ns: str.split(",")) {
                this.prices.add(Integer.valueOf(ns));
            }
        }

        private void parsePeopleNumber(String str) {
            this.peoples = new ArrayList<>();
            for (String symbol : str.split(",")) {
                People.AgeClass ageClass = null;
                boolean hasTicket = false;
                boolean hasSpecialTicket = false;
                if (symbol.charAt(0) == 'A') {
                    ageClass = People.AgeClass.ADULT;
                } else if (symbol.charAt(0) == 'C') {
                    ageClass = People.AgeClass.CHILD;
                } else {
                    ageClass = People.AgeClass.INFANT;
                }
                if (symbol.charAt(1) == 'p') {
                    hasTicket = true;
                } else if (symbol.charAt(1) == 'x') {
                    hasSpecialTicket = true;
                }
                peoples.add(new Main.People(ageClass, hasTicket, hasSpecialTicket));
            }
        }
    }

    static class People {
        public static enum AgeClass { ADULT, CHILD, INFANT };
        private AgeClass ageClass;
        private boolean hasTicket;
        private boolean hasSpecialTicket;

        public AgeClass getAgeClass() {
            return ageClass;
        }
        public void setAgeClass(AgeClass ageClass) {
            this.ageClass = ageClass;
        }

        public boolean hasTicket() {
            return hasTicket;
        }
        public void setHasTicket(boolean hasTicket) {
            this.hasTicket = hasTicket;
        }

        public boolean hasSpecialTicket() {
            return hasSpecialTicket;
        }
        public void setHasSpecialTicket(boolean hasSpecialTicket) {
            this.hasSpecialTicket = hasSpecialTicket;
        }

        public People(AgeClass ageClass, boolean hasTicket, boolean hasSpecialTicket) {
            this.ageClass = ageClass;
            this.hasTicket = hasTicket;
            this.hasSpecialTicket = hasSpecialTicket;
        }

        public boolean isAdult() {
            return this.ageClass == AgeClass.ADULT;
        }
        public boolean isChild() {
            return this.ageClass == AgeClass.CHILD;
        }
        public boolean isInfant() {
            return this.ageClass == AgeClass.INFANT;
        }
    }

    static class GroupFare {

        private ArrayList<People> peoples;
        // 実際の人数
        private int adultNum = 0;
        private int childNum = 0;
        private int infantNum = 0;

        // 一般料金でカウントされる人数
        private int adultCount = 0;
        private int childCount = 0;

        // 特別料金でカウントされる人数
        private int adultSpecialCount = 0;
        private int childSpecialCount = 0;

        // 各料金
        private int adultPay = 0;
        private int childPay = 0;
        private int adultSpecialPay = 0;
        private int childSpecialPay = 0;

        public GroupFare(ArrayList<People> peoples) {
            this.peoples = peoples;
            this.calcCount();
            // System.out.println("dump");
            // System.out.println(this.adultCount);
            // System.out.println(this.adultSpecialCount);
            // System.out.println(this.childCount);
            // System.out.println(this.childSpecialCount);
        }

        private void calcCount() {
            int adultTicketCount = 0;
            int childTicketCount = 0;
            int infantTicketCount = 0;

            this.adultSpecialCount = 0;
            this.childSpecialCount = 0;
            int infantSpecialCount = 0;

            for (People people : peoples) {
                if (people.isAdult()) {
                    this.adultNum += 1;
                    if (people.hasTicket()) {
                        adultTicketCount += 1;
                    } else if (people.hasSpecialTicket()) {
                        this.adultSpecialCount += 1;
                    }
                } else if (people.isChild()) {
                    this.childNum += 1;
                    if (people.hasTicket()) {
                        childTicketCount += 1;
                    } else if (people.hasSpecialTicket()) {
                        this.childSpecialCount += 1;
                    }
                } else if (people.isInfant()) {
                    this.infantNum += 1;
                    if (people.hasTicket()) {
                        infantTicketCount += 1;
                    } else if (people.hasSpecialTicket()) {
                        infantSpecialCount += 1;
                    }
                }
            }
            this.adultCount = this.adultNum - adultTicketCount - this.adultSpecialCount;
            this.childCount = this.childNum - childTicketCount - this.childSpecialCount;
            // 幼児と子供計算
            int infantCount = this.infantNum - infantTicketCount - infantSpecialCount;
            int infantDiscount = this.adultNum * 2;
            if (infantDiscount > 0) {
                infantCount -= infantDiscount;
                if (infantCount < 0) {
                    infantSpecialCount += infantCount;
                    infantCount = 0;
                }
            }
            // System.out.println("infant");
            // System.out.println(infantCount);
            // System.out.println(infantTicketCount);
            // System.out.println(infantSpecialCount);
            if (infantCount > 0) {
                this.childCount += infantCount;
            }
            if (infantSpecialCount > 0) {
                this.childSpecialCount += infantSpecialCount;
            }
        }

        /** 料金計算結果 */
        public void addFare(int price) {
            this.adultPay += price;
            this.adultSpecialPay += toSpecialPrice(price);
            int inChildPay = toChildPrice(price);
            this.childPay += inChildPay;
            this.childSpecialPay += toSpecialPrice(inChildPay);
        }

        public int pay() {
            int adultPrice = Math.min(910, this.adultPay);
            int adultSpecialPrice = Math.min(510, this.adultSpecialPay);
            int childPrice = Math.min(460, this.childPay);
            int childSpecialPrice = Math.min(260, this.childSpecialPay);
            return adultPrice * this.adultCount +
                    adultSpecialPrice * this.adultSpecialCount +
                    childPrice * this.childCount +
                    childSpecialPrice * this.childSpecialCount;
        }

        public int toChildPrice(int price) {
            return ((int) Math.ceil(price / 20.0f)) * 10;
        }

        public int toSpecialPrice(int price) {
            return ((int) Math.ceil(price * 0.056f)) * 10;
        }
    }
}
