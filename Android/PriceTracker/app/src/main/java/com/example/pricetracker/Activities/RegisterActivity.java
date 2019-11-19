package com.example.pricetracker.Activities;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.pricetracker.Models.User;
import com.example.pricetracker.R;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;
import java.util.Map;

public class RegisterActivity extends AppCompatActivity {

    private EditText signUpUserName;
    private EditText email;
    private EditText signUpPassword;
    private EditText confirmPassword;
    private Button confirmButton;
    private FirebaseDatabase database;
    private DatabaseReference reference;
    private FirebaseAuth mAuth;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        getIds();
        confirmButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"Confirm button clicked", Toast.LENGTH_LONG).show();
                String username = signUpUserName.getText().toString();
                String password = signUpPassword.getText().toString();
                String userEmail = email.getText().toString();
                addNewUser();

            }
        });
    }

    public void getIds(){
        signUpUserName = findViewById(R.id.signUpUserName);
        email = findViewById(R.id.email);
        signUpPassword = findViewById(R.id.signUpPassword);
        confirmPassword = findViewById(R.id.confirmPassword);
        confirmButton = findViewById(R.id.confirmButton);
        mAuth = FirebaseAuth.getInstance();
    }

    public void addNewUser(){
        database = FirebaseDatabase.getInstance();
        reference = database.getReference("Users/");
        Map <String, String> user = new HashMap<>();
        user.put("Name", signUpUserName.getText().toString());
        user.put("Password", signUpPassword.getText().toString());
        reference.setValue(user).addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void aVoid) {
                Toast.makeText(getApplicationContext(),"Registration succesfull!", Toast.LENGTH_LONG).show();
                Intent loginActivity = new Intent(getApplicationContext(), LoginActivity.class);
                startActivity(loginActivity);
            }
        });

    }
}
