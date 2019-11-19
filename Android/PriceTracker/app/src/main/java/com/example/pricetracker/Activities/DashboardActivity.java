package com.example.pricetracker.Activities;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import com.example.pricetracker.Adapters.ProductAdapter;
import com.example.pricetracker.Models.Enums;
import com.example.pricetracker.Models.Product;
import com.example.pricetracker.R;

import java.util.ArrayList;
import java.util.List;

public class DashboardActivity extends AppCompatActivity {
    RecyclerView recyclerView;
    RecyclerView.Adapter adapter;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        setRecyclerView();
    }

    public void setRecyclerView(){
        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        List<Product> products = new ArrayList<>();
        for(int i=0; i < 10; i++){
            Product product = new Product(i, "Product"+i, "Description"+i, "image"+i, Enums.ProductType.Laptop, 1999);
            products.add(product);
        }
        adapter = new ProductAdapter(products);
        recyclerView.setAdapter(adapter);
    }
}
