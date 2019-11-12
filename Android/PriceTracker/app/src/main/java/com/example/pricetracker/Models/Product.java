package com.example.pricetracker.Models;

import com.example.pricetracker.Models.Enums;

public class Product {
    private int id;
    private String productName;
    private String productDescription;
    private String imageURL;
    private Enums.ProductType productType;
    private double price;

    public Product(int id, String productName, String productDescription, String imageURL, Enums.ProductType productType, double price) {
        this.id = id;
        this.productName = productName;
        this.productDescription = productDescription;
        this.imageURL = imageURL;
        this.productType = productType;
        this.price = price;
    }

    public int getId() {
        return id;
    }

    public String getProductName() {
        return productName;
    }

    public String getProductDescription() {
        return productDescription;
    }

    public String getImageURL() {
        return imageURL;
    }

    public Enums.ProductType getProductType() {
        return productType;
    }

    public double getPrice() {
        return price;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setProductName(String productName) {
        this.productName = productName;
    }

    public void setProductDescription(String productDescription) {
        this.productDescription = productDescription;
    }

    public void setImageURL(String imageURL) {
        this.imageURL = imageURL;
    }

    public void setProductType(Enums.ProductType productType) {
        this.productType = productType;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}
