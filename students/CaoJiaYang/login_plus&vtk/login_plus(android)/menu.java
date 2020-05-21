package com.example.two;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import static com.example.two.R.*;
public class menu extends AppCompatActivity {
    private EditText userName;
    private TextView passWord;
    private Button login,cancnel,time;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
        userName=findViewById(id.username);
        passWord=findViewById(id.password);
        login=findViewById(id.button);
        time=findViewById(id.button3);
        cancnel=findViewById(id.button2);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(menu.this, player.class);
                String username_0=new String("cjy");
                String password_0=new String("1234");
                if(username_0.equals(userName.getText().toString()) && password_0.equals(passWord.getText().toString())) {
                    intent.putExtra("username", userName.getText().toString());
                    intent.putExtra("password", passWord.getText().toString());
//                    intent.putExtra("");
                    startActivity(intent);
                }
            }
        });
        time.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(menu.this, time.class);
                startActivity(intent);
            }
        });
    }
}
