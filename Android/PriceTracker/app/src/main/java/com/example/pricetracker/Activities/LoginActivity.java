package com.example.pricetracker.Activities;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.renderscript.Sampler;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.example.pricetracker.R;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

public class LoginActivity extends AppCompatActivity {

    private EditText username;
    private EditText password;
    private CheckBox rememberMe;
    private Button signInButton;
    private TextView registerLink;
    private Boolean saveLogin;
    private LinearLayout layout;
    SharedPreferences sharedPreferences;
    SharedPreferences.Editor editor;

    @Override
    public void onBackPressed() {
        // TODO Auto-generated method stub
        super.onBackPressed();
        LoginActivity.this.overridePendingTransition(R.anim.splash_in,
                R.anim.splash_out);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        overridePendingTransition(R.anim.splash_in, R.anim.splash_out);
        getIds();
        registerLink.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               // Toast.makeText(getApplicationContext(),"Register link clicked", Toast.LENGTH_LONG).show();
                Intent registerActivity = new Intent(getApplicationContext(), RegisterActivity.class);
                startActivity(registerActivity);
            }
        });

        saveLogin = sharedPreferences.getBoolean("saveLogin", true);
        if(saveLogin == true){
            username.setText(sharedPreferences.getString("userName", null));
            password.setText(sharedPreferences.getString("password", null));
        }

        signInButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //oast.makeText(getApplicationContext(),"Sign In button clicked", Toast.LENGTH_LONG).show();
                if(username.getText().toString().isEmpty() || password.getText().toString().isEmpty()){
                    Toast.makeText(getApplicationContext(),"Please fill all fields of data!", Toast.LENGTH_LONG).show();

                }
                DatabaseReference reference = FirebaseDatabase.getInstance().getReference("RegisteredUsers");
                Query query = reference.orderByChild("RegisteredUsers");
                query.addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        String key = null;
                        boolean incorrect = false;
                        for(DataSnapshot data : dataSnapshot.getChildren()){
                            if(data.child("Name").getValue().equals(username.getText().toString()) && !data.child("Password").getValue().equals(password.getText().toString())){
                                Toast.makeText(getApplicationContext(),"Incorrect password!!", Toast.LENGTH_LONG).show();
                                incorrect = true;
                                break;

                            }

                                if(data.child("Name").getValue().equals(username.getText().toString()) && data.child("Password").getValue().equals(password.getText().toString())){
                                key = data.getKey();
                                break;
                            }

                        }
                        if(incorrect==false){
                        if(key == null){
                            Toast.makeText(getApplicationContext(),"User not found!", Toast.LENGTH_LONG).show();

                        }
                        else {
                            Toast.makeText(getApplicationContext(),"Login successful!", Toast.LENGTH_LONG).show();
                            Intent dashboardActivity= new Intent(getApplicationContext(), DashboardActivity.class);
                            dashboardActivity.putExtra("Username", username.getText().toString());
                            startActivity(dashboardActivity);
                            if(rememberMe.isChecked()){
                                editor.putBoolean("saveLogin", true);
                                editor.putString("userName", username.getText().toString());
                                editor.putString("password", password.getText().toString());
                                editor.commit();
                            }
                        }
                        }
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                });

            }
        });
    }

    public void getIds(){
        username = findViewById(R.id.userName);
        password = findViewById(R.id.password);
        rememberMe = findViewById(R.id.rememberMe);
        signInButton = findViewById(R.id.signInButton);
        registerLink = findViewById(R.id.registerLink);
        sharedPreferences = getSharedPreferences("loginref", MODE_PRIVATE);
        editor = sharedPreferences.edit();
        layout = findViewById(R.id.layout);
        layout.getBackground().setAlpha(60);
    }
}
