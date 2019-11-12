package com.example.pricetracker.Models;

import com.example.pricetracker.Models.Product;

import java.util.ArrayList;

public class User {
    private String userName;
    private String email;
    private String password;
    private ArrayList<Product> products = new ArrayList<>();

    public User(String userName, String email, String password) {
        this.userName = userName;
        this.email = email;
        this.password = password;
    }

    public String getUserName() {
        return userName;
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void addProduct(Product product){
        products.add(product);
    }
}
