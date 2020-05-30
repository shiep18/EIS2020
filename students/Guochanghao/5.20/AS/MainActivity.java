package com.example.video;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private EditText userName;
    private TextView passWord;
    private Button login,cancnel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        userName=findViewById(R.id.userName);
        passWord=findViewById(R.id.passWord);
        login=findViewById(R.id.button);
        cancnel=findViewById(R.id.button4);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(MainActivity.this,Main2Activity.class);
                String username_0 = new String("test");
                String password_0 = new String("password123");
                if (username_0.equals(userName.getText().toString()) && password_0.equals(passWord.getText().toString())){
                    intent.putExtra("userName",userName.getText().toString());
                    intent.putExtra("password",passWord.getText().toString());
                    startActivity(intent);
                }
                else{
                    Toast.makeText(MainActivity.this,"账号密码错误",Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}