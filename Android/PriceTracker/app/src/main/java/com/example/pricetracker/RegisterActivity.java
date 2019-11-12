package com.example.pricetracker;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class RegisterActivity extends AppCompatActivity {

    private EditText signUpUserName;
    private EditText email;
    private EditText signUpPassword;
    private EditText confirmPassword;
    private Button confirmButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        getIds();
        confirmButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"Confirm button clicked", Toast.LENGTH_LONG).show();
                Intent loginActivity = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(loginActivity);
            }
        });
    }

    public void getIds(){
        signUpUserName = findViewById(R.id.signUpUserName);
        email = findViewById(R.id.email);
        signUpPassword = findViewById(R.id.signUpPassword);
        confirmPassword = findViewById(R.id.confirmPassword);
        confirmButton = findViewById(R.id.confirmButton);
    }
}
