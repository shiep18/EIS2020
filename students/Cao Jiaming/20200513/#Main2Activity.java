
#Main2Activity.java 
package com.example.myapplication;



import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;

import android.os.Bundle;

import android.view.View;

import android.widget.Button;

import static com.example.myapplication.R.*;


public class Main2Activity extends AppCompatActivity {

    private Button login;





    @Override

    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main2);

        login=findViewById(R.id.button3);

        login.setOnClickListener(new View.OnClickListener() {

            @Override

            public void onClick(View v) {

                Intent intent =new Intent(Main2Activity.this,MainActivity.class);

                startActivity(intent);

            }

        });

    }

}