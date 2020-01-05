package com.example.pricetracker.Models;

import java.util.Date;

public class Check {
    private String date;
    private Double price;

    public Check() {

    }

    public Check(String date, Double price) {
        this.date = date;
        this.price = price;
    }

    public String getDate() {
        return date;
    }

    public Double getPrice() {
        return price;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public void setPrice(Double price) {
        this.price = price;
    }
}
