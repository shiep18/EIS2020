package com.example.lianxi0520_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class Main2Activity extends AppCompatActivity {
    private EditText userName;
    private TextView passWord;
    private Button login,cancel,time;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        userName=findViewById(R.id.userName);
        passWord=findViewById(R.id.passWord);
        login=(Button)findViewById(R.id.button);
        cancel=(Button)findViewById(R.id.button1);
        time=(Button)findViewById(R.id.time);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent loginin=new Intent(Main2Activity.this,Main3Activity.class);
                String username_0=("zhuzhemin");
                String password_0=("123");
                if (username_0.equals(userName.getText().toString())&&password_0.equals((passWord.getText().toString()))){
                    loginin.putExtra("userName",userName.getText().toString());
                    loginin.putExtra("passWord",passWord.getText().toString());
                    startActivity(loginin);
                }
                else{
                    Toast.makeText(Main2Activity.this,"账号密码错误",Toast.LENGTH_SHORT).show();
                }
            }
        });
        cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent kobe=new Intent(Main2Activity.this,Main4Activity.class);
                startActivity(kobe);
            }
        });
        time.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent time1=new Intent(Main2Activity.this,MainActivity.class);
                String username_0=("zhuzhemin");
                String password_0=("123");
                if (username_0.equals(userName.getText().toString())&&password_0.equals((passWord.getText().toString()))){
                    startActivity(time1);
                }
                else{
                    Toast.makeText(Main2Activity.this,"账号密码错误",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
