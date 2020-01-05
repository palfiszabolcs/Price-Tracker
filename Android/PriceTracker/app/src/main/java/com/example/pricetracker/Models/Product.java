package com.example.pricetracker.Models;

import android.os.Parcel;
import android.os.Parcelable;

import com.example.pricetracker.Models.Enums;

import java.util.ArrayList;

public class Product implements Parcelable {
    private String category;
    private String currency;
    private String imageUrl;
    private String name;
    private String url;
    private ArrayList<Check> check;


    public Product() {
    }

    public Product(String category, String currency, String imageUrl, String name, String url, ArrayList<Check> check) {
        this.category = category;
        this.currency = currency;
        this.imageUrl = imageUrl;
        this.name = name;
        this.url = url;
        this.check = check;
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

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getCurrency() {
        return currency;
    }

    public void setCurrency(String currency) {
        this.currency = currency;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public void setImageUrl(String imageUrl) {
        this.imageUrl = imageUrl;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


    public void setCheck(ArrayList<Check> check) {
        this.check = check;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    public Product(Parcel parcel) {
        category = parcel.readString();
        currency = parcel.readString();
        imageUrl = parcel.readString();
        name = parcel.readString();
        url = parcel.readString();
    }
    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(category);
        dest.writeString(currency);
        dest.writeString(imageUrl);
        dest.writeString(name);
        dest.writeString(url);
    }
}
