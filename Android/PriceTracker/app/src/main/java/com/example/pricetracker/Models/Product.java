package com.example.pricetracker.Models;

import android.os.Parcel;
import android.os.Parcelable;

import com.example.pricetracker.Models.Enums;

public class Product implements Parcelable {
    private int id;
    private String productName;
    private String productDescription;
    private String imageURL;
    private Enums.ProductType productType;
    private Double price;

    public Product(){

    }
    public Product(int id, String productName, String productDescription, String imageURL, Enums.ProductType productType, Double price) {
        this.id = id;
        this.productName = productName;
        this.productDescription = productDescription;
        this.imageURL = imageURL;
        this.productType = productType;
        this.price = price;
    }

    public static final Creator<Product> CREATOR = new Creator<Product>() {
        @Override
        public Product createFromParcel(Parcel in) {
            return new Product(in);
        }

        @Override
        public Product[] newArray(int size) {
            return new Product[size];
        }
    };

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

    public Double getPrice() {
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

    public void setPrice(Double price) {
        this.price = price;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(productName);
        dest.writeString(productDescription);
        dest.writeDouble(price);
        dest.writeString(productType.toString());

    }

    public Product(Parcel parcel){
        productName = parcel.readString();
        productDescription = parcel.readString();
        price = parcel.readDouble();
        productType = Enums.ProductType.valueOf(parcel.readString());
        //imageURL = parcel.readString();
    }
}
