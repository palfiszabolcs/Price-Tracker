package com.example.pricetracker.Activities;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.example.pricetracker.Adapters.ProductAdapter;
import com.example.pricetracker.Database.FirebaseViewHolder;
import com.example.pricetracker.Models.Enums;
import com.example.pricetracker.Models.Product;
import com.example.pricetracker.R;
import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.ArrayList;
import java.util.List;

public class DashboardActivity extends AppCompatActivity {
    private RecyclerView recyclerView;
    private FirebaseRecyclerAdapter<Product, FirebaseViewHolder> adapter;
    private ArrayList<Product> products;
    private DatabaseReference databaseReference;
    private FirebaseRecyclerOptions<Product> options;

    @Override
    protected void onStart() {
        super.onStart();
        adapter.startListening();
    }

    @Override
    protected void onStop() {
        super.onStop();
        adapter.stopListening();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        setRecyclerView();
    }

    public void setRecyclerView(){
        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setHasFixedSize(true);
        products = new ArrayList<>();
        databaseReference = FirebaseDatabase.getInstance().getReference().child("Products");
        databaseReference.keepSynced(true);
        options = new FirebaseRecyclerOptions.Builder<Product>().setQuery(databaseReference, Product.class).build();

        adapter = new FirebaseRecyclerAdapter<Product, FirebaseViewHolder>(options) {
            @Override
            protected void onBindViewHolder(@NonNull FirebaseViewHolder holder, int position, @NonNull final Product model) {
                holder.productName.setText(model.getProductName());
                holder.productDescription.setText(model.getProductDescription());
                holder.productPrice.setText(Double.toString(model.getPrice()));
                holder.productType.setText(model.getProductType().toString());
                holder.itemView.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        Intent details = new Intent(DashboardActivity.this, ProductDetailActivity.class);
                        details.putExtra("product", model);
                        startActivity(details);
                    }
                });
            }

            @NonNull
            @Override
            public FirebaseViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
                return new FirebaseViewHolder(LayoutInflater.from(DashboardActivity.this).inflate(R.layout.product_row, parent, false));
            }
        };
        recyclerView.setAdapter(adapter);

    }
}
