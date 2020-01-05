package com.example.pricetracker.Activities;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.Lifecycle;
import androidx.lifecycle.OnLifecycleEvent;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.os.Parcelable;
import android.os.PersistableBundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import com.example.pricetracker.Adapters.ProductAdapter;
import com.example.pricetracker.Database.FirebaseViewHolder;
import com.example.pricetracker.Models.Check;
import com.example.pricetracker.Models.Enums;
import com.example.pricetracker.Models.Product;
import com.example.pricetracker.R;
import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class DashboardActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    private RecyclerView recyclerView;
    private FirebaseRecyclerAdapter<Product, FirebaseViewHolder> adapter;
    private ArrayList<Product> products;
    private DatabaseReference databaseReference;
    private FirebaseRecyclerOptions<Product> options;
    private String registeredUser;
    private Spinner productTypes;
    private Button addUrl;
    private EditText url;
    private String selectedCategory = null;
    private Double currentPrice = 0.0;

    private final String KEY_RECYCLER_STATE = "recycler_state";
    private static Bundle mBundleRecyclerViewState;

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        selectedCategory = productTypes.getItemAtPosition(position).toString();
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    @Override
    protected void onStart() {
        super.onStart();
        adapter.startListening();
    }

    @Override
    protected void onStop() {
        super.onStop();
        adapter.stopListening();
        mBundleRecyclerViewState = new Bundle();
        Parcelable listState = recyclerView.getLayoutManager().onSaveInstanceState();
        mBundleRecyclerViewState.putParcelable(KEY_RECYCLER_STATE, listState);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (mBundleRecyclerViewState != null) {
            Parcelable listState = mBundleRecyclerViewState.getParcelable(KEY_RECYCLER_STATE);
            recyclerView.getLayoutManager().onRestoreInstanceState(listState);
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        mBundleRecyclerViewState = new Bundle();
        Parcelable listState = recyclerView.getLayoutManager().onSaveInstanceState();
        mBundleRecyclerViewState.putParcelable(KEY_RECYCLER_STATE, listState);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        registeredUser = getIntent().getStringExtra("Username");
        setTitle("Hello " + registeredUser + "!");
        initialize();
        fillRecyclerView();
        addUrl.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!url.getText().toString().isEmpty() || selectedCategory == null) {
                    addNewUrl();
                }
                else{
                    Toast.makeText(getApplicationContext(),"Please fill all fields!", Toast.LENGTH_LONG).show();

                }
            }
        });

    }

    private void addNewUrl(){

        Map <String, String> product = new HashMap<>();
        product.put("category", selectedCategory);
        product.put("url", url.getText().toString());
        final DatabaseReference reference = FirebaseDatabase.getInstance().getReference("NEW/" + registeredUser + "/");
        reference.push().setValue(product).addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                Toast.makeText(getApplicationContext(),"Url added", Toast.LENGTH_LONG).show();

            }
        });
    }

    private void initialize(){
        productTypes = findViewById(R.id.productTypes);
        url = findViewById(R.id.url);
        addUrl = findViewById(R.id.addUrl);
        String[] productName = getTypes();
        ArrayAdapter <String> types = new ArrayAdapter<>(DashboardActivity.this, android.R.layout.simple_spinner_item, productName);
        types.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        productTypes.setAdapter(types);
        productTypes.setOnItemSelectedListener(this);
    }

    public static String[] getTypes(){
        LinkedList<String> types = new LinkedList<>();
        for(Enums.ProductType p : Enums.ProductType.values()){
            types.add(p.name());
        }
        return types.toArray(new String[(types.size())]);
    }

    private void fillRecyclerView(){
        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        products = new ArrayList<>();
        databaseReference = FirebaseDatabase.getInstance().getReference().child("USERS/" + registeredUser + "/");
        databaseReference.keepSynced(true);
        options = new FirebaseRecyclerOptions.Builder<Product>().setQuery(databaseReference, Product.class).build();

        adapter = new FirebaseRecyclerAdapter<Product, FirebaseViewHolder>(options) {
            @Override
            protected void onBindViewHolder(@NonNull final FirebaseViewHolder holder, int position, final @NonNull Product model) {
                final String key = getRef(position).getKey();
                fillPriceValue(key, holder);
                if(model.getName().length() > 35){
                    holder.name.setText(model.getName().substring(0, 20) + "\n" + model.getName().substring(20, 35) + "...");
                }
                else{
                    holder.name.setText(model.getName());
                }
                holder.category.setText(model.getCategory());
                holder.currency.setText(model.getCurrency());
                //holder.price.setText(currentPrice.toString());
                holder.itemView.setOnClickListener(new View.OnClickListener(){
                    @Override
                    public void onClick(View v) {
                        Intent intent = new Intent(DashboardActivity.this, ProductDetailActivity.class);
                        intent.putExtra("product", model);
                        intent.putExtra("price", holder.price.getText().toString());
                        intent.putExtra("key", key);
                        intent.putExtra("username", registeredUser);
                        startActivity(intent);
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

    private void fillPriceValue(String key, final FirebaseViewHolder holder){


        Query query = databaseReference.child(key + "/check").orderByChild("check");

        query.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                for(DataSnapshot data : dataSnapshot.getChildren()){
                    Check check = data.getValue(Check.class);
                   currentPrice = check.getPrice();
                   holder.price.setText(check.getPrice().toString());
                   break;
                }


            }


            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

    }

}
