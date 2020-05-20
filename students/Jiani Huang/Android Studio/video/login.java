package com.example.video;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class login extends AppCompatActivity {
    private EditText userName;
    private TextView passWord;
    private Button log,time,cancnel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);userName = findViewById(R.id.userName);
        passWord = findViewById(R.id.passWord);
        log = findViewById(R.id.log);
        cancnel = findViewById(R.id.cancnel);
        time = findViewById(R.id.time);
        log.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent_video = new Intent(login.this, MainActivity.class);
                String username_0 = new String("Lin");
                String password_0 = new String("19981127");
                if(username_0.equals(userName.getText().toString()) && password_0.equals(passWord.getText().toString())) {
                    intent_video.putExtra("userName",userName.getText().toString());
                    intent_video.putExtra("passWord",passWord.getText().toString());
                    startActivity(intent_video);
                }
                else{
                    Toast.makeText(login.this,"账号密码错误。",Toast.LENGTH_SHORT).show();
                }
            }
        });
        time.setOnClickListener(new View.OnClickListener() {
            Intent intent_time = new Intent(login.this, handler.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_time);
            }
        });
    }
}
