package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private EditText username;
    private TextView password;
    private Button login,cancnel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username=findViewById(R.id.username);
        password=findViewById(R.id.password);
        login=findViewById(R.id.login);
        cancnel=findViewById(R.id.cancnel);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this,Main2Activity.class);
                String username_0 = new String("test");
                String password_0 = new String("12345678");
                if(username_0.equals(username.getText().toString())&&password_0.equals(password.getText().toString())) {
                    intent.putExtra("username", username.getText().toString());
                    intent.putExtra("password", password.getText().toString());
                    startActivity(intent);
                }
                else{
                    Toast.makeText(MainActivity.this,"账号密码错误",Toast.LENGTH_SHORT).show();
                    }

            }
        });
    }
}
