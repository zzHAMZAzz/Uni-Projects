package com.poppleton.christmas.crackers;

import java.text.NumberFormat;
import java.util.Locale;

public class employee {

    /* For the Employee, they will have a string for their name, and a double for pay rate*/
    private String name;
    private double rate;
    private String role;
    private int quantity;

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public String getName() { return name; }

    public void setName(String name) { this.name = name; }



    public employee(String name, String role, int quantity) {
        this.name = name;
        this.role = role;
        this.quantity = quantity;
    }
    public String getWorkerDetails()
    {
        return this.getName() + " is working as a " + this.getRole() + ".";
    }

    public String calculateWage()
    {
        double wage = 0;
        double firstBoxes = 1.11;
        double subsequentBoxes = 1.25;

        /* If they have completed more than or equal to 51 boxes, their wage is split into 2 and added together
        Else if they have completed 50 or less boxes, their wage is calculated by the first box wage * quantity
         */

        if (this.quantity >= 51) {
           /* Calculate the wage for the first 50 boxes */
           double wage1 = 50*firstBoxes;
           /* Calculate the subsequent boxes after 50 */
           double remainingQuantity = this.quantity - 50;
           /* Calculate the wage for every other box after 50 */
           double wage2 = remainingQuantity*subsequentBoxes;
           /* Finally add them together to get the final wage */
           wage = wage1 + wage2;
        } else {
            wage = this.quantity * firstBoxes;
        }

        /* Set locale currency to correctly print money values */
        Locale locale = new Locale ("en", "GB");
        NumberFormat cf = NumberFormat.getCurrencyInstance (locale);

        return this.getName() + " will receive a wage of " + cf.format(wage) + " for processing " + this.quantity + " units";
    }

    public static void main(String[] args) {
        /* Creating an employee named bob who has completed 45 units */
        employee Bob = new employee("Bob", "packer", 45);
        /* Print the employee details and wage for Bob */
        System.out.println(Bob.getWorkerDetails() + "\n" + Bob.calculateWage());

        System.out.println("");

        /* Create a second employee */
        employee John = new employee("John", "packer",76);
        System.out.println(John.getWorkerDetails() + "\n" + John.calculateWage());

    }
}
