#MainActivity.java
package com.example.myapplication;



import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;



import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import android.widget.EditText;

import android.widget.TextView;

import android.widget.Toast;

import static com.example.myapplication.R.*;

public class MainActivity extends AppCompatActivity {

    private EditText userName;

    private TextView passWord;

    private Button login,cancnel;



    @Override

    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        userName=findViewById(id.username);

        passWord=findViewById(id.password);

        login=findViewById(id.button);

        cancnel=findViewById(id.button2);

        login.setOnClickListener(new View.OnClickListener() {

            @Override

            public void onClick(View v) {

                Intent intent =new Intent(MainActivity.this,Main2Activity.class);

                String username_0=new String("cjy");

                String password_0=new String("1234");

                if(username_0.equals(userName.getText().toString()) && password_0.equals(passWord.getText().toString())) {

                    intent.putExtra("username", userName.getText().toString());

                    intent.putExtra("password", passWord.getText().toString());


                    startActivity(intent);

                }

            }

        });

    }

}
