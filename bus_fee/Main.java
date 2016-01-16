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
        int sumFare = 0;
        for (int price: p.getPrices()) {
            sumFare += new Main.BusFare(price, p.getAdultNum(), p.getChildNum(), p.getInfantNum()).fare();
        }
        System.out.println(sumFare);
    }

    static class Parser {
        private ArrayList<Integer> prices;
        private int adultNum;
        private int childNum;
        private int infantNum;

        public ArrayList<Integer> getPrices() {
            return prices;
        }

        public int getAdultNum() {
            return adultNum;
        }
        public int getChildNum() {
            return childNum;
        }

        public int getInfantNum() {
            return infantNum;
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
            this.adultNum = 0;
            this.childNum = 0;
            this.infantNum = 0;
            for (String symbol : str.split(",")) {
                if (symbol.equals("A")) {
                    this.adultNum += 1;
                } else if (symbol.equals("C")) {
                    this.childNum += 1;
                } else {
                    this.infantNum += 1;
                }
            }
        }
    }

    static class BusFare {

        private int adultPrice;
        private int adultNum;
        private int childNum;
        private int infantNum;

        public BusFare(int adultPrice, int adultNum, int childNum, int infantNum) {
            this.adultPrice = adultPrice;
            this.adultNum = adultNum;
            this.childNum = childNum;
            this.infantNum = infantNum;
            // System.out.println("dump");
            // System.out.println(adultsFare());
            // System.out.println(childsFare());
        }

        /** 料金計算結果 */
        public int fare() {
            return this.adultsFare() + this.childsFare();
        }

        private int adultsFare() {
            return this.adultPrice * this.adultNum;
        }

        private int childsFare() {
            return this.childPrice() * this.applyChildCount();
        }

        /** 子供料金に該当する人数 */
        private int applyChildCount() {
            return this.childNum + this.discountedInfantNum();
        }

        /** 子供料金 */
        private int childPrice() {
            return ((int) Math.ceil(this.adultPrice / 20.0f)) * 10;
        }

        /** 無料にならない幼児の人数 */
        private int discountedInfantNum() {
            return Math.max(0, this.infantNum - this.adultNum * 2);
        }
    }
}
