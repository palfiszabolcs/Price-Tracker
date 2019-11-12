package com.example.pricetracker;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText username;
    private EditText password;
    private CheckBox rememberMe;
    private Button signInButton;
    private TextView registerLink;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getIds();
        registerLink.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"Register link clicked", Toast.LENGTH_LONG).show();
                Intent registerActivity = new Intent(getApplicationContext(), RegisterActivity.class);
                startActivity(registerActivity);
            }
        });

        signInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(),"Sign In button clicked", Toast.LENGTH_LONG).show();
                Intent dashboardActivity= new Intent(getApplicationContext(), DashboardActivity.class);
                startActivity(dashboardActivity);
            }
        });
    }

    public void getIds(){
        username = findViewById(R.id.userName);
        password = findViewById(R.id.password);
        rememberMe = findViewById(R.id.rememberMe);
        signInButton = findViewById(R.id.signInButton);
        registerLink = findViewById(R.id.registerLink);
    }
}
