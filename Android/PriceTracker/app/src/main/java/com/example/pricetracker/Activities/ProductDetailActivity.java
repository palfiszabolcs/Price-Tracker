package com.example.pricetracker.Activities;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.pricetracker.Database.FirebaseViewHolder;
import com.example.pricetracker.Models.Check;
import com.example.pricetracker.Models.Product;
import com.example.pricetracker.R;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet;
import com.github.mikephil.charting.listener.OnChartGestureListener;
import com.github.mikephil.charting.listener.OnChartValueSelectedListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ProductDetailActivity extends AppCompatActivity {

    private static  final String TAG = "Details";


    private Button viewChart;
    private TextView name, url, category, currency, price;
    private ImageView productImage;
    final Map <String, Double> map = new HashMap<>();

    @Override
    public void onBackPressed() {
        // TODO Auto-generated method stub
        super.onBackPressed();
        ProductDetailActivity.this.overridePendingTransition(R.anim.splash_in,
                R.anim.splash_out);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_detail);
        overridePendingTransition(R.anim.splash_in, R.anim.splash_out);
        setTitle("Product detail");
        Product product = getIntent().getParcelableExtra("product");
        //Toast.makeText(this, product.getProductName() + " " + product.getProductDescription(), Toast.LENGTH_SHORT).show();
        setContents(product);
        getCheckValues();
        viewChart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ProductDetailActivity.this, ChartActivity.class);
                intent.putExtra("chart", (Serializable)map);
                startActivity(intent);
            }
        });
    }

    void setContents(Product product){
        name = findViewById(R.id.name);
        url = findViewById(R.id.url);
        category = findViewById(R.id.category);
        currency = findViewById(R.id.currency);
        viewChart = findViewById(R.id.viewChart);
        productImage = findViewById(R.id.productImage);
        price = findViewById(R.id.price);
        name.setText(product.getName());
        url.setText(product.getUrl());
        category.setText(product.getCategory());
        currency.setText(product.getCurrency());
        price.setText(getIntent().getStringExtra("price"));

        if(product.getCategory().equals("Sports"))
            productImage.setImageResource(R.drawable.sports);
        if(product.getCategory().equals("Vehicles"))
            productImage.setImageResource(R.drawable.vehicles);
        if(product.getCategory().equals("Clothing"))
            productImage.setImageResource(R.drawable.clothing);
        if(product.getCategory().equals("Other"))
            productImage.setImageResource(R.drawable.other);
        if(product.getCategory().equals("Electronics"))
            productImage.setImageResource(R.drawable.electronics);

    }

    private void getCheckValues(){
    String key = getIntent().getStringExtra("key");
    String username = getIntent().getStringExtra("username");
       DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference().child("USERS/" + username + "/" + key + "/check");
        Query query = databaseReference.orderByChild("check");


        query.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                for(DataSnapshot data : dataSnapshot.getChildren()){
                    Check check = data.getValue(Check.class);
                    map.put(check.getDate(), check.getPrice());
                }


            }


            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

    }



}