package com.example.test2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class login extends AppCompatActivity {
    private EditText userName;
    private TextView passWord;
    private Button login,cancnel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        userName=findViewById(R.id.userName);
        passWord=findViewById(R.id.passWord);
        login=findViewById(R.id.login);
        cancnel=findViewById(R.id.cancnel);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(login.this,video.class);
                String username_0=new String("fhz");
                String password_0=new String("123");
                if (username_0.equals(userName.getText().toString()) && password_0.equals(passWord.getText().toString())){
                    intent.putExtra("userName",userName.getText().toString());
                    intent.putExtra("passWord",passWord.getText().toString());
                    startActivity(intent);
                }
                else{
                    Toast.makeText(login.this,"error",Toast.LENGTH_SHORT).show();
                }
            }
        });

    }
}
