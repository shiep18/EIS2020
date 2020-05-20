package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class Main2Activity extends AppCompatActivity {
    private EditText username;
    private TextView password;
    private Button login, cancnel,button5;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        username=findViewById(R.id.username);
        password=findViewById(R.id.password);
        login=findViewById(R.id.button);
        cancnel=findViewById(R.id.button2);
        button5=findViewById(R.id.button5);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Main2Activity.this, Main3Activity.class);
                String username_0 = new String(  "test");
                String password_0 = new String(  "password123");
                if (username_0.equals(username.getText().toString()) && password_0.equals(password.getText().toString())) {
                    intent.putExtra("username", username.getText().toString());
                    intent.putExtra("password", password.getText().toString());
                    startActivity(intent);
                }
                else {
                    Toast.makeText( Main2Activity.this,  "erros", Toast.LENGTH_SHORT).show();
                }
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Main2Activity.this,MainActivity.class);
                startActivity(intent);
            }
        });

    }
}
